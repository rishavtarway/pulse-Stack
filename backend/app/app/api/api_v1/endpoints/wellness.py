from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from motor.core import AgnosticDatabase
from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("/challenges", response_model=List[schemas.wellness.WellnessChallenge])
async def read_challenges(
    db: AgnosticDatabase = Depends(deps.get_db),
    page: int = 0,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve challenges.
    """
    challenges = await crud.wellness.wellness_challenge.get_multi(db, page=page)
    return challenges

@router.post("/challenges", response_model=schemas.wellness.WellnessChallenge)
async def create_challenge(
    *,
    db: AgnosticDatabase = Depends(deps.get_db),
    challenge_in: schemas.wellness.WellnessChallengeCreate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create a new challenge. (Superuser only)
    """
    challenge = await crud.wellness.wellness_challenge.create(db, obj_in=challenge_in)
    return challenge

@router.post("/activity", response_model=schemas.wellness.ActivityLog)
async def log_activity(
    *,
    db: AgnosticDatabase = Depends(deps.get_db),
    activity_in: schemas.wellness.ActivityLogBase,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Log a new wellness activity.
    """
    activity_data = schemas.wellness.ActivityLogCreate(
        **activity_in.dict(),
        user_id=current_user.id
    )
    activity = await crud.wellness.activity_log.create(db, obj_in=activity_data)
    return activity

@router.get("/activity", response_model=List[schemas.wellness.ActivityLog])
async def read_activities(
    db: AgnosticDatabase = Depends(deps.get_db),
    page: int = 0,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve user activity logs.
    """
    # Note: In a real app, we would add a filter by user_id in get_multi or a specific method
    activities = await crud.wellness.activity_log.get_multi(db, page=page)
    return [a for a in activities if a.user_id == current_user.id]
