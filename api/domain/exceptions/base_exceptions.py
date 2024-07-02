import logging
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)


class ApiBaseException(Exception):
    """Base class for all own exceptions."""

    MESSAGE: Optional[str] = None

    def dict(self) -> Dict[str, str]:
        """Return error message as dict"""

        default_message = f"The '{self.__class__.__name__}' base class should not be used to raise exceptions."
        message = self.MESSAGE if self.MESSAGE is not None else default_message
        return {"error": message}


class ApiBaseGenericError(ApiBaseException):
    def __init__(
        self,
        exception_or_message: Any,
    ) -> None:
        super().__init__()

        msg = (
            type(exception_or_message)
            if isinstance(exception_or_message, Exception)
            and not isinstance(exception_or_message, ApiBaseException)
            else exception_or_message
        )
        self._exception_or_message = str(msg)
        logger.error(f"ERROR: Generic error: {self._exception_or_message}.")

    def dict(self):
        return {"generic error": self._exception_or_message}


class ApiBaseWarning(ApiBaseException):
    """Base class for all own warnings."""


class ApiBaseNotAuthorized(ApiBaseException):
    """Base class for all Not Authorized exceptions."""


class ApiBaseNotFound(ApiBaseException):
    """Base class for all Not Found exceptions."""
