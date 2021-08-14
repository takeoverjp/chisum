from abc import ABC
from abc import abstractmethod


class AbstractReportCountUseCase(ABC):
    @abstractmethod
    def handle(self):
        pass
