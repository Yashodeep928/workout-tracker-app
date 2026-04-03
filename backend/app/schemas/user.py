from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime


class UserCreate(BaseModel):
    # Input schema for user registration
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    # Safe response schema sent back to client (no password)
    id: int
    email: EmailStr
    created_at: datetime

    # Allow reading data directly from SQLAlchemy model
    model_config = ConfigDict(from_attributes=True)