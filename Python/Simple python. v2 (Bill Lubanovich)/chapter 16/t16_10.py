"""
Увеличьте поле count хеша test и выведите его на экран.
"""
import redis
conn = redis.Redis()

conn.hincrby('test', 'count', 3)


print(conn.hget('test', 'count'))
