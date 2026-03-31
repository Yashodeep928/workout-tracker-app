from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


# This model represents the "users" table in PostgreSQL
class User(Base):
    __tablename__ = "users"

    # Primary key column (auto increment integer)
    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    # User name column
    name: Mapped[str] = mapped_column(String(100), nullable=False)

    # Email should be unique because no two users should share same email
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)

    # One user can have many workouts
    workouts = relationship("Workout", back_populates="user", cascade="all, delete-orphan")