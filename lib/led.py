import time
import machine

led = machine.Pin('LED', machine.Pin.OUT)

def toggle():
  led.value(not led.value())
  time.sleep(0.5)
