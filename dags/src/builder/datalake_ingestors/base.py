from abc import ABC, abstractmethod
from typing import Any


class BaseDataCollector(ABC):
    @abstractmethod
    def get_data_chunk(self) -> Any:
        ...


class BaseDatalakeDumper(ABC):
    @abstractmethod
    def store_data_chunk(self) -> None:
        ...
