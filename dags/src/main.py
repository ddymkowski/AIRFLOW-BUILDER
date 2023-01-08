PATH = (
    "/home/damian/Desktop/projects/airflow_builder/dags/src/configs/dags/dags_cfg.yml"
)

from builder.builder import DagBuilder, DagBuilderConfig

cfg = DagBuilderConfig(PATH)

z = DagBuilder(cfg)
