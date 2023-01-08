from abc import ABC, abstractmethod


class BaseLoader(ABC):
    @abstractmethod
    def load_from_stage_to_dwh() -> None:
        ...
