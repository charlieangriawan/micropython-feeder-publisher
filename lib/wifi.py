import time
import network
# import urequests

from lib import secrets, config, lcd

def connect():
  ssid = secrets.WIFI_SSID
  password = secrets.WIFI_PASSWORD

  lcd.display("Connecting Wifi", 1)

  wlan = network.WLAN(network.STA_IF)
  wlan.active(True)
  wlan.connect(ssid, password)

  print("Connecting to WiFi...")
  while not wlan.isconnected():
    time.sleep(1)
    lcd.display("Retrying...", 2)
    print("Still trying to connect...")

  lcd.display("Connected", 1)
  lcd.display("to Wifi", 2)

  print("Connected to Wi-Fi:", wlan.ifconfig())
  config.PUBLISHER_LED.on()
