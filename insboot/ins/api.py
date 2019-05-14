from rest_framework import viewsets, views, permissions
from rest_framework.response import Response
from .serializers import (
    AccountSerializer,
    TagSerializer,
    SettingSerrializer,
    ProxySerializer,
    RegisterWorkerSerializer,
)
from .models import Account, Tag, Setting, Proxy, RegisterWorker


class AccountViewset(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Account.objects.all()


class TagViewset(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Tag.objects.all()


class SettingViewset(viewsets.ModelViewSet):
    serializer_class = SettingSerrializer
    permission_classes = [permissions.AllowAny]
    queryset = Setting.objects.all()


class ProxyViewset(viewsets.ModelViewSet):
    serializer_class = ProxySerializer
    permission_classes = [permissions.AllowAny]
    queryset = Proxy.objects.all()


class RegisterSettingViewset(viewsets.ModelViewSet):
    serializer_class = RegisterWorkerSerializer
    permission_class = [permissions.AllowAny]
    queryset = RegisterWorker.objects.all()

    def create(self, request, *args, **kwargs):
        return Response({"error": "1111"})
