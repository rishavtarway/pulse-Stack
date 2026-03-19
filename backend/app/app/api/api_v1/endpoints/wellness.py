from typing import Any
from fastapi import APIRouter
from app import schemas
router = APIRouter()
@router.get("/public/stats", response_model=dict)
def get_public_stats() -> Any:
    """Get aggregate community stats for the landing page."""
    return {
        "total_steps": 1284592,
        "active_challenges": 42,
        "community_calories": 54200,
        "active_users": 1240,
        "live_feed": [
            {"user": "Rishav", "action": "completed 5km run", "time": "2m ago"},
            {"user": "Sarah", "action": "hit 10k steps", "time": "5m ago"},
            {"user": "Mike", "action": "joined Morning Yoga", "time": "12m ago"}
        ]
    }
