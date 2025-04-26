import time
import network
import urequests

from lib import secrets, config, lcd

wlan = network.WLAN(network.STA_IF)

def connect():
  ssid = secrets.WIFI_SSID
  password = secrets.WIFI_PASSWORD

  lcd.display("Connecting Wifi", 1)

  wlan.active(True)
  wlan.connect(ssid, password)

  print("Connecting to WiFi...")
  while not wlan.isconnected():
    time.sleep(1)
    lcd.display("Retrying...", 2)
    print("Still trying to connect...")

  lcd.display("Connected", 1)

  print("Connected to Wi-Fi:", wlan.ifconfig())

  health()

def health():
  lcd.display(f"Checking Wifi...", 2)

  r = urequests.get("https://www.google.com")
  status = r.status_code
  r.close()

  if status == 200:
    lcd.display(f"Online ({config.APP_VERSION})", 2)
    config.PUBLISHER_LED.on()
  else:
    lcd.display(f"Offline ({config.APP_VERSION})", 2)
    wlan.disconnect()
    config.PUBLISHER_LED.off()
    connect()
