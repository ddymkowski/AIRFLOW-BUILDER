from .base import BaseCloudService
from typing import Dict, Any, List


class GCPService(BaseCloudService):
    def __init__(self, project_name: str, region: str, auth: ...) -> None:
        self._project_name = project_name
        self._region = region
        self._auth = auth


    @property
    def project_name(self) -> str:
        return self._project_name

    @property
    def region(self) -> str:
        return self._region
        

    def save_from_memory_to_object_storage(
        self,
        data: bytes,
        project_name: str,
        bucket_name: str,
        **kwargs,
    ) -> None:
        ...

    def save_from_files_to_object_storage(
        self,
        file_name: List[str],
        project_name: str,
        bucket_name: str,
        **kwargs,
    ) -> None:
        ...

    def move_between_object_storages(
        self,
        files_to_move: List[str],
        source_project_name: str,
        source_bucket_name: str,
        target_project_name: str,
        target_bucket_name: str,
        **kwargs,
    ) -> None:
        ...

    def copy_to_internal_object_storage(self) -> None:
        ...
