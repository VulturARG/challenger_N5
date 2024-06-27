from typing import Dict, List

from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.viewsets import ViewSet

from api.infrastructure.django.views.decorators.view_response_handler import (
    view_response_handler,
)
from api.infrastructure.wirings.infraction_wirirng import InfractionWiring


class LoadInfractionViewSet(ViewSet):
    permission_classes = []
    _infraction_use_case = InfractionWiring().instantiate()

    @action(methods=["POST"], detail=False)
    @view_response_handler()
    def generar_informe(self, request: Request, *args, **kwargs) -> List[Dict[str, str]]:
        """Show all infractions by email."""
        return self._infraction_use_case.list_by_email(payload=request.data)
