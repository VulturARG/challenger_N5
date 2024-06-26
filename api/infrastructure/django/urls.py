from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=True)

# router.register(prefix="", viewset=AliveViewSet, basename="alive")

urlpatterns = router.urls
