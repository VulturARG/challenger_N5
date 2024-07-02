from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Optional

from api.domain.entities.base_entity import BaseEntity
from api.domain.entities.vehicle_entity import VehicleEntity


@dataclass
class InfractionEntity(BaseEntity):
    vehicle: VehicleEntity
    timestamp: datetime
    comments: Optional[str] = None

    def to_dict(self):
        return {
            "placa_patente": self.vehicle.license_plate,
            "timestamp": self.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "comentarios": self.comments,
        }
