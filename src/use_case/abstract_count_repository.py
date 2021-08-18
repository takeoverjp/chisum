from abc import ABC, abstractmethod
from datetime import datetime
from typing import List

from src.entity.count_entity import CountEntity


class AbstractCountRepository(ABC):
    @abstractmethod
    def save(self, counts: List[CountEntity]):
        pass

    @abstractmethod
    def save_timestamps(self, timestamps: List[datetime]):
        pass

    @abstractmethod
    def find_all(self) -> List[CountEntity]:
        pass

    @abstractmethod
    def find_by_timestamp(self, timestamp: int) -> List[CountEntity]:
        pass

    @abstractmethod
    def get_timestamps(self, max_num: int) -> List[datetime]:
        pass
