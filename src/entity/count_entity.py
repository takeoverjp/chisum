from datetime import datetime
from dataclasses import dataclass


@dataclass(frozen=True, eq=True)
class CountEntity:
    timestamp: datetime
    key: str
    value: int
