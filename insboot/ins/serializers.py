from rest_framework import serializers
from .models import Account, Setting, Tag


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ("id", "email", "phone", "password", "status", "tag")


class SettingSerrializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = ("id", "name", "first_day", "second_day", "tag")


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "name")

