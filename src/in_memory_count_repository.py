from datetime import datetime
from typing import List
from src.entity.count_entity import CountEntity
from src.abstract_count_repository import AbstractCountRepository


class InMemoryCountRepository(AbstractCountRepository):
    counts: List[CountEntity]

    def __init__(self) -> None:
        self.counts = []

    def save(self, counts: List[CountEntity]):
        self.counts.extend(counts)

    def find_all(self) -> List[CountEntity]:
        return self.counts

    def find_by_timestamp(self, timestamp: datetime) -> List[CountEntity]:
        return list(filter(lambda count: count.timestamp == timestamp,
                           self.counts))

    def get_timestamps(self, max_num: int) -> List[datetime]:
        return list(sorted(set(map(lambda count:
                               count.timestamp,
                               self.counts)), reverse=True))[0:max_num]


AbstractCountRepository.register(InMemoryCountRepository)
