from app.core.cached import redis_client
import json 

class RedisService:
    def __init__(self):
        self.client = redis_client

    def get (self, key: str):
        return self.client.get(key) if self.client else None

    def set (self, key: str, value: any, ex: int = 60):
        return self.client.set(key, value, ex=ex) if self.client else None

    def delete (self, key : str):
        return self.client.delete(key) if self.client else None
    
    def get_with_json(self, key: str):
        if self.client is None:
            return None 
        cached_data = self.client.get(key) 
        if cached_data:
            return json.loads(cached_data)
        else:
            return cached_data

    def set_with_json (self, key: str, value: any, ex: int = 60):
        return self.client.set(key, json.dumps(value), ex=ex)
    
def get_redis_service():
    return RedisService()