# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685

import random as rnd

# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 150  # 150 Min pulse length out of 4096
servo_max = 450  # 600 Max pulse length out of 4096
increment = 10
initial_state = 150

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

#print('Moving servo on channel 0, press Ctrl-C to quit...')

def get_servo_min():
    return servo_min

def get_servo_max():
    return servo_max

def open(channel=0, pulse_length=servo_min):
    pwm.set_pwm(channel, 0, pulse_length)
    time.sleep(0.5)

def close(channel=0, pulse_length=servo_max):
    pwm.set_pwm(channel, 0, pulse_length)
    time.sleep(0.3)

#def random(channel=0):
    #open(channel, rnd.randrange(servo_min, servo_max))

def move(channel=0, amount=servo_min):
    pwm.set_pwm(channel, 0, amount)
    time.sleep(0.5) #0.5


def open_slower(channel=0, lap=2):
    x = 150
    i = 1
    j = 0
    while j<lap:
      x = i*increment+x
      pwm.set_pwm(channel, 0, x)
      time.sleep(0.03)
      if (x==150 or x==600):
        i = i*(-1)
        j += 1

def random(channel=0, lap=2):
    j = 0
    while j<lap:
      a = rnd.randrange(300, 400, 10)
      b = rnd.randrange(500, 600, 10)
      print(a, b)
      if (j==0): 
        x = b
        pwm.set_pwm(channel, 0, a)
        #time.sleep(0.3)
        #pwm.set_pwm(1, 0, 150)
        while (x>a):
          x = x - 5
          pwm.set_pwm(channel, 0, x)
          time.sleep(0.01)
      else:
        x = a
        pwm.set_pwm(channel, 0, b)
        #time.sleep(0.3)
        #pwm.set_pwm(1, 0, 450)
        while (x<b):
          x = x + 5
          pwm.set_pwm(channel, 0, x)
          time.sleep(0.01)
      j += 1
      print(x)
      time.sleep(0.5)


def page1():
    open(1)
    close(1)
    random(2)
    #time.sleep(0.1)
    

def page2():
    open(3)
    close(3)
    random(4)
    #time.sleep(0.1)

def page3():
    open(5)
    close(5)
    random(6)
    #time.sleep(0.1)

open_slower()
time.sleep(1)
page1()
page2()
page3()
#random(2)