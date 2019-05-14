from celery.task import task
from .models import Account


@task
def print_hello():
    print("hello celery and django...")
    return "hello celery and django..."


@task
def follow_worker():
    # 获取所有账号

