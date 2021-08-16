import unittest

from src.interface_adapter.in_memory_count_repository import \
    InMemoryCountRepository
from src.interface_adapter.report_count_controller import ReportCountController
from src.use_case.record_count_use_case_interactor import \
    RecordCountUseCaseInteractor


class TestRecordCountController(unittest.TestCase):
    def setUp(self) -> None:
        self.repository = InMemoryCountRepository()
        self.interactor = RecordCountUseCaseInteractor(self.repository)
        return super().setUp()

    def test_create(self):
        # Execute
        ReportCountController(self.interactor)
