import logging
import sys
import traceback
from typing import Optional

from api.domain.exceptions.base_exceptions import (
    ApiBaseException,
    ApiBaseWarning,
    ApiBaseGenericError,
    ApiBaseNotAuthorized,
    ApiBaseNotFound,
)

logger = logging.getLogger(__name__)


base_exception = ApiBaseException
warning = ApiBaseWarning
general_exception = ApiBaseGenericError
not_authorized = ApiBaseNotAuthorized
not_found = ApiBaseNotFound


def generic_error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            class_name = args[0].__class__.__name__
        except IndexError:
            class_name = None
        method_name = func.__name__
        try:
            return func(*args, **kwargs)
        except (warning, not_authorized, not_found) as exc:
            raise exc
        except base_exception as exc:
            logger_error_details(
                exc=exc, method_name=method_name, class_name=class_name
            )
            message = exc.dict().get("error", "No error message received")
            logger.error("ERROR MESSAGE: %s", message)
            raise exc
        except Exception as exc:
            logger_error_details(
                exc=exc, method_name=method_name, class_name=class_name
            )
            logger.error("ERROR TYPE: %s.", type(exc))
            logger.error("ERROR RAW: %s", exc)
            raise general_exception(exc) from exc

    return wrapper


def logger_error_details(
    exc: Exception, method_name: str, class_name: Optional[str]
) -> None:
    tb = traceback.extract_tb(sys.exc_info()[2])
    _, line_number, _, _ = tb[-1]

    if class_name is None:
        logger.error(
            "ERROR: '%s' exception was raised in line %s in '%s' function/method.",
            exc.__class__.__name__,
            line_number,
            method_name,
        )
        return None

    logger.error(
        "ERROR: '%s' exception was raised in line %s in '%s' method of the '%s' class.",
        exc.__class__.__name__,
        line_number,
        method_name,
        class_name,
    )
