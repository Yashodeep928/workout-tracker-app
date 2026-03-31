from sqlalchemy.orm import DeclarativeBase


# Base class for all SQLAlchemy models
class Base(DeclarativeBase):
    pass


# Import models here so Alembic can detect them
# from app.models.user import User 
# from app.models.workout import Workout  