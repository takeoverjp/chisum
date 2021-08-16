from abc import ABC, abstractmethod

from .report_count_output_data import ReportCountOutputData


class AbstractReportCountPresenter(ABC):
    @abstractmethod
    def complete(self, output: ReportCountOutputData):
        pass
