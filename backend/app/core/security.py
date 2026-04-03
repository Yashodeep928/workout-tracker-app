from datetime import datetime, timedelta, timezone
from jose import jwt
from passlib.context import CryptContext

from app.core.config import settings

# This object handles password hashing and verification using bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    # Convert plain password into secure hash before storing in DB
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    # Compare entered password with stored hashed password
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    # Copy the data so original dictionary is not modified
    to_encode = data.copy()

    # Decide token expiry time
    expire = datetime.now(timezone.utc) + (
        expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    # Add expiry to token payload
    to_encode.update({"exp": expire})

    # Create and return signed JWT token
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)