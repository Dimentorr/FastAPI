from typing import Optional
from datetime import datetime

from pydantic import BaseModel, ConfigDict, field_validator


class Task(BaseModel):
    name: str
    description: str
    time_to_complete: Optional[int] = 0
    
    model_config = ConfigDict(form_attributes=True)
