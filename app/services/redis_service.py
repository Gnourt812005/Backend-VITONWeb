from app.core.cached import redis_client
import json 

class RedisService:
    def __init__(self):
        self.client = redis_client

    def get (self, key: str):
        return self.client.get(key)
    
    def set (self, key: str, value: any, ex: int = 60):
        return self.client.set(key, value, ex=ex)

    def delete (self, key : str):
        return self.client.delete(key)
    
    def get_with_json(self, key: str):
        cached_data = self.client.get(key)
        if cached_data:
            return json.loads(cached_data)
        else:
            cached_data

    def set_with_json (self, key: str, value: any, ex: int = 60):
        return self.client.set(key, json.dumps(value), ex=ex)
    
def get_redis_service():
    return RedisService()