from django.db import models


class Account(models.Model):
    STATUS_CHOICES = ((1, "VALID"), (2, "WARNED"), (3, "BANNED"))
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    status = models.IntegerField(choices=STATUS_CHOICES, null=True)
    tag = models.ForeignKey("Tag", on_delete=models.CASCADE)


class Setting(models.Model):
    name = models.CharField(max_length=50)
    first_day = models.IntegerField()
    second_day = models.IntegerField()
    tag = models.ForeignKey("Tag", on_delete=models.CASCADE)


class Tag(models.Model):
    name = models.CharField(max_length=50)
