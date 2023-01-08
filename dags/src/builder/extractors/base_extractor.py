from abc import ABC, abstractmethod
from typing import Any, Optional


class BaseExtractor(ABC):
    @abstractmethod
    def auth() -> Optional[str]:
        ...

    @abstractmethod
    def extract() -> Any:
        ...

    @abstractmethod
    def move_to_stage() -> None:
        ...
