from typing import Any, Dict

from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.viewsets import ViewSet

from api.infrastructure.django.serializers.officer_serializer import OfficerSerializer
from api.infrastructure.django.views.decorators.view_response_handler import (
    view_response_handler,
)
from api.infrastructure.wirings.officer_token_use_case_wiring import (
    OfficerTokenUseCaseWiring,
)


class OfficerViewSet(ViewSet):
    permission_classes = []
    _officer_use_case = OfficerTokenUseCaseWiring().instantiate()

    @extend_schema(
        request=OfficerSerializer,
        responses={200: OpenApiResponse(description="Success")},
    )
    @action(methods=["POST"], detail=False)
    @view_response_handler()
    def officer_token(self, request: Request, *args, **kwargs) -> Dict[str, Any]:
        """Get a token for an Officer."""
        return self._officer_use_case.token(payload=request.data)
