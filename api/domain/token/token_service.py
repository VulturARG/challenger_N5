from typing import Dict

from api.domain.dtos.token_dto import TokenDTO
from api.domain.token.token_repository import TokenRepository


class TokenService:
    def __init__(self, token_repository: TokenRepository):
        self._token_repository = token_repository

    def token(self, payload: Dict[str, str]) -> TokenDTO:
        """Service to get an Officer token."""
        return self._token_repository.token(payload=payload)
