from enum import Enum


class TaskStatus(str, Enum):
    success = "SUCCESS"
    in_progress = "IN PROGRESS"
    scheduled = "SCHEDULED"
    failure = "FAILURE"

    def __str__(self) -> str:
        return self.value


class CloudProvider(str, Enum):
    aws = "AWS"
    gcp = "GCP"
