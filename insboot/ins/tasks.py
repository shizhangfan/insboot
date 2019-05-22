from celery.task import task
from celery import Celery
from .models import Account, Target
from datetime import datetime, timedelta
import random


import json
import codecs
import datetime
import os.path
import logging
import argparse
try:
    from instagram_private_api import (
        Client, ClientError, ClientLoginError,
        ClientCookieExpiredError, ClientLoginRequiredError,
        __version__ as client_version)
except ImportError:
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from .ins_api import (
        Client, ClientError, ClientLoginError,
        ClientCookieExpiredError, ClientLoginRequiredError,
        __version__ as client_version)


@task
def print_hello():
    print("hello celery and django...")
    return "hello celery and django..."


@task
def follow_worker():
    # 获取所有账号
    accounts = Account.objects.all()
    # 获取账号之后，查看每个账号是否正在工作

    # 每个账号启动一个worker
    for account in accounts:
        single_account_follow_worker.delay(account)


@task
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

