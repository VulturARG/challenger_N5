from dataclasses import dataclass, asdict


@dataclass
class TokenDTO:
    access: str
    refresh: str

    def to_dict(self):
        return asdict(self)
