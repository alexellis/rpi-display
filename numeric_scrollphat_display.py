import scrollphat
import time

class output_display:
    def __init__(self):
        MID_LEVEL = 10
        scrollphat.clear()
        scrollphat.update()
        scrollphat.set_brightness(MID_LEVEL)

        self.last = 0
        self.HEIGHT = 5
        self.WIDTH = 11
        self.MAX = (self.WIDTH) * (self.HEIGHT)

    def display(self, amt):
        val = 0
        if(amt != None):
            val = int(amt)
        txt = str(val)
        if(val <10):
            txt = "  " +txt
        elif(val < 100):
            txt = " "+txt

        scrollphat.clear()
        scrollphat.write_string(txt)
        scrollphat.update()
