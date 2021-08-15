from src.report_count_controller import ReportCountController
import unittest

from src.in_memory_count_repository import InMemoryCountRepository
from src.record_count_use_case_interactor import RecordCountUseCaseInteractor


class TestRecordCountController(unittest.TestCase):
    def setUp(self) -> None:
        self.repository = InMemoryCountRepository()
        self.interactor = RecordCountUseCaseInteractor(self.repository)
        return super().setUp()

    def test_create(self):
        # Execute
        ReportCountController(self.interactor)
