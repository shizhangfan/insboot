from rest_framework import serializers
from .models import Account, Setting, Tag, Proxy, FirstName, LastName, RegisterWorker


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ("id", "email", "phone", "password", "status")


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


class FirstNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstName
        fields = ("id", "text")


class LastNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = LastName
        fields = ("id", "text")


class RegisterWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterWorker
        fields = ("id", "working", "times_per_proxy")
