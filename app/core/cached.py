import redis
from app.core.config import settings
import logging

logger = logging.getLogger(__name__)
# Redis
redis_client : any
try:
    redis_client = redis.Redis.from_url(settings.getRedisUrl())
except Exception as e:
    logger.error(f"Error: {e}")
    redis_client = None 
