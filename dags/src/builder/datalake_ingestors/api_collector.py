from .base import BaseDataCollector, BaseDatalakeDumper
from typing import Literal, Optional, Dict, Any
from abc import abstractmethod

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class BaseApiDataCollector(BaseDataCollector):
    def __init__(
        self,
        base_url: str,
        auth_url: str = None,
        authorization_method: Literal["Bearer", "Credentials"] = None,
        data_dumper: BaseDatalakeDumper = None # In case we want to store data every request somewhere else than ram

    ) -> None:
        self._base_url = base_url
        self._auth_url = auth_url
        self._authorization_method = authorization_method
        self._data_dumper = data_dumper

    
    @abstractmethod
    def get_token(self) -> Optional[str]:
        ...

    @abstractmethod
    def gather_all_data(self) -> ...:
        ...

    @abstractmethod
    def _handle_200(self, response: requests.Response) -> ...:
        ...
    
    @abstractmethod
    def _handle_not_200(self, response: requests.Response) -> ...:
        ...
    


EndpointsParams = Dict[str, Dict[str, Any]]

class BinanceApiExampleCollector(BaseApiDataCollector):
    def __init__(self, base_url: str, auth_url: str = None, authorization_method: Literal["Bearer", "Credentials"] = None,data_dumper: BaseDatalakeDumper = None,) -> None:
        super().__init__(base_url, auth_url, authorization_method, data_dumper)

    @staticmethod
    def _prepare_session() -> HTTPAdapter:
        retry_strategy = Retry(
            total=3,
            status_forcelist=[500, 401],
            method_whitelist=["GET"],
            backoff_factor=1,
        )

        return HTTPAdapter(max_retries=retry_strategy)

    def get_token(self) -> str:
        return


    def request_data(self, session: requests.Session, endpoint: str, params: Dict[str, Any]) -> ...:
        request_url = self._base_url + endpoint
        return session.get(url=request_url, params=params)
    

    def _handle_200(self, response: requests.Response) -> ...:
        print('200')
        return response.text[:100]

    def _handle_not_200(self, response: requests.Response) -> ...:
        print(response.status_code)
        return

    def gather_all_data(self, endpoint: str, params: Dict[str, Any], headers: Dict[str, Any]) -> ...:
        adapter = self._prepare_session()

        with requests.Session() as s:
            if headers:
                s.headers = headers
            s.mount("https://", adapter)
            s.mount("http://", adapter)

            r = self.request_data(s,endpoint, params)

            if r.status_code == 200:
                data = self._handle_200(r)
                return data

            else:
                self._handle_not_200(r)
                



        
        