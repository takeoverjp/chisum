from src.count_entity import CountEntity
import unittest
from datetime import datetime
from test.support import captured_stdout

from src.report_count_output_data import ReportCountOutputData
from src.report_count_presenter import ReportCountPresenter


class TestReportCountPresenter(unittest.TestCase):
    def setUp(self) -> None:
        one_old_date = datetime(2020, 1, 1)
        self.one_old = [CountEntity(one_old_date, "key1", 1),
                        CountEntity(one_old_date, "key2", 2),
                        CountEntity(one_old_date, "key3", 3)]
        latest_date = datetime(2020, 1, 2)
        self.latest = [CountEntity(latest_date, "key1", 1),
                       CountEntity(latest_date, "key2", 2),
                       CountEntity(latest_date, "key3", 4)]

        return super().setUp()

    def test_create(self):
        # Execute
        presenter = ReportCountPresenter()

        self.assertIsNotNone(presenter)

    def test_report_empty(self):
        output = ReportCountOutputData()

        # Execute
        presenter = ReportCountPresenter()
        with captured_stdout() as stdout:
            presenter.complete(output)

        # Assert
        self.assertIn('Total: 0(-)', stdout.getvalue())

    def test_report_with_one_old(self):
        output = ReportCountOutputData(self.latest, self.one_old)

        # Execute
        presenter = ReportCountPresenter()
        with captured_stdout() as stdout:
            presenter.complete(output)

        # Assert
        self.assertIn('Total: 7(+1)', stdout.getvalue())

    def test_report_without_one_old(self):
        output = ReportCountOutputData(self.latest)

        # Execute
        presenter = ReportCountPresenter()
        with captured_stdout() as stdout:
            presenter.complete(output)

        # Assert
        self.assertIn('Total: 7(+7)', stdout.getvalue())