from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Optional

from api.domain.entities.base_entity import BaseEntity


@dataclass
class InfractionEntity(BaseEntity):
    vehicle_id: str
    timestamp: datetime
    comments: Optional[str] = None

    def to_dict(self):
        return asdict(self)
