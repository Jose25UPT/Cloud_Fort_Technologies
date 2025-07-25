from fastapi import APIRouter, Depends, HTTPException, status
from datetime import timedelta
from app.core.security import create_access_token, authenticate_admin
from app.config import settings
from app.schemas.auth import LoginRequest, LoginResponse

router = APIRouter()


@router.post("/login", response_model=LoginResponse)
async def login_admin(form_data: LoginRequest):
    """Admin login"""
    if not authenticate_admin(form_data.email, form_data.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        subject=form_data.email, expires_delta=access_token_expires
    )
    return LoginResponse(access_token=access_token, token_type="bearer", expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60)
