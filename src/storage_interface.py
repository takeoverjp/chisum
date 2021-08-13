from abc import ABC
from abc import abstractmethod
from typing import List
from src.count_entity import CountEntity


class StorageInterface(ABC):
    @abstractmethod
    def store(self, count: CountEntity):
        pass

    @abstractmethod
    def load_all(self) -> List[CountEntity]:
        pass
