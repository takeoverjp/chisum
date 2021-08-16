from abc import ABC, abstractmethod

from .record_count_input_data import RecordCountInputData


class AbstractRecordCountUseCase(ABC):
    @abstractmethod
    def handle(self, input: RecordCountInputData):
        pass
