from abc import ABC, abstractmethod


class BaseCloudService(ABC):
    # Object Storage
    @abstractmethod
    def save_from_memory_to_object_storage(self) -> None:
        ...

    @abstractmethod
    def save_from_file_to_object_storage(self) -> None:
        ...

    @abstractmethod
    def copy_to_internal_object_storage(self) -> None:
        ...
    
    @abstractmethod
    def delete_from_internal_object_storage(self) -> None:
        ...

    @abstractmethod
    def move_between_internal_object_storages(self) -> None:
        ...

    @abstractmethod
    def copy_to_external_object_storage(self) -> None:
        ...
    
    @abstractmethod
    def copy_from_external_object_storage(self) -> None:
        ...

    @abstractmethod
    def move_from_external_object_storage(self) -> None:
        ...

    @abstractmethod
    def delete_from_external_object_storage(self) -> None:
        ...