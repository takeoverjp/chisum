from typing import List
from src.count_entity import CountEntity
from src.abstract_count_repository import AbstractCountRepository


class InMemoryCountRepository(AbstractCountRepository):
    counts: List[CountEntity]

    def __init__(self) -> None:
        self.counts = []

    def save(self, counts: List[CountEntity]):
        self.counts.extend(counts)

    def find_all(self) -> List[CountEntity]:
        return self.counts

    def find_by_timestamp(self, timestamp: int) -> List[CountEntity]:
        return list(filter(lambda count: count.timestamp == timestamp,
                           self.counts))


AbstractCountRepository.register(InMemoryCountRepository)
