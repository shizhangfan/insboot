from celery.task import task


@task
def print_hello():
    return "hello celery and django..."

