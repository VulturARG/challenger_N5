from api.application.officer_token_use_case import OfficerTokenUseCase
from api.domain.token.token_repository import TokenRepository
from api.domain.token.token_service import TokenService
from api.infrastructure.adapters.token_adapter import TokenAdapter
from api.infrastructure.django.models import Officer
from api.infrastructure.django.serializers.officer_serializer import OfficerSerializer


class OfficerTokenUseCaseWiring:
    def instantiate(self) -> OfficerTokenUseCase:
        return OfficerTokenUseCase(
            token_service=self._token_service,
        )

    @property
    def _token_service(self) -> TokenService:
        return TokenService(token_repository=self._token_repository)

    @property
    def _token_repository(self) -> TokenRepository:
        return TokenAdapter(
            officer_model=Officer,
            officer_serializer=OfficerSerializer,
        )
