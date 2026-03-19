from __future__ import annotations
from datetime import datetime
from typing import Optional
from odmantic import ObjectId, Field
from app.db.base_class import Base

def datetime_now_sec():
    return datetime.now().replace(microsecond=0)

class WellnessChallenge(Base):
    name: str
    description: str
    start_date: datetime
    end_date: datetime
    target_steps: Optional[int] = Field(default=10000)
    points: int = Field(default=100)
    created: datetime = Field(default_factory=datetime_now_sec)
    modified: datetime = Field(default_factory=datetime_now_sec)

class ActivityLog(Base):
    user_id: ObjectId
    activity_type: str = Field()
    value: float  # e.g., steps or minutes
    date: datetime = Field(default_factory=datetime_now_sec)
    created: datetime = Field(default_factory=datetime_now_sec)
