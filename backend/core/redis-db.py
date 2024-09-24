import redis
from config import settings

r = redis.Redis(
  host=settings.RS_HOST,
  port=settings.RS_PORT,
  password=settings.RS_PASSWORD
  )
