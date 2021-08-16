from .abstract_count_repository import AbstractCountRepository
from .abstract_report_count_presenter import AbstractReportCountPresenter
from .abstract_report_count_use_case import AbstractReportCountUseCase
from .report_count_output_data import ReportCountOutputData


class ReportCountUseCaseInteractor(AbstractReportCountUseCase):
    def __init__(self,
                 repository: AbstractCountRepository,
                 presenter: AbstractReportCountPresenter):
        self.repository = repository
        self.presenter = presenter

    def handle(self):
        timestamps = self.repository.get_timestamps(2)
        counts = list(
            map(lambda ts:
                self.repository.find_by_timestamp(ts),
                timestamps))
        output = ReportCountOutputData(counts[0], counts[1])
        self.presenter.complete(output)


AbstractReportCountUseCase.register(ReportCountUseCaseInteractor)
