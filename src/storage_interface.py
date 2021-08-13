from abc import ABC
from abc import abstractmethod
from typing import List
from src.entity import Entity


class StorageInterface(ABC):
    @abstractmethod
    def store(self, entity: Entity):
        pass

    @abstractmethod
    def load_all(self) -> List[Entity]:
        pass
