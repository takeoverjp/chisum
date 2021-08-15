from abc import ABC
from abc import abstractmethod

from src.report_count_output_data import ReportCountOutputData


class AbstractReportCountPresenter(ABC):
    @abstractmethod
    def complete(self, output: ReportCountOutputData):
        pass
