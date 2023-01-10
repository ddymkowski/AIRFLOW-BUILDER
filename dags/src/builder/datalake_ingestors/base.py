from abc import ABC, abstractmethod


class BaseDataCollector(ABC):
    @abstractmethod
    def gather_all_data(self) -> ...:
        ...


class BaseDatalakeDumper(ABC):
    @abstractmethod
    def store_data(self) -> None:
        ...


class DatalalakeIngestorFactory(ABC):
    @abstractmethod
    def get_data_collector(self) -> BaseDataCollector:
        ...

    @abstractmethod
    def get_data_dumper(self) -> BaseDatalakeDumper:
        ...
