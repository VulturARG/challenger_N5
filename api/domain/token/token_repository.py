from abc import ABC, abstractmethod
from typing import Dict

from api.domain.dtos.token_dto import TokenDTO


class TokenRepository(ABC):
    @abstractmethod
    def token(self, payload: Dict[str, str]) -> TokenDTO:
        """Repository to get a token."""
