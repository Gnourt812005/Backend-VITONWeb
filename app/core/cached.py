import redis
from app.core.config import settings

# Redis
redis_client = redis.Redis.from_url(settings.getRedisUrl())