from typing import Any, Dict

from ..cloud_services.aws import S3Service
from ..cloud_services.gcp import GCSService
from .api_collector import BinanceApiExampleCollector
from .base import BaseDataCollector, BaseDatalakeDumper


class DatalalakeIngestor:
    def __init__(
        self,
        source_type: str,
        source_details: Dict[str, Any],
        storage_type: str,
        storage_details: Dict[str, Any],
    ) -> None:
        self._source_type = source_type
        self._source_details = source_details
        self._storage_type = storage_type
        self._storage_details = storage_details

    def get_data_collector(self) -> BaseDataCollector:

        source_class_mapping = {
            "binance_api": BinanceApiExampleCollector,
        }  # to be moved to some constants file

        return source_class_mapping[self._source_type](**self._source_details)

    def get_data_dumper(self) -> BaseDatalakeDumper:
        target_class_maping = {"gcs": GCSService, "aws": S3Service}

        return target_class_maping[self._storage_type](**self._storage_details)

    # TODO fix this abomination probably should be different class/func
    def ingest(self):
        collector = self.get_data_collector()
        dumper = self.get_data_dumper()

        while True:
            data = collector.get_data_chunk()
            if not data:
                break
            dumper.store_data_chunk(data)
