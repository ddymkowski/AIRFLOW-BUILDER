PATH = (
    "/home/damian/Desktop/projects/airflow_builder/dags/src/configs/dags/dags_cfg.yml"
)

from pprint import pprint

from builder.builder import DagBuilder, DagBuilderConfig
from builder.datalake_ingestors.api_collector import BinanceApiExampleCollector
from builder.enums import CloudProvider

cfg = DagBuilderConfig(PATH)

# pprint(cfg.dag_instances)




c = BinanceApiExampleCollector("https://api2.binance.com/")

print(c.gather_all_data("api/v3/ticker/24hr", None, None))
