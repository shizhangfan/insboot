from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import Account, Target, RegisterWorker, Proxy, FirstName, LastName
from datetime import datetime, timedelta
import random
import time
import string
import json
import codecs
import datetime
import os.path
import logging
import urllib.request as request
from celery.utils.log import get_task_logger

try:
    from instagram_private_api import (
        Client, ClientError, ClientLoginError, Device,
        ClientCookieExpiredError, ClientLoginRequiredError,
        __version__ as client_version)
except ImportError:
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from .ins_api import (
        Client, ClientError, ClientLoginError, Device,
        ClientCookieExpiredError, ClientLoginRequiredError,
        __version__ as client_version)


API_BASE_URL = 'http://api.fxhyd.cn/UserInterface.aspx'
API_TOKEN = '00662039b612335469fc69b4410c1e9d9e7548129e01'

logger_celery = get_task_logger(__name__)
# celery -A insboot worker -l info -P eventlet -f celery.log


@shared_task
def print_hello():
    logger_celery.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("hello celery and django...")
    return "hello celery and django..."


@shared_task
def register_worker():
    worker = RegisterWorker.objects.get(pk=1)
    logger_celery.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    """
    if worker.working:
        # logger.info("注册机开始工作，时间：{}".format(str(datetime.datetime.utcnow())))
        register_times_per_proxy = worker.times_per_proxy
        register_duration = 15 * 60 / 4
        proxies = Proxy.objects.all()
        for proxy in proxies:
            # 分钟数
            register_times = [get_register_times(register_duration, i) for i in range(0, register_times_per_proxy)]
            # 毫秒
            register_times_mis = [time * 60 * 1000 for time in register_times]
            # 开始注册

    else:
        # logger.info("注册机未启动~， 时间：{}".format(str(datetime.datetime.utcnow())))
        print("注册机未启动")
    """


def get_register_times(duration, index):
    return index * duration + random.randint(0, duration)


def single_account_register():
    logging.basicConfig()
    logger = logging.getLogger('instagram_private_api')
    logger.setLevel(logging.INFO)

    # 随机获取 first name
    last_index = FirstName.objects.count()
    index1 = random.randint(0, last_index)
    first_name = FirstName.objects.all()[index1]

    # 随机获取 last name
    index2 = random.randint(0, last_index)
    last_name = LastName.objects.all()[index2]

    new_username = '{}.{}.{}'.format(random.randint(0, 99999), first_name, last_name)
    new_password = generate_password(size=random.randint(6, 10))
    phone = None
    try:
        phone = get_phone_number(0)
    except Exception as e:
        logger.error('{}{}', e, str(datetime.datetime.utcnow()))
        return

    creator = Client()
    creator.set_phone(phone)
    sms = get_phone_sms(phone, 0)
    creator.set_sms(phone, sms)

    create_res = creator.create()
    if create_res.get('result') == 'valid':
        # 注册成功，记录注册事件和账号
        new_account = Account(username=new_username, password=new_password, phone=phone)
        new_account.save()


def get_phone_sms(phone, try_number):
    """
    从易码平台获取短信 :http://www.51ym.me
    账号:shizhangfan  密码:kobebryant
    :param phone:
    :param try_number:
    :return:
    """
    if try_number > 10:
        raise Exception("请求次数超过10次，停止获取手机号码")

    url = '{0}?action=getsms&token={1}&itemid=项目编号&mobile={2}&release=1&timestamp={3}'\
        .format(API_BASE_URL, API_TOKEN, phone, time.mktime(datetime.datetime.now().timetuple()))

    req = request.Request(url)
    http_handler = request.HTTPHandler()
    opener = request.build_opener(*http_handler)
    response = opener.open(req, timeout=60)
    response_content = response.read().decode('utf8')

    if response_content.find('success') > 0:
        sms = response_content.split('|')[1]
        return sms
    else:
        return get_phone_number(try_number=try_number + 1)


def get_phone_number(try_number):
    """
    从易码平台获取新手机号 :http://www.51ym.me
    账号:shizhangfan  密码:kobebryant
    :return:
    """
    if try_number > 10:
        raise Exception("请求次数超过10次，停止获取手机号码")

    url = '{0}?action=getmobile&token={1}&itemid=项目编号&excludeno=170.171.180&' \
          'timestamp=TIMESTAMP'.format(API_BASE_URL, API_TOKEN, time.mktime(datetime.datetime.now().timetuple()))

    req = request.Request(url)
    http_handler = request.HTTPHandler()
    opener = request.build_opener(*http_handler)
    response = opener.open(req, timeout=15)
    response_content = response.read().decode('utf8')

    if response_content.find('success') > 0:
        phone = response_content.split('|')[1]
        return phone
    else:
        return get_phone_number(try_number=try_number + 1)


def generate_password(size=6, chars=string.ascii_lowercase + string.digits):
    """
    生成密码
    :param size: 密码的长度，默认为6
    :param chars: 密码的字符集
    :return:
    """
    return ''.join(random.choice(chars) for _ in range(size))


@shared_task
def follow_worker():
    # 获取所有账号
    accounts = Account.objects.all()
    # 获取账号之后，查看每个账号是否正在工作

    # 每个账号启动一个worker
    for account in accounts:
        single_account_follow_worker.delay(account)


@shared_task
def single_account_follow_worker(account):
    if account.working:
        setting = account.setting
        first_day = account.first_day
        now = datetime.datetime.now()
        working_days = (now - first_day).days
        if working_days > 7:
            # 大于七天
            max_follow_number = setting.max
            min_follow_number = setting.min
            # 根据最大值和最小值，随机获取一个值
            target_number = random.randint(min_follow_number, max_follow_number)
            target_per_hour = target_number / 8
            seconds = 60 * 60 / target_per_hour
            targets = Target.objects.all().filter(tag__exact='tag', status__exact='done')[target_number]

            for i in range(0, target_number):
                account.apply_async(targets[i], eta=now + timedelta(seconds=seconds))
        else:
            # 小于七天
            target_number_tmp = get_follow_count(working_days, setting)
            target_number = random.randint(target_number_tmp - 10, target_number_tmp + 10)
            target_per_hour = target_number / 8
            seconds = 60 * 60 / target_per_hour
            targets = Target.objects.all().filter(tag__exact='tag', status__exact='done')[target_number]

            for i in range(0, target_number):
                account.apply_async(targets[i], eta=now + timedelta(seconds=seconds))
    else:
        print("账号不在工作中")


def to_json(python_object):
    if isinstance(python_object, bytes):
        return {'__class__': 'bytes',
                '__value__': codecs.encode(python_object, 'base64').decode()}
    raise TypeError(repr(python_object) + ' is not JSON serializable')


def from_json(json_object):
    if '__class__' in json_object and json_object['__class__'] == 'bytes':
        return codecs.decode(json_object['__value__'].encode(), 'base64')
    return json_object


def onlogin_callback(api, new_settings_file):
    cache_settings = api.settings
    with open(new_settings_file, 'w') as outfile:
        json.dump(cache_settings, outfile, default=to_json)
        print('SAVED: {0!s}'.format(new_settings_file))


def follow(username, password, userid):
    logging.basicConfig()
    logger = logging.getLogger('instagram_private_api')
    logger.setLevel(logging.DEBUG)

    print('Client version: {0!s}'.format(client_version))

    api = login(username, password)

    res = api.friendships_create(userid)

    # todo: res 是否成功，成功则写入数据库


def unfollow(username, password, userid):
    logging.basicConfig()
    logger = logging.getLogger('instagram_private_api')
    logger.setLevel(logging.DEBUG)

    print('Client version: {0!s}'.format(client_version))

    api = login(username, password)

    res = api.friendships_destroy(userid)

    # todo: res 是否成功，成功则写入数据库


def login(username, password):
    device_id = None
    settings_file_path = 'settings/{0!s}.json'.format(username)
    try:

        settings_file = settings_file_path
        if not os.path.isfile(settings_file):
            # settings file does not exist
            print('Unable to find file: {0!s}'.format(settings_file))

            # login new
            api = Client(
                username, password,
                on_login=lambda x: onlogin_callback(x, settings_file_path))
        else:
            with open(settings_file) as file_data:
                cached_settings = json.load(file_data, object_hook=from_json)
            print('Reusing settings: {0!s}'.format(settings_file))

            device_id = cached_settings.get('device_id')
            # reuse auth settings
            api = Client(
                username, password,
                settings=cached_settings)

    except (ClientCookieExpiredError, ClientLoginRequiredError) as e:
        print('ClientCookieExpiredError/ClientLoginRequiredError: {0!s}'.format(e))

        # Login expired
        # Do relogin but use default ua, keys and such
        api = Client(
            username, password,
            device_id=device_id,
            on_login=lambda x: onlogin_callback(x, settings_file_path))

    except ClientLoginError as e:
        print('ClientLoginError {0!s}'.format(e))
        exit(9)
    except ClientError as e:
        print('ClientError {0!s} (Code: {1:d}, Response: {2!s})'.format(e.msg, e.code, e.error_response))
        exit(9)
    except Exception as e:
        print('Unexpected Exception: {0!s}'.format(e))
        exit(99)

    # Show when login expires
    cookie_expiry = api.cookie_jar.auth_expires
    print('Cookie Expiry: {0!s}'.format(datetime.datetime.fromtimestamp(cookie_expiry).strftime('%Y-%m-%dT%H:%M:%SZ')))

    return api


def get_follow_count(days, setting):
    if days == 0:
        print("第零天")
    elif days == 1:
        print("第一天")
    elif days == 2:
        print("第二天")
    elif days == 3:
        print("第三天")

