# Generated by Django 2.2.1 on 2019-05-27 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ins', '0005_auto_20190527_1413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='tag',
        ),
    ]