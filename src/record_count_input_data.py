from typing import List
from dataclasses import dataclass, field
from src.entity.count_entity import CountEntity


@dataclass(frozen=True)
class RecordCountInputData:
    counts: List[CountEntity] = field(default_factory=list)
