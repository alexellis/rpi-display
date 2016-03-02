import sys
import time

#from displays import terminal_display
from scrollphat_display import scrollphat_display
from redis_controller import redis_controller

#display = terminal_display()
display = scrollphat_display()
redis_controller1 = redis_controller("Timer1", sys.argv[1])

def messageReady():
    print ("_")
    display.display(redis_controller1.get())

redis_controller1.set_subscriber_callback(messageReady)
redis_controller1.subscribe()

while(True):
    time.sleep(1)
