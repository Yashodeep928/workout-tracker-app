from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse


# Create router for all user-related endpoints
router = APIRouter(prefix="/users", tags=["Users"])


# Create a new user
@router.post("/", response_model=UserResponse, status_code=201)
def create_user(payload: UserCreate, db: Session = Depends(get_db)):
    # Check if email already exists in DB
    existing_user = db.query(User).filter(User.email == payload.email).first()

    if existing_user:
        # If email already exists, return 400 error
        raise HTTPException(status_code=400, detail="Email already registered")

    # Create SQLAlchemy user object from incoming request data
    user = User(name=payload.name, email=payload.email)

    # Save to DB
    db.add(user)
    db.commit()
    db.refresh(user)

    # Return created user
    return user


# Get all users
@router.get("/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    # Fetch all users from DB
    users = db.query(User).all()

    # Return list of users
    return users