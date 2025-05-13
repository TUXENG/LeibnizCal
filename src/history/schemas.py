from pydantic import BaseModel
from typing import Literal
from datetime import datetime

class HistoryEntry(BaseModel):
    id: int
    expression: str
    result: str
    type: Literal["defined", "undefined"]
    timestamp: datetime
