from dataclasses import dataclass, field
from datetime import datetime
from typing import List

from src.entity.count_entity import CountEntity


@dataclass(frozen=True)
class RecordCountInputData:
    timestamp: datetime
    counts: List[CountEntity] = field(default_factory=list)
