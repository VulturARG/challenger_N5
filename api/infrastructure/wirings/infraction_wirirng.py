from api.application.infraction_use_case import InfractionUseCase
from api.domain.infraction.infraction_repository import InfractionRepository
from api.domain.infraction.infraction_service import InfractionService
from api.infrastructure.adapters.infraction_adapter import InfractionAdapter
from api.infrastructure.django.models import Vehicle, Person
from api.infrastructure.django.models.infraction import Infraction
from api.infrastructure.django.serializers.email_serializer import EmailSerializer
from api.infrastructure.django.serializers.infraction_serializer import (
    InfractionSerializer,
)


class InfractionWiring:
    def instantiate(self) -> InfractionUseCase:
        return InfractionUseCase(
            infraction_service=self._infraction_service,
        )

    @property
    def _infraction_service(self) -> InfractionService:
        return InfractionService(
            infraction_repository=self._infraction_repository,
        )

    @property
    def _infraction_repository(self) -> InfractionRepository:
        return InfractionAdapter(
            vehicle_model=Vehicle,
            infraction_model=Infraction,
            person_model=Person,
            infraction_serializer=InfractionSerializer,
            email_serializer=EmailSerializer,
        )
