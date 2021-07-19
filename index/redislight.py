from redislite import Redis
from json import dumps
from django.core.serializers.json import DjangoJSONEncoder

class RedisLight():
    def __init__(self) :
        self.redis_instance = self.__call__()

    def __call__(self):
        redis_instance = Redis('/tmp/redis.db')
        return redis_instance

    def get_redis(self,key_redis):
        instance =self.redis_instance.get(key_redis)
        return instance
        
    def set_queryset_values_redis(self,key_redis,qs_values):
        self.redis_instance.set(key_redis, dumps(list(qs_values), cls=DjangoJSONEncoder))
