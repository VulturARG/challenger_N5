from typing import Dict

from api.domain.exceptions.base_exceptions import ApiBaseNotFound


class ModelException(ApiBaseNotFound):
    """Base class for all exceptions in this module."""


class ModelNotExistError(ModelException):
    MESSAGE = "does not exist."

    def __init__(self, model: str) -> None:
        self._model = model.capitalize()

    def dict(self) -> Dict[str, str]:
        return {"error": f"{self._model} {self.MESSAGE}"}
