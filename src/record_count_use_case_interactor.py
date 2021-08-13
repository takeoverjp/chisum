from src.abstract_count_repository import AbstractCountRepository
from src.abstract_record_count_use_case import AbstractRecordCountUseCase
from src.record_count_input_data import RecordCountInputData


class RecordCountUseCaseInteractor(AbstractRecordCountUseCase):
    def __init__(self, repository: AbstractCountRepository):
        self.repository = repository

    def handle(self, input: RecordCountInputData):
        self.repository.save(input.counts)
