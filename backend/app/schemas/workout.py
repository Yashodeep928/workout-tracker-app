from pydantic import BaseModel, ConfigDict


# Schema for incoming request when creating a workout
class WorkoutCreate(BaseModel):
    title: str
    description: str | None = None
    user_id: int


# Schema for outgoing response when returning workout data
class WorkoutResponse(BaseModel):
    id: int
    title: str
    description: str | None = None
    user_id: int

    # Allow conversion from SQLAlchemy model -> API response
    model_config = ConfigDict(from_attributes=True)