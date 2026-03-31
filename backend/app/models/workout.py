from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


# This model represents the "workouts" table in PostgreSQL
class Workout(Base):
    __tablename__ = "workouts"

    # Primary key for workout table
    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    # Workout title like "Chest Day", "Leg Day"
    title: Mapped[str] = mapped_column(String(150), nullable=False)

    # Optional longer description of the workout
    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Foreign key: each workout belongs to one user
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, index=True)

    # Relationship back to the user object
    user = relationship("User", back_populates="workouts")