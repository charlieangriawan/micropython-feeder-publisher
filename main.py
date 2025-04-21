from utime import sleep

from lib import config, wifi, clock, lcd, led

def init():
  print("Program: start")
  lcd.configure()
  wifi.connect()
  wifi.health()

  clock.sync_rtc()

def main():
  clock.tick()
  [hour, minute, second] = clock.now()
  print(second)
  led.toggle()

def end():
  print("Program: end")

def app():
  try:
    init()
    while True:
      main()
      sleep(config.APP_CYCLE_SECOND)
  except KeyboardInterrupt:
    pass
  finally:
    end()

app()
