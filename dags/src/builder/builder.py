import os
from pathlib import Path
from typing import Dict

import yaml

from builder.exceptions import (DagTaskConfigMissmatchException,
                                PipelineYmlParserException)


def read_yml(yml_path: str) -> Dict[str, str]:
    try:
        with open(yml_path) as yaml_file:
            yml = yaml.load(yaml_file, Loader=yaml.Loader)
        return yml

    except (yaml.parser.ParserError, yaml.scanner.ScannerError):
        raise PipelineYmlParserException(
            f"{yml_path} is incorrectly formatted yml file."
        )


class DagBuilderConfig:
    def __init__(self, dag_instances_cfg_path: str) -> None:
        self._dag_instances_cfg_path = Path(dag_instances_cfg_path)

        self._dag_instances = self._load_dag_instances()

        self._validate_dag_instances()

    @property
    def dag_instances(self) -> ...:
        return self._dag_instances

    def _load_dag_instances(self) -> Dict[str, str]:
        """
        Loads dags configuration file from dags/src/configs/dags.

        {
            "first_dag_name: {options},
            ...
         }
        """
        return read_yml(self._dag_instances_cfg_path)["dag_instances"]["options"]

    def _validate_dag_instances(self) -> None:
        """
        Validates whether for each entry in dags configuration there is tasks configuration file in dags/src/configs/tasks with name of dag_instance.
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

    def create_dag(self) -> ...:
        ...
