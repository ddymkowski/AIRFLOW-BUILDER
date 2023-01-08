from typing import Any, Dict

import requests
from pyparsing import Optional
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from builder.enums import CloudProvider
from builder.extractors.base_extractor import BaseExtractor


class APIExtractor(BaseExtractor):
    def __init__(
        self,
        auth_url: str,
        base_url: str,
        blob_storage_provider: CloudProvider,
        token: str = None,
    ) -> None:

        self.auth_url = auth_url
        self.base_url = base_url
        self.blob_storage_provider = blob_storage_provider

    def auth(self) -> None:
        self.token = super().auth()

    @staticmethod
    def _prepare_session() -> HTTPAdapter:
        retry_strategy = Retry(
            total=3,
            status_forcelist=[500, 401],
            method_whitelist=["GET"],
            backoff_factor=1,
        )

        return HTTPAdapter(max_retries=retry_strategy)

    @staticmethod
    def _handle_200(response: requests.Response):
        print("woo 200")
        print(response.text[:50])

    @staticmethod
    def _handle_not_200(response: requests.Response):
        print("woo nie 200 lipa")

    def extract(self, endpoint: str, payload: Dict[str, Any]) -> Any:

        request_url = self.base_url + endpoint
        adapter = self._prepare_session()

        with requests.Session() as s:
            if self.token:
                s.headers = {f"Authorization": f"Bearer {self.token}"}
            s.mount("https://", adapter)
            s.mount("http://", adapter)
            r = s.get(url=request_url, params=payload)

            if r.status_code == 200:
                self._handle_200(r)
            else:
                self._handle_not_200(r)

    def move_to_stage(self) -> None:
        print(f"moving to {self.blob_storage_provider} blob storage")
