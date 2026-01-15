from app.crud.base import CRUDBase
from app.models.wellness import WellnessChallenge, ActivityLog
from app.schemas.wellness import WellnessChallengeCreate, WellnessChallengeUpdate, ActivityLogCreate

class CRUDWellnessChallenge(CRUDBase[WellnessChallenge, WellnessChallengeCreate, WellnessChallengeUpdate]):
    pass

class CRUDActivityLog(CRUDBase[ActivityLog, ActivityLogCreate, ActivityLogCreate]):
    pass

wellness_challenge = CRUDWellnessChallenge(WellnessChallenge)
activity_log = CRUDActivityLog(ActivityLog)
