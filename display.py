import sys
import time
from config import config_values

#from terminal_display import output_display
from scrollphat_display import output_display
from redis_controller import redis_controller

output_display1 = output_display()
redis_controller1 = redis_controller(config_values["redis_key"], sys.argv[1])

def messageReady():
    print ("_")
    output_display1.display(redis_controller1.get())

redis_controller1.set_subscriber_callback(messageReady)
redis_controller1.subscribe()

while(True):
    time.sleep(1)
