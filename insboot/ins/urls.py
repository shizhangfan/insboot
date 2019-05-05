from .api import AccountViewset, TagViewset, SettingViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register("ins/accounts", AccountViewset, base_name="insAccount")
router.register("ins/settings", SettingViewset, base_name="insSetting")
router.register("ins/tags", TagViewset, base_name="tag")

urlpatterns = router.urls
