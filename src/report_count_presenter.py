from typing import List
from functools import reduce

from src.abstract_report_count_presenter import AbstractReportCountPresenter
from src.count_entity import CountEntity
from src.report_count_output_data import ReportCountOutputData


class ReportCountPresenter(AbstractReportCountPresenter):
    @classmethod
    def _accumulate(cls, counts: List[CountEntity]):
        return reduce(lambda a, b: a + b.value, counts, 0)

    def complete(self, output: ReportCountOutputData):
        one_old_total = ReportCountPresenter._accumulate(output.one_old)
        latest_total = ReportCountPresenter._accumulate(output.latest)
        diff = latest_total - one_old_total
        if diff == 0:
            diff_str = '-'
        elif diff > 0:
            diff_str = f'+{diff}'
        else:
            diff_str = str(diff)
        total_line = f'Total: {latest_total}({diff_str})'
        print(total_line)


AbstractReportCountPresenter.register(ReportCountPresenter)
