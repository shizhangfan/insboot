from rest_framework import viewsets, permissions
from .serializers import AccountSerializer, TagSerializer, SettingSerrializer
from .models import Account, Tag, Setting


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

