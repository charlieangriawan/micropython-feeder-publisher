import machine

led = machine.Pin('LED', machine.Pin.OUT)

def toggle():
  led.value(not led.value())
