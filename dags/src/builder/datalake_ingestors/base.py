from abc import ABC, abstractmethod


class BaseDatalakeIngestor(ABC):

    @abstractmethod
    def get_source_data(self) -> ...:
        ...

    @abstractmethod
    def ingest_to_datalake(self) -> None:
        ...

    @abstractmethod
    def log_ingestion(self) -> None:
        ...
