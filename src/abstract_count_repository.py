from abc import ABC
from abc import abstractmethod
from typing import List
from src.count_entity import CountEntity


class AbstractCountRepository(ABC):
    @abstractmethod
    def save(self, counts: List[CountEntity]):
        pass

    @abstractmethod
    def find_all(self) -> List[CountEntity]:
        pass

    @abstractmethod
    def find_by_timestamp(self, timestamp: int) -> List[CountEntity]:
        pass
