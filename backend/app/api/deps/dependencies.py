from typing import Generator, Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.security import verify_token, SecurityException
from app.core.logging import logger
from app.db.database import get_db
from app.db.redis import get_redis, RedisClient
from app.config import settings
from app.schemas.auth import AdminUser


# Security scheme
security = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
) -> AdminUser:
    """Get current authenticated admin user"""
    try:
        # Extract token from credentials
        token = credentials.credentials
        
        # Verify token
        username = verify_token(token)
        if username is None:
            raise SecurityException("Could not validate credentials")
        
        # In a real application, you would fetch user from database
        # For now, we validate against admin email from settings
        if username != settings.ADMIN_EMAIL:
            raise SecurityException("Invalid admin user")
        
        return AdminUser(
            email=username,
            is_active=True,
            is_admin=True
        )
        
    except Exception as e:
        logger.error(f"Authentication error: {e}")
        raise SecurityException("Could not validate credentials")


async def get_current_admin(
    current_user: AdminUser = Depends(get_current_user)
) -> AdminUser:
    """Dependency to ensure user is admin"""
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin privileges required"
        )
    return current_user


# Database dependency (already exists in db/database.py but imported here for convenience)
async def get_database() -> AsyncSession:
    """Get database session"""
    async for db in get_db():
        yield db


# Redis dependency
async def get_redis_client() -> RedisClient:
    """Get Redis client"""
    return await get_redis()


def get_settings():
    """Get application settings"""
    return settings
