from typing import Dict

from api.domain.token.token_service import TokenService


class OfficerTokenUseCase:
    def __init__(self, token_service: TokenService):
        self._token_service = token_service

    def token(self, payload: Dict[str, str]) -> Dict[str, str]:
        officer_token = self._token_service.token(payload=payload)
        return officer_token.to_dict()
