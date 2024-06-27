from typing import Dict, List

from api.domain.entities.infraction_entity import InfractionEntity
from api.domain.infraction.infraction_repository import InfractionRepository


class InfractionService:
    def __init__(self, infraction_repository: InfractionRepository):
        self._infraction_repository = infraction_repository

    def create(self, payload: Dict[str, str]) -> InfractionEntity:
        """Service to create an infraction on database."""
        return self._infraction_repository.create(payload=payload)

    def list_by_email(self, payload: Dict[str, str]) -> List[InfractionEntity]:
        """Service to list all infractions in database."""
        return self._infraction_repository.list_by_email(payload=payload)
