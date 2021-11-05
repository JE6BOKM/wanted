from rest_framework.routers import DefaultRouter

from apps.users.views import UserViewSet

app_name = "users"

router = DefaultRouter()
router.register(r"users", UserViewSet)


urlpatterns = router.urls
