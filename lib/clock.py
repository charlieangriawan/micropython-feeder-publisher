import urequests
from machine import RTC

from lib import secrets, lcd

STSTEM_RTC = RTC()
SYSTEM_HOUR_NOW = 0
SYSTEM_MINUTE_NOW = 0
SYSTEM_SECOND_NOW = 0

def sync_rtc():
  lcd.display("Syncing Clock", 1)

  url = f'http://api.ipgeolocation.io/timezone?apiKey={secrets.GEOLOCATION_SECRET}&tz=Asia/Singapore'
  r = urequests.get(url)
  data = r.json()

  current_time = data["date_time"]
  the_date, the_time = current_time.split(" ")

  year, month, mday = map(int, the_date.split("-"))
  hours, minutes, seconds = map(int, the_time.split(":"))
  week_day = data.get("day_of_week", 0) 

  STSTEM_RTC.datetime((year, month, mday, week_day, hours, minutes, seconds, 0))

  lcd.display(f"Time: {hours:02}:{minutes:02}:{seconds:02}", 1)

def tick():
  global SYSTEM_HOUR_NOW
  global SYSTEM_MINUTE_NOW
  global SYSTEM_SECOND_NOW

  now = STSTEM_RTC.datetime()

  if (SYSTEM_SECOND_NOW != now[6]):
    lcd.display(f"Time: {SYSTEM_HOUR_NOW:02}:{SYSTEM_MINUTE_NOW:02}:{SYSTEM_SECOND_NOW:02}", 1)

  SYSTEM_HOUR_NOW = now[4]
  SYSTEM_MINUTE_NOW = now[5]
  SYSTEM_SECOND_NOW = now[6]

def now():
  return SYSTEM_HOUR_NOW, SYSTEM_MINUTE_NOW, SYSTEM_SECOND_NOW

def hour():
  return SYSTEM_HOUR_NOW
