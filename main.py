from utime import sleep

from lib import config, wifi, clock, lcd, hardware, publisher

def init():
  print("Program: start")
  hardware.reset()
  lcd.configure()
  wifi.connect()
  clock.sync_rtc()

def main():
  clock.tick()
  publisher.check_missed_feeding()
  hardware.listen()

def end():
  print("Program: end")
  hardware.kill()

def app():
  try:
    init()
    while True:
      main()
      sleep(config.APP_CYCLE_SECOND)
  except Exception as e:
    print(e)
  finally:
    end()

app()
