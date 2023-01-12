from .base import BaseDataCollector, BaseDatalakeDumper
from typing import Dict, Any
from .api_collector import BinanceApiExampleCollector


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

        return source_class_mapping[self._source_type](**self._storage_details)

    def get_data_dumper(self) -> BaseDatalakeDumper:
        ...
