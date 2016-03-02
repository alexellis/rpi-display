import sys

class output_display:
    def __init__(self):
        pass
    def display(self, amt):
        if amt == None:
            print("-")
            return
        val = ""
        for x in range(0, int(amt)):
            val =val +"#"
        print(val)
