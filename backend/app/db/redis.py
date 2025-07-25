import json
from typing import Optional, Any, Union
from app.core.logging import logger

# Default cache expiration in seconds
DEFAULT_CACHE_EXPIRE = 300  # 5 minutes

# Temporary mock for Redis to avoid import errors
def log_cache_operation(operation: str, key: str, hit: bool = True):
    """Mock function for cache operations"""
    logger.info(f"Cache {operation}: {key} (mock)")


class RedisClient:
    """Mock Redis Client - uses in-memory cache"""
    def __init__(self):
        self.redis = "mock"  # Always set to non-None
        self._cache = {}  # In-memory cache as fallback
    
    async def connect(self):
        """Mock connect - just log that we're using mock"""
        logger.info("🟡 Using mock Redis client (no actual Redis connection)")
        self.redis = "mock"
    
    async def disconnect(self):
        """Mock disconnect - just log"""
        logger.info("🟡 Mock Redis disconnect (no action needed)")
    
    async def set(
        self, 
        key: str, 
        value: Union[str, dict, list], 
        expire: Optional[int] = None
    ) -> bool:
        """Mock SET - store in memory cache"""
        try:
            # Serialize non-string values to JSON for consistency
            if isinstance(value, (dict, list)):
                value = json.dumps(value, default=str)
            
            self._cache[key] = value
            log_cache_operation("SET", key)
            return True
        except Exception as e:
            logger.error(f"Mock Redis SET error for key {key}: {e}")
            return False
    
    async def get(self, key: str) -> Optional[Any]:
        """Mock GET - retrieve from memory cache"""
        try:
            value = self._cache.get(key)
            if value is None:
                log_cache_operation("GET", key, hit=False)
                return None
            
            # Try to deserialize JSON
            try:
                value = json.loads(value)
            except (json.JSONDecodeError, TypeError):
                # Keep as string if not valid JSON
                pass
            
            log_cache_operation("GET", key, hit=True)
            return value
        except Exception as e:
            logger.error(f"Mock Redis GET error for key {key}: {e}")
            return None
    
    async def delete(self, key: str) -> bool:
        """Mock DELETE - remove from memory cache"""
        try:
            if key in self._cache:
                del self._cache[key]
                log_cache_operation("DELETE", key)
                return True
            return False
        except Exception as e:
            logger.error(f"Mock Redis DELETE error for key {key}: {e}")
            return False
    
    async def exists(self, key: str) -> bool:
        """Mock EXISTS - check if key exists in memory cache"""
        try:
            result = key in self._cache
            return result
        except Exception as e:
            logger.error(f"Mock Redis EXISTS error for key {key}: {e}")
            return False
    
    async def flush_all(self) -> bool:
        """Mock FLUSH - clear memory cache"""
        try:
            self._cache.clear()
            logger.info("Mock Redis cache cleared")
            return True
        except Exception as e:
            logger.error(f"Mock Redis FLUSH error: {e}")
            return False
    
    async def invalidate_pattern(self, pattern: str) -> int:
        """Mock pattern delete - remove matching keys from memory cache"""
        try:
            keys_to_delete = [k for k in self._cache.keys() if pattern.replace('*', '') in k]
            deleted = 0
            for key in keys_to_delete:
                del self._cache[key]
                deleted += 1
            
            if deleted > 0:
                log_cache_operation("DELETE_PATTERN", pattern)
            return deleted
        except Exception as e:
            logger.error(f"Mock Redis pattern delete error for {pattern}: {e}")
            return 0


# Global Redis client instance
redis_client = RedisClient()


async def get_redis() -> RedisClient:
    """Dependency to get Redis client"""
    return redis_client


# Cache utility functions
async def cache_get(key: str) -> Optional[Any]:
    """Get value from cache"""
    return await redis_client.get(key)


async def cache_set(
    key: str, 
    value: Any, 
    expire: Optional[int] = None
) -> bool:
    """Set value in cache"""
    if expire is None:
        expire = DEFAULT_CACHE_EXPIRE
    return await redis_client.set(key, value, expire)


async def cache_delete(key: str) -> bool:
    """Delete value from cache"""
    return await redis_client.delete(key)


async def invalidate_home_cache():
    """Invalidate home page cache"""
    await cache_delete("home_cache")
    logger.info("Home cache invalidated")
