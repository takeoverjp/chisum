from src.use_case.abstract_report_count_use_case import \
    AbstractReportCountUseCase


class ReportCountController:
    input_boundary: AbstractReportCountUseCase

    def __init__(self, input_boundary: AbstractReportCountUseCase):
        self.input_boundary = input_boundary

    def run(self):
        self.input_boundary.handle()
