from django.db import models


class Account(models.Model):
    STATUS_CHOICES = ((1, "VALID"), (2, "WARNED"), (3, "BANNED"))
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    status = models.IntegerField(choices=STATUS_CHOICES, null=True)
    tag = models.ForeignKey("Tag", on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)


class Setting(models.Model):
    name = models.CharField(max_length=50)
    first_day = models.IntegerField()
    second_day = models.IntegerField()
    tag = models.ForeignKey("Tag", on_delete=models.CASCADE)


class Tag(models.Model):
    name = models.CharField(max_length=50)


class Proxy(models.Model):
    name = models.CharField(max_length=100)
    ip = models.CharField(max_length=30)
    port = models.CharField(max_length=10)
    used_for_register = models.BooleanField(default=False, null=True)


class RegisterWorker(models.Model):
    working = models.BooleanField(default=False)
    times_per_proxy = models.IntegerField(default=0)


class FirstName(models.Model):
    text = models.CharField(max_length=100)


class LastName(models.Model):
    text = models.CharField(max_length=100)


class Target(models.Model):
    userId = models.CharField(max_length=300)
