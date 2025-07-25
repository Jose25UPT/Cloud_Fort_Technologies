from typing import Optional
from pydantic import BaseModel, Field, EmailStr


class LoginRequest(BaseModel):
    email: EmailStr = Field(..., description="Admin email")
    password: str = Field(..., min_length=1, description="Admin password")


class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int  # seconds


class TokenData(BaseModel):
    username: Optional[str] = None


class AdminUser(BaseModel):
    email: EmailStr
    is_active: bool = True
    is_admin: bool = True
