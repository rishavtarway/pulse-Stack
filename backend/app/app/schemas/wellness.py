from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from odmantic import ObjectId

class WellnessChallengeBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    target_steps: Optional[int] = 10000
    points: Optional[int] = 100

class WellnessChallengeCreate(WellnessChallengeBase):
    name: str
    description: str
    start_date: datetime
    end_date: datetime

class WellnessChallengeUpdate(WellnessChallengeBase):
    pass

class WellnessChallenge(WellnessChallengeBase):
    id: ObjectId
    created: datetime
    modified: datetime

    class Config:
        from_attributes = True

class ActivityLogBase(BaseModel):
    activity_type: Optional[str] = None
    value: Optional[float] = None
    date: Optional[datetime] = None

class ActivityLogCreate(ActivityLogBase):
    activity_type: str
    value: float
    user_id: ObjectId

class ActivityLog(ActivityLogBase):
    id: ObjectId
    user_id: ObjectId
    created: datetime

    class Config:
        from_attributes = True
