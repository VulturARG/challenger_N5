import logging
from typing import Any, Dict

from api.domain.exceptions.base_exceptions import ApiBaseException

logger = logging.getLogger(__name__)


class SerializerException(ApiBaseException):
    """Base class for all exceptions in this module."""


class SerializerError(SerializerException):
    MESSAGE = "Serializer error:"

    def __init__(self, error: Any) -> None:
        self._error = error

    def dict(self) -> Dict[str, str]:
        return {"error": f"{self.MESSAGE} {self._error}."}
