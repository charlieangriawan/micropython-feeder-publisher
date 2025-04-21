from lib import wifi, lcd, led

def init():
  print("Program: start")
  lcd.configure()
  wifi.connect()

def end():
  print("Program: end")

def main():
  try:
    init()
    while True:
      led.toggle()
  except KeyboardInterrupt:
    pass
  finally:
    end()

main()
