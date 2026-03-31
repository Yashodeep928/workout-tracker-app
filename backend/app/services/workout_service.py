from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.user import User
from app.models.workout import Workout
from app.schemas.workout import WorkoutCreate


# This function contains business logic for creating a workout
def create_workout(db: Session, payload: WorkoutCreate) -> Workout:
    # First check if the user exists
    user = db.query(User).filter(User.id == payload.user_id).first()

    if not user:
        # If user does not exist, return 404
        raise HTTPException(status_code=404, detail="User not found")

    # Create workout object
    workout = Workout(
        title=payload.title,
        description=payload.description,
        user_id=payload.user_id,
    )

    # Save workout in DB
    db.add(workout)
    db.commit()
    db.refresh(workout)

    return workout


# This function returns all workouts
def get_all_workouts(db: Session) -> list[Workout]:
    return db.query(Workout).all()


# This function returns all workouts for a specific user
def get_workouts_by_user(db: Session, user_id: int) -> list[Workout]:
    # Check if user exists first
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return db.query(Workout).filter(Workout.user_id == user_id).all()