# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time
import Adafruit_PCA9685

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 1440  # Min pulse length out of 4096
servo_stop = 1500 # 400 @ 60Hz 
servo_max = 1530 # Max pulse length out of 4096

#1500mseconds
#Speed:	4.8V: 0.23 sec/60°
#6.0V: 0.19 sec/60°

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 100       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(225)

print('Moving servo on channel 0, press Ctrl-C to quit...')
i = 0
while True:
    pwm.set_pwm(0, 0, servo_stop)
    time.sleep(1.5)
    pwm.set_pwm(0, 0, servo_max)
    time.sleep(1)
    pwm.set_pwm(0, 0, servo_stop)
    time.sleep(1.5)
    pwm.set_pwm(0, 0, servo_min)
    time.sleep(1)