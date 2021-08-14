import unittest

from src.in_memory_count_repository import InMemoryCountRepository
from src.report_count_use_case_interactor import ReportCountUseCaseInteractor


class TestReportCountUseCaseInteractor(unittest.TestCase):
    def setUp(self) -> None:
        self.repository = InMemoryCountRepository
        return super().setUp()

    def test_create(self):
        # Execute
        ReportCountUseCaseInteractor(self.repository)
