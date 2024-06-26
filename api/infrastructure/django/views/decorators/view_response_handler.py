from functools import wraps

from rest_framework import status
from rest_framework.response import Response

from api.domain.execptions.base_exceptions import (
    ApiBaseException,
    ApiBaseWarning,
    ApiBaseGenericError,
    ApiBaseNotAuthorized,
    ApiBaseNotFound,
)

base_exception = ApiBaseException
warning = ApiBaseWarning
general_exception = ApiBaseGenericError
not_authorized = ApiBaseNotAuthorized
not_found = ApiBaseNotFound


def view_response_handler(
    success_status=status.HTTP_200_OK,
    generic_error_status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    global_status=status.HTTP_400_BAD_REQUEST,
    warning_status=status.HTTP_202_ACCEPTED,
    not_authorized_status=status.HTTP_401_UNAUTHORIZED,
    not_found_status=status.HTTP_404_NOT_FOUND,
):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                response = func(*args, **kwargs)
                return Response(response, status=success_status)
            except warning as error:
                return Response(error.dict(), status=warning_status)
            except not_authorized as error:
                return Response(error.dict(), status=not_authorized_status)
            except not_found as error:
                return Response(error.dict(), status=not_found_status)
            except general_exception as error:
                return Response(error.dict(), status=generic_error_status)
            except base_exception as error:
                return Response(error.dict(), status=global_status)
            except Exception as error:
                return Response(str(error), status=global_status)

        return wrapper

    return decorator
