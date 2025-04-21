import machine
import time

led = machine.Pin('LED', machine.Pin.OUT)

def toggle_led():
  led.value(not led.value())
  time.sleep(0.5)
