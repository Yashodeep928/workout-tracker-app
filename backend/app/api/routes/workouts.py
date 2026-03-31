from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.workout import WorkoutCreate, WorkoutResponse
from app.services.workout_service import (
    create_workout,
    get_all_workouts,
    get_workouts_by_user,
)


# Create router for workout-related endpoints
router = APIRouter(prefix="/workouts", tags=["Workouts"])


# Create a new workout
@router.post("/", response_model=WorkoutResponse, status_code=201)
def create_workout_route(payload: WorkoutCreate, db: Session = Depends(get_db)):
    # Call service layer to create workout
    return create_workout(db, payload)


# Get all workouts
@router.get("/", response_model=list[WorkoutResponse])
def get_workouts_route(db: Session = Depends(get_db)):
    # Call service layer to fetch all workouts
    return get_all_workouts(db)


# Get workouts for a specific user
@router.get("/user/{user_id}", response_model=list[WorkoutResponse])
def get_workouts_by_user_route(user_id: int, db: Session = Depends(get_db)):
    # Call service layer to fetch workouts for a given user
    return get_workouts_by_user(db, user_id)