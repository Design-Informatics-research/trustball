import RPi.GPIO as GPIO
import time
import pyautogui

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

for k in buttons:
  GPIO.setup(k, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button pin
  GPIO.setup(buttons[k]['led'], GPIO.OUT) #LED pin

def check_state(button):
  button_state = GPIO.input(button)
  led_pin = buttons[button]['led']
  key = buttons[button]['key']
  if button_state == False:
    GPIO.output(led_pin, False)
    pyautogui.press(key)
    time.sleep(0.3)
  else:
    GPIO.output(led_pin, True)

try:
  while True:
    for k in buttons:
      check_state(k)
except:
  print("quitting")
  GPIO.cleanup()
