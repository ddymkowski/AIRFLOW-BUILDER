from pathlib import Path
from typing import Dict

from pydantic.error_wrappers import ValidationError

from src.builder.exceptions import (DagConfigValidationException,
                                DagTaskConfigMissmatchException,
                                YmlConfigException)
from src.builder.schemas import DAGConfig
from src.utils import read_yml
from airflow import DAG
from pprint import pprint

class DagBuilderConfig:
    def __init__(self, dag_instances_cfg_path: str) -> None:
        self._dag_instances_cfg_path = Path(dag_instances_cfg_path)
        self._dag_instances = self._load_dag_instances()

        self._validate_dag_instances()

    def __repr__(self) -> str:
        return '\n\n'.join([f'{key} -> {value}' for key, value in self.dag_instances.items()])

    @property
    def dag_instances(self) -> Dict[str, DAGConfig]:
        return self._dag_instances

    @property
    def dags_count(self) -> int:
        return len(self._dag_instances.keys())

    def _load_dag_instances(self) -> Dict[str, str]:
        """
        Loads dags configuration file from dags/src/configs/dags and parses it into pydantic dataclass.
        """
        try:
            raw_cfg = read_yml(self._dag_instances_cfg_path)["dag_instances"]["options"]
            return {
                cfg_name: DAGConfig(name=cfg_name, **cfg)
                for cfg_name, cfg in raw_cfg.items()
            }

        except KeyError:
            raise YmlConfigException(
                f'Given file {self._dag_instances_cfg_path} is missing one or both keys: "dag_instances", "options"'
            )

        except ValidationError as e:
            errors = "\n".join(
                [f"{error['loc']} -> {error['msg']}" for error in e.errors()]
            )
            raise DagConfigValidationException(
                f"Invalid data type in dag instances config:\n{errors}"
            )

    def _validate_dag_instances(self) -> None:
        """
        Validates whether for each entry in dag instance configurations there is tasks configuration in dags/src/configs/tasks with name of dag_instance.
        """
        task_files = [
            file.stem
            for file in Path(
                self._dag_instances_cfg_path.parent.parent / "tasks"
            ).iterdir()
        ]

        if sorted(self._dag_instances.keys()) != sorted(task_files):
            raise DagTaskConfigMissmatchException(
                f"Dag or task config is missing for: {(set(self._dag_instances.keys())) ^ set(task_files)}"
            )


class DagBuilder:
    def __init__(self, dags_config: DagBuilderConfig) -> None:
        self.dags_config = dags_config

    def create_dags(self):
        for dag_name, dag_cfg in self.dags_config.dag_instances.items():
            self._create_dag(dag_name, dag_cfg)
            break

    def _create_dag(self, dag_name: str, dag_cfg: DAGConfig) -> ...:
        tasks_details = read_yml(f'dags/src/configs/tasks/{dag_name}.yml')
        pprint(dag_cfg)
        print("**"*30)
        pprint(tasks_details)

        tasks = []



