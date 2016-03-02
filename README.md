rpi-display: Remote Display for Raspberry PI
============================================

### The arrangement

You have two Raspberry PIs, one is connected to a sensor - such as a PIR and the other is connected to a Scrollphat display or similar.

* For every minute the PIR sees inactivity there will be one dot displayed on the scrollphat.
* If the PIR senses motion it will reset the timer and the display

![Sample image of live scrollphat system](/docs/output_display.jpg)

*Sample picture of the output display after several minutes of inactivity*


### Running the code

**On the sensing PI:**

First update the PIN number in your `sender.py` file or connect a PIR to the default PIN **17**.

```
# redis-server &
# python sender.py
```

**On the display PI:**

If you do not own a scrollphat then replace the `scrollphat_display` for the `terminal_display` class and you will see `#` symbols printed out instead.

```
python display.py IPAddressOfSensingPI
```
