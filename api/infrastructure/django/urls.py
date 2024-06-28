from rest_framework.routers import DefaultRouter

from api.infrastructure.django.views.create_infraction_viewset import (
    CreateInfractionViewSet,
)
from api.infrastructure.django.views.list_infraction_viewset import (
    ListInfractionViewSet,
)
from api.infrastructure.django.views.officer_viewset import OfficerViewSet

router = DefaultRouter(trailing_slash=True)

router.register(
    prefix="", viewset=CreateInfractionViewSet, basename="create-infraction"
)
router.register(prefix="", viewset=ListInfractionViewSet, basename="list-infraction")
router.register(prefix="", viewset=OfficerViewSet, basename="token")

urlpatterns = router.urls
