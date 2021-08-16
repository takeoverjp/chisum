from abc import ABC, abstractmethod


class AbstractReportCountUseCase(ABC):
    @abstractmethod
    def handle(self):
        pass
