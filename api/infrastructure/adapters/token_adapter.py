from typing import Dict

from rest_framework_simplejwt.tokens import RefreshToken

from api.domain.dtos.token_dto import TokenDTO
from api.domain.exceptions.decorators.generic_error_handler import generic_error_handler
from api.domain.exceptions.model_exceptions import ModelNotExistError
from api.domain.exceptions.serializer_exceptions import SerializerError
from api.domain.token.token_repository import TokenRepository
from api.infrastructure.django.models import Officer
from api.infrastructure.django.serializers.officer_serializer import OfficerSerializer


class TokenAdapter(TokenRepository):
    def __init__(
        self, officer_model: type(Officer), officer_serializer: type(OfficerSerializer)
    ):
        self._officer_model = officer_model
        self._officer_serializer = officer_serializer

    @generic_error_handler
    def token(self, payload: Dict[str, str]) -> TokenDTO:
        """Adapter to get an officer token."""
        serializer = self._officer_serializer(data=payload)
        if not serializer.is_valid():
            raise SerializerError(serializer.errors)

        try:
            officer = self._officer_model.objects.get(
                name=payload["name"], unique_id=payload["unique_id"]
            )
        except self._officer_model.DoesNotExist:
            raise ModelNotExistError(model=self._officer_model._meta.verbose_name)

        refresh = RefreshToken.for_user(officer)
        return TokenDTO(access=str(refresh.access_token), refresh=str(refresh))
