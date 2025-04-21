from lib import wifi, led

def init():
  print("Program: start")
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
