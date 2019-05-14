from django.urls import include, path
from .api import (
    AccountViewset,
    TagViewset,
    SettingViewset,
    ProxyViewset,
    RegisterSettingViewset,
)
from .views import RegisterApi, print_hello
from rest_framework import routers


router = routers.DefaultRouter()
router.register("ins/accounts", AccountViewset, base_name="insAccount")
router.register("ins/settings", SettingViewset, base_name="insSetting")
router.register("ins/tags", TagViewset, base_name="tag")
router.register("ins/proxies", ProxyViewset, base_name="proxies")
router.register("ins/regsetting", RegisterSettingViewset, base_name="regsetting")

urlpatterns = [
    path("", include(router.urls)),
    path("ins/registers/", RegisterApi.as_view(), name="registers"),
    path("print_hello/", print_hello, name="registers"),
]
