from typing import Any, Dict, List
from google.cloud import storage
from .base import BaseCloudObjectStorageService


class GCSService(BaseCloudObjectStorageService):
    def __init__(
        self,
        project_name: str,
        region: str,
        service_account_credentials: Dict[str, str],
    ) -> None:
        self._project_name = project_name
        self._region = region
        self._service_account_credentials = service_account_credentials

    @property
    def project_name(self) -> str:
        return self._project_name

    @property
    def region(self) -> str:
        return self._region

    @staticmethod
    def _get_blob(project_name: str, bucket_name:str, blob_path: str,) -> 'Blob':
    
        storage_client = storage.Client(project=project_name)
        bucket = storage_client.bucket(bucket_name)
        return bucket.blob(blob_path)

    def save_from_memory_to_object_storage(
        self,
        data: bytes,
        project_name: str,
        bucket_name: str,
        prefix: str,
        filename: str,
        **kwargs,
    ) -> None:

        gcs_file = bucket_name + prefix + filename
        blob = self._get_blob(project_name, bucket_name, gcs_file)
        blob.upload_from_string(data)

    def save_file_to_object_storage(
        self,
        file_name: List[str],
        project_name: str,
        bucket_name: str,
        **kwargs,
    ) -> None:
        ...

    def copy_to_internal_object_storage(
        self,
        files_to_copy: List[str],
        source_project_name: str,
        source_bucket_name: str,
        target_project_name: str,
        target_bucket_name: str,
        **kwargs,
    ) -> None:
        ...

    def delete_from_internal_object_storage(
        self,
        files_to_delete: List[str],
        source_project_name: str,
        source_bucket_name: str,
        target_project_name: str,
        target_bucket_name: str,
        **kwargs,
    ) -> None:
        ...

    def move_to_internal_object_storage(
        self,
        files_to_move: List[str],
        source_project_name: str,
        source_bucket_name: str,
        target_project_name: str,
        target_bucket_name: str,
        **kwargs,
    ) -> None:
        ...

    # probably I do not need external methods as I could just use other cloud module maybe for smaller clouds not covered with interfaces
    def copy_to_external_object_storage(
        self,
        files_to_move: List[str],
        source_project_name: str,
        source_bucket_name: str,
        target_service_provider: str,
        target_details: Dict[str, Any],
        **kwargs,
    ) -> None:
        ...

    def copy_from_external_object_storage(self) -> None:
        ...

    def move_from_external_object_storage(self) -> None:
        ...

    def delete_from_external_object_storage(self) -> None:
        ...
