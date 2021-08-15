import unittest
from datetime import datetime
from test.support import captured_stdout

from src.count_entity import CountEntity
from src.in_memory_count_repository import InMemoryCountRepository
from src.report_count_presenter import ReportCountPresenter
from src.report_count_use_case_interactor import ReportCountUseCaseInteractor


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
        self.assertIn('Total: 9(+1)', stdout.getvalue())
