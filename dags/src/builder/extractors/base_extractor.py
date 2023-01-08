from abc import ABC, abstractmethod
from typing import Any, Optional

from builder.enums import CloudProvider


class BaseExtractor(ABC):
    @abstractmethod
    def auth(auth_url: str) -> Optional[str]:
        ...

    @abstractmethod
    def extract(base_url: str) -> Any:
        ...

    @abstractmethod
    def move_to_stage(provider: CloudProvider, location: str) -> None:
        ...
