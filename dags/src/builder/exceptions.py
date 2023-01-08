class YmlConfigException(Exception):
    """Handles incorrectly formatted config yml files"""


class DagTaskConfigMissmatchException(Exception):
    """Handles inconsistency between dag and task configuration files"""


class DagConfigValidationException(Exception):
    """Handles type checking errors for dag instances configs"""
