from .abstract_count_repository import AbstractCountRepository
from .abstract_record_count_use_case import AbstractRecordCountUseCase
from .record_count_input_data import RecordCountInputData


class RecordCountUseCaseInteractor(AbstractRecordCountUseCase):
    def __init__(self, repository: AbstractCountRepository):
        self.repository = repository

    def handle(self, input: RecordCountInputData):
        # TODO: must be atomic
        self.repository.save(input.counts)
        self.repository.save_timestamps([input.timestamp])


AbstractRecordCountUseCase.register(RecordCountUseCaseInteractor)
