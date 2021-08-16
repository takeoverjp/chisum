import unittest
from datetime import datetime
from test.support import captured_stdout

from src.entity.count_entity import CountEntity
from src.report_count_output_data import ReportCountOutputData
from src.report_count_presenter import ReportCountPresenter


class TestReportCountPresenter(unittest.TestCase):
    def setUp(self) -> None:
        one_old_date = datetime(2020, 1, 1)
        self.one_old = [CountEntity(one_old_date, "increase", 2),
                        CountEntity(one_old_date, "no_change", 2),
                        CountEntity(one_old_date, "decrease", 2),
                        CountEntity(one_old_date, "disappear", 2)]
        latest_date = datetime(2020, 1, 2)
        self.latest = [CountEntity(latest_date, "increase", 4),
                       CountEntity(latest_date, "no_change", 2),
                       CountEntity(latest_date, "decrease", 1),
                       CountEntity(latest_date, "appear", 2)]

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
        self.assertIn('0 (   +0) total', stdout.getvalue())

    def test_report_with_one_old(self):
        output = ReportCountOutputData(self.latest, self.one_old)

        # Execute
        presenter = ReportCountPresenter()
        with captured_stdout() as stdout:
            presenter.complete(output)

        # Assert
        self.assertIn('4 (   +2) increase', stdout.getvalue())
        self.assertIn('2 (   +0) no_change', stdout.getvalue())
        self.assertIn('1 (   -1) decrease', stdout.getvalue())
        self.assertIn('2 (   +2) appear', stdout.getvalue())
        self.assertIn('0 (   -2) disappear', stdout.getvalue())
        self.assertIn('9 (   +1) total', stdout.getvalue())

    def test_report_without_one_old(self):
        output = ReportCountOutputData(self.latest)

        # Execute
        presenter = ReportCountPresenter()
        with captured_stdout() as stdout:
            presenter.complete(output)

        # Assert
        self.assertIn('4 (   +4) increase', stdout.getvalue())
        self.assertIn('2 (   +2) no_change', stdout.getvalue())
        self.assertIn('1 (   +1) decrease', stdout.getvalue())
        self.assertIn('2 (   +2) appear', stdout.getvalue())
        self.assertIn('9 (   +9) total', stdout.getvalue())
        self.assertNotIn('disappear', stdout.getvalue())
