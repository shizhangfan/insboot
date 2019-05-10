from rest_framework import serializers
from .models import Account, Setting, Tag, Proxy


class AccountSerializer(serializers.ModelSerializer):
    tag_name = serializers.CharField(source="tag.name")

    class Meta:
        model = Account
        fields = ("id", "email", "phone", "password", "status", "tag_name")


class SettingSerrializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = ("id", "name", "first_day", "second_day", "tag")


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "name")


class ProxySerializer(serializers.ModelSerializer):
    class Meta:
        model = Proxy
        fields = ("id", "name", "ip", "port")

