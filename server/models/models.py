from pydantic import BaseModel
from typing import Optional

class Event(BaseModel):
    title: str
    start_datetime: str
    end_datetime: str
    description: Optional[str] = None
    location: Optional[str] = None
    is_recurring: Optional[bool] = False
    recurrence_rule: Optional[str] = None

class EventUpdate(BaseModel):
    title: Optional[str] = None
    start_datetime: Optional[str] = None
    end_datetime: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None

class AIChatRequest(BaseModel):
    message: str