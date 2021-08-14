from abc import ABC
from abc import abstractmethod

from src.record_count_input_data import RecordCountInputData


class AbstractRecordCountUseCase(ABC):
    @abstractmethod
    def handle(self, input: RecordCountInputData):
        pass
