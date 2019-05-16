from celery.task import task
from celery import Celery
from .models import Account, Target
from datetime import datetime, timedelta
import random


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


def get_follow_count(days, setting):
    if days == 0:
        print("第零天")
    elif days == 1:
        print("第一天")
    elif days == 2:
        print("第二天")
    elif days == 3:
        print("第三天")

