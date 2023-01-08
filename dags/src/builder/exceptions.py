class PipelineYmlParserException(Exception):
    """Handles incorrectly formatted pipeline yml files"""


class DagTaskConfigMissmatchException(Exception):
    """Handles inconsistency between dag and task configuration files"""
