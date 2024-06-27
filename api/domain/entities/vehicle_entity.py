from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Optional

from api.domain.entities.base_entity import BaseEntity
from api.domain.entities.person_entity import PersonEntity


@dataclass
class VehicleEntity(BaseEntity):
    license_plate: str
    brand: str
    color: str
    person: PersonEntity

    def to_dict(self):
        return asdict(self)
