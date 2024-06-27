from typing import Dict, List

from django.db import transaction

from api.domain.entities.infraction_entity import InfractionEntity
from api.domain.exceptions.decorators.generic_error_handler import generic_error_handler
from api.domain.exceptions.model_exceptions import ModelNotExistError
from api.domain.exceptions.serializer_exceptions import SerializerError
from api.domain.infraction.infraction_repository import InfractionRepository
from api.infrastructure.django.models import Vehicle, Person
from api.infrastructure.django.models.infraction import Infraction
from api.infrastructure.django.serializers.email_serializer import EmailSerializer
from api.infrastructure.django.serializers.infraction_serializer import (
    InfractionSerializer,
)


class InfractionAdapter(InfractionRepository):
    def __init__(
        self,
        vehicle_model: type(Vehicle),
        infraction_model: type(Infraction),
        person_model: type(Person),
        infraction_serializer: type(InfractionSerializer),
        email_serializer: type(EmailSerializer),
    ):
        self._vehicle = vehicle_model
        self._infraction = infraction_model
        self._person = person_model
        self._infraction_serializer = infraction_serializer
        self._email_serializer = email_serializer

    @generic_error_handler
    @transaction.atomic
    def create(self, payload: Dict[str, str]) -> InfractionEntity:
        """Adapter to create an infraction on database."""
        serializer = self._infraction_serializer(data=payload)
        if not serializer.is_valid():
            raise SerializerError(serializer.errors)

        try:
            vehicle = self._vehicle.objects.select_for_update().get(
                license_plate=payload["placa_patente"]
            )
        except self._vehicle.DoesNotExist:
            raise ModelNotExistError(model=self._vehicle._meta.verbose_name)

        infraction = self._infraction.objects.create(
            vehicle=vehicle,
            timestamp=serializer.validated_data["timestamp"],
            comments=serializer.validated_data["comentarios"],
        )
        return infraction.to_entity()

    @generic_error_handler
    def list_by_email(self, payload: Dict[str, str]) -> List[InfractionEntity]:
        """Adapter to list all infractions in database."""
        email_serializer = self._email_serializer(data=payload)
        if not email_serializer.is_valid():
            raise SerializerError(email_serializer.errors)
        email = email_serializer.validated_data["email"]

        try:
            person = self._person.objects.get(email=email)
        except self._person.DoesNotExist:
            raise ModelNotExistError(model=self._person._meta.verbose_name)

        infractions = self._infraction.objects.filter(
            vehicle__person=person
        ).select_related("vehicle")
        return [infraction.to_entity() for infraction in infractions]
