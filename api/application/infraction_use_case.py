from typing import Dict, List

from api.domain.entities.infraction_entity import InfractionEntity
from api.domain.exceptions.decorators.generic_error_handler import generic_error_handler
from api.domain.infraction.infraction_service import InfractionService


class InfractionUseCase:
    def __init__(self, infraction_service: InfractionService) -> None:
        self._infraction_service = infraction_service

    @generic_error_handler
    def create(self, payload: Dict[str, str]) -> Dict[str, str]:
        """Use case: create an infraction on database."""
        infraction = self._infraction_service.create(payload=payload)
        return infraction.to_dict()

    @generic_error_handler
    def list_by_email(self, payload: Dict[str, str]) -> List[Dict[str, str]] or str:
        """Use case: list all infractions in database."""
        infractions = self._infraction_service.list_by_email(payload=payload)
        if not infractions:
            return "No registra infracciones"
        return [infraction.to_dict() for infraction in infractions]
