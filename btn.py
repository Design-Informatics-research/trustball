import RPi.GPIO as GPIO
import time
import pyautogui
import os

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

#inpin = 27
#outpin = 22

buttons = {
  17: { 'key': '1', 'led': 18 },
  27: { 'key': '2', 'led': 22 },
  23: { 'key': '3', 'led': 24 },
  5: { 'key': '4', 'led': 6 },
  19: { 'key': '5', 'led': 20 },
}

buttons24 = {
  17: { 'key': '1', 'led': 18 },
  19: { 'key': '5', 'led': 20 },
}

def all_on():
  for k in buttons:
    GPIO.setup(k, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button pin
    GPIO.setup(buttons[k]['led'], GPIO.OUT) #LED pin
  GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Reset button pin

def all_off():
  for k in buttons:
    GPIO.output(buttons[k]['led'], False)

def two_on():
  for k in buttons24:
    GPIO.setup(k, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button pin
    GPIO.setup(buttons24[k]['led'], GPIO.OUT) #LED pin
  GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Reset button pin

def buttonAll():
  GPIO.setmode(GPIO.BCM)
  all_on()
  b=0
  while True:
    if GPIO.input(21) == False:
      pyautogui.press('6')
      print('reset')
      #GPIO.cleanup()
      break
    if b==1:
      #GPIO.cleanup()
      break
    for button in buttons:
      #print(button)
      button_state = GPIO.input(button)
      led_pin = buttons[button]['led']
      key = buttons[button]['key']
      if button_state == False:
        b = 1
        for k in buttons:
          if not k==button:
            GPIO.output(buttons[k]['led'], False)
        pyautogui.press(key)
        os.system('aplay OldSchool10.wav &')
        time.sleep(2)
      else:
        GPIO.output(led_pin, True)

def buttonAll_nodelay():
  GPIO.setmode(GPIO.BCM)
  all_on()
  b=0
  while True:
    if GPIO.input(21) == False:
      pyautogui.press('6')
      print('reset')
      #GPIO.cleanup()
      break
    if b==1:
      #GPIO.cleanup()
      break
    for button in buttons:
      button_state = GPIO.input(button)
      led_pin = buttons[button]['led']
      key = buttons[button]['key']
      if button_state == False:
        b = 1
        for k in buttons:
          if not k==button:
            GPIO.output(buttons[k]['led'], False)
        pyautogui.press(key)
        time.sleep(0.3)
      else:
        GPIO.output(led_pin, True)


def buttonTwo():
  GPIO.setmode(GPIO.BCM)
  two_on()
  b=0
  while True:
    if GPIO.input(21) == False:
      pyautogui.press('6')
      print('reset')
      #GPIO.cleanup()
      break
    if b==1:
      #GPIO.cleanup()
      break
    for button in buttons24:
      button_state = GPIO.input(button)
      led_pin = buttons24[button]['led']
      key = buttons24[button]['key']
      if button_state == False:
        pyautogui.press(key)
        os.system('aplay Beep6.wav &')
        b = 1
        for k in buttons24:
          if not k==button:
            GPIO.output(buttons24[k]['led'], False)
        time.sleep(1)
      else:
        GPIO.output(led_pin, True)


def blink():
  GPIO.setmode(GPIO.BCM)
  all_on()
  all_off()
  b = 0
  c = 0
  order = [17, 27, 23, 5, 19]
  while True:
    #print('im here')
    if ((b == 1) or (c == 1)):
      print(button)
      #GPIO.cleanup()
      break
    for button in order:
      for k in order:  
        if GPIO.input(k) == False:
          pyautogui.press(buttons[k]['key'])
          os.system('mpg123 -q Jingle_Lose_00.mp3 &')
          b = 1
          break
        if GPIO.input(21) == False:
          pyautogui.press('6')
          print(button)
          c = 1
          break
        if not k==button:
          GPIO.output(buttons[k]['led'], False)
        else:
          GPIO.output(buttons[k]['led'], True)
      if ((b == 1) or (c == 1)):
          break
      time.sleep(0.2)

#buttonAll()
#buttonTwo()
#blink()
