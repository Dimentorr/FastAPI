from typing import Optional
from datetime import datetime

from pydantic import BaseModel, ConfigDict, field_validator


class ValidateToken(BaseModel):
    token: str


class Task(BaseModel):
    name: str
    description: str
    time_to_complete: Optional[int] = 0
    token: str


class Users(BaseModel):
    name: str
    password: str


class Tokens(BaseModel):
    token: str
