from typing import Dict

import yaml


class PipelineYmlParserException(BaseException):
    """Handles incorrectly formatted pipeline yml files"""


def read_yml(yml_path: str) -> Dict[str, str]:
    try:
        with open(yml_path) as yaml_file:
            yml = yaml.load(yaml_file, Loader=yaml.Loader)
        return yml

    except (yaml.parser.ParserError, yaml.scanner.ScannerError):
        raise PipelineYmlParserException(
            f"{yml_path} is incorrectly formatted yml file."
        )
