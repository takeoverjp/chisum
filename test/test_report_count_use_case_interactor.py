import unittest
from datetime import datetime
from test.support import captured_stdout

from src.entity.count_entity import CountEntity
from src.interface_adapter.in_memory_count_repository import \
    InMemoryCountRepository
from src.interface_adapter.report_count_presenter import ReportCountPresenter
from src.use_case.report_count_use_case_interactor import \
    ReportCountUseCaseInteractor


class TestReportCountUseCaseInteractor(unittest.TestCase):
    def setUp(self) -> None:
        self.repository = InMemoryCountRepository()
        self.presenter = ReportCountPresenter()

        dates = [datetime(2020, 1, 1), datetime(2020, 1, 2)]
        counts = [CountEntity(dates[0], "increase", 2),
                  CountEntity(dates[0], "no_change", 2),
                  CountEntity(dates[0], "decrease", 2),
                  CountEntity(dates[0], "disappear", 2),
                  CountEntity(dates[1], "increase", 4),
                  CountEntity(dates[1], "no_change", 2),
                  CountEntity(dates[1], "decrease", 1),
                  CountEntity(dates[1], "appear", 2)]
        self.repository.save_timestamps(dates)
        self.repository.save(counts)

        return super().setUp()

    def test_create(self):
        # Execute
        ReportCountUseCaseInteractor(self.repository, self.presenter)

#    @unittest.skip('after InMemoryRepository.get_timestamps')
    def test_handle(self):
        # Execute
        interactor = ReportCountUseCaseInteractor(
            self.repository, self.presenter)
        with captured_stdout() as stdout:
            interactor.handle()

        # Assert
        self.assertIn('4 (   +2) increase', stdout.getvalue())
        self.assertIn('2 (   +0) no_change', stdout.getvalue())
        self.assertIn('1 (   -1) decrease', stdout.getvalue())
        self.assertIn('2 (   +2) appear', stdout.getvalue())
        self.assertIn('0 (   -2) disappear', stdout.getvalue())
        self.assertIn('9 (   +1) TOTAL', stdout.getvalue())
