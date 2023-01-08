from typing import Optional

from pydantic import BaseModel


class DAGConfig(BaseModel):
    name: str
    description: Optional[str] = "No description"
    schedule: str
    start_date: str
    end_date: str
    timezone: Optional[str] = "UTC"


class BaseTask(BaseModel):
    name: str
