from src.abstract_count_repository import AbstractCountRepository
from src.abstract_report_count_use_case import AbstractReportCountUseCase


class ReportCountUseCaseInteractor(AbstractReportCountUseCase):
    def __init__(self, repository: AbstractCountRepository):
        self.repository = repository

    def handle(self):
        pass


AbstractReportCountUseCase.register(ReportCountUseCaseInteractor)
