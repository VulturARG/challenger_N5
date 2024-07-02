from dataclasses import dataclass, asdict

from api.domain.entities.base_entity import BaseEntity


@dataclass
class PersonEntity(BaseEntity):
    name: str
    email: str

    def to_dict(self):
        return asdict(self)
