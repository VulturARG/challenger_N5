from abc import ABC, abstractmethod
from typing import Dict, List

from api.domain.entities.infraction_entity import InfractionEntity


class InfractionRepository(ABC):
    @abstractmethod
    def create(self, payload: Dict[str, str]) -> InfractionEntity:
        """Repository to create an infraction on database."""

    @abstractmethod
    def list_by_email(self, payload: Dict[str, str]) -> List[InfractionEntity]:
        """Repository to list all infractions in database."""
