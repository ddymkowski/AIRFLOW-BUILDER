PATH = (
    "/home/damian/Desktop/projects/airflow_builder/dags/src/configs/dags/dags_cfg.yml"
)

from pprint import pprint

from builder.builder import DagBuilder, DagBuilderConfig
from builder.enums import CloudProvider

cfg = DagBuilderConfig(PATH)

# pprint(cfg.dag_instances)

