
from src.builder.dag_builder import DagBuilderConfig, DagBuilder
from src.utils import read_yml
from pprint import pprint


AIRFLOW_HOME = ''
DAGS_CFG_YML = 'dags/src/configs/dags/dags_cfg.yml'

dags_cfg = DagBuilderConfig(DAGS_CFG_YML)

builder = DagBuilder(dags_cfg)

builder.create_dags()