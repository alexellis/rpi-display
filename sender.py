import time

from redis_controller import redis_controller
from sensors import PIR
from config import config_values

def PIR_triggered(name):
    print (name, "fired sensor")
    redis_controller1.reset()
    print ("-")

pir1 = PIR(17, "PIR1", PIR_triggered)
redis_controller1 = redis_controller(config_values["redis_key"], "127.0.0.1")

secs = 0
secs_per_tick = 1
while(True):
    if secs > secs_per_tick:
        secs = 0
        print (".")
        redis_controller1.increment()
    secs = secs + 1
    time.sleep(1)
