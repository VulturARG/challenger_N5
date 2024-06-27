from typing import Any, Dict

from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.viewsets import ViewSet

from api.infrastructure.django.serializers.infraction_serializer import InfractionSerializer
from api.infrastructure.django.views.decorators.view_response_handler import (
    view_response_handler,
)
from api.infrastructure.wirings.infraction_wirirng import InfractionWiring


class CreateInfractionViewSet(ViewSet):
    permission_classes = [IsAuthenticated]
    _infraction_use_case = InfractionWiring().instantiate()

    @extend_schema(
        request=InfractionSerializer,
        responses={200: OpenApiResponse(description='Success')}
    )
    @action(methods=["POST"], detail=False)
    @view_response_handler()
    def cargar_infraccion(self, request: Request, *args, **kwargs) -> Dict[str, Any]:
        """Refreshes all Arma3 MODs in DB from disk."""
        return self._infraction_use_case.create(payload=request.data)
