from abc import ABC, abstractmethod


class BaseTransformer(ABC):
    @abstractmethod
    def run_transformations() -> None:
        ...
