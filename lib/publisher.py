from lib import clock, hardware, notification

PUBLISHER_NOTIFICATION_SENT = False

def set_notification_sent(state):
  global PUBLISHER_NOTIFICATION_SENT
  PUBLISHER_NOTIFICATION_SENT = state

def check_missed_feeding():
  [hour, minute, second] = clock.now()

  if (hour == 10 and minute == 0 and second == 0):
    broadcast_hungry_girls()
    hardware.reset()

  elif (hour == 22 and minute == 0 and second == 0):
    broadcast_hungry_girls()
    hardware.reset()
  elif (not PUBLISHER_NOTIFICATION_SENT and second == 0):
    broadcast_happy_girls()

def broadcast_hungry_girls():
  hour = clock.hour()
  [naixi_fed, naicha_fed] = hardware.fed()

  message = None
  context = "breakfast" if (3 <= hour and hour <= 15) else "dinner"

  if not naixi_fed and not naicha_fed:
    message = f"both Naixi and Naicha SKIPPED {context}. (ALERT)"
  elif not naixi_fed:
    message = f"Naixi SKIPPED {context}. (ALERT)"
  elif not naicha_fed:
    message = f"Naicha SKIPPED {context}. (ALERT)"

  if (message):
    notification.notify_subscribers(message)

def broadcast_happy_girls():
  global PUBLISHER_NOTIFICATION_SENT

  hour = clock.hour()
  [naixi_fed, naicha_fed] = hardware.fed()

  message = None
  context = "breakfast" if (3 <= hour and hour <= 15) else "dinner"

  if naixi_fed and naicha_fed:
    message = f"both Naixi and Naicha have been fed {context}."
  elif naixi_fed:
    message = f"Naixi have been fed {context}."
  elif naicha_fed:
    message = f"Naicha have been fed {context}."

  if (message):
    notification.notify_subscribers(message)
  
  PUBLISHER_NOTIFICATION_SENT = True
