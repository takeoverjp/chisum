import unittest
from datetime import datetime, timedelta, timezone

from src.interface_adapter.in_memory_count_repository import \
    InMemoryCountRepository
from src.interface_adapter.record_count_controller import RecordCountController
from src.use_case.record_count_use_case_interactor import \
    RecordCountUseCaseInteractor


class TestRecordCountController(unittest.TestCase):
    def setUp(self) -> None:
        self.repository = InMemoryCountRepository()
        self.interactor = RecordCountUseCaseInteractor(self.repository)
        return super().setUp()

    def test_create(self):
        # Execute
        RecordCountController(self.interactor)

    def test_record_once(self):
        controller = RecordCountController(self.interactor)

        # Execute
        controller.run("testdata/counts0.txt",
                       datetime(2020, 1, 1,
                                tzinfo=timezone.utc))

        # Assert
        counts = self.repository.find_all()
        self.assertEqual(len(counts), 9)

    def test_record_multi(self):
        controller = RecordCountController(self.interactor)
        time1 = datetime(2020, 1, 1, tzinfo=timezone.utc)
        time2 = time1 + timedelta(days=1)

        # Execute
        controller.run("testdata/counts0.txt", time1)
        controller.run("testdata/counts1.txt", time2)

        # Assert
        counts = self.repository.find_by_timestamp(time1)
        self.assertEqual(len(counts), 9)
        counts = self.repository.find_by_timestamp(time2)
        self.assertEqual(len(counts), 9)
        counts = self.repository.find_all()
        self.assertEqual(len(counts), 18)
