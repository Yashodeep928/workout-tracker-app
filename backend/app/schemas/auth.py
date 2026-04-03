from pydantic import BaseModel, EmailStr


class LoginRequest(BaseModel):
    # Input schema for login request
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    # Response schema returned after successful login
    access_token: str
    token_type: str