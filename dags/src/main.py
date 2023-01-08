PATH = (
    "/home/damian/Desktop/projects/airflow_builder/dags/src/configs/dags/dags_cfg.yml"
)

from pprint import pprint

from builder.builder import DagBuilder, DagBuilderConfig
from builder.enums import CloudProvider
from builder.extractors.api_extractor import APIExtractor

cfg = DagBuilderConfig(PATH)

# pprint(cfg.dag_instances)




z = APIExtractor("none", "https://api2.binance.com/api/v3/", CloudProvider.gcp)

z.auth()
z.extract("ticker/24hr", None)
z.move_to_stage()
