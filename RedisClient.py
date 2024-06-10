import sys
import redis


print("Hello World!")
print(sys.version)


def retriveFromRedis(id, b):
    print("My function ", id, b)
    r = redis.Redis(host='localhost', port=6379, db=0, decode_responses='true')
    print(r.hgetall('Student:' + str(id)))
    keys = r.keys()
    r.close()
