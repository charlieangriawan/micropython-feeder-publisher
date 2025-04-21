import time
import network

from lib import secrets

def connect():
  ssid = secrets.WIFI_SSID
  password = secrets.WIFI_PASSWORD

  wlan = network.WLAN(network.STA_IF)
  wlan.active(True)
  wlan.connect(ssid, password)

  print("Connecting to WiFi...")
  while not wlan.isconnected():
    time.sleep(1)
    print("Still trying to connect...")

  print("Connected to Wi-Fi:", wlan.ifconfig())
