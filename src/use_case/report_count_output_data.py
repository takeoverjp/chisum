from dataclasses import dataclass, field
from typing import List

from src.entity.count_entity import CountEntity


@dataclass(frozen=True)
class ReportCountOutputData:
    latest: List[CountEntity] = field(default_factory=list)
    one_old: List[CountEntity] = field(default_factory=list)
