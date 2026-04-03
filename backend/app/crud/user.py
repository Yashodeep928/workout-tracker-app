from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password


def get_user_by_email(db: Session, email: str):
    # Find user by email (used in register and login)
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user_data: UserCreate):
    # Convert plain password into hash before saving
    hashed_password = hash_password(user_data.password)

    # Create new user model instance
    user = User(
        email=user_data.email,
        hashed_password=hashed_password,
    )

    # Save to DB
    db.add(user)
    db.commit()
    db.refresh(user)

    return user