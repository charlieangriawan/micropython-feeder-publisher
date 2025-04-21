from lib import config, publisher, lcd

NAIXI_FED = False
NAICHA_FED = False
RESET_BUTTON_PRESSED = False

def reset():
  global NAIXI_FED
  global NAICHA_FED

  NAIXI_FED = False
  NAICHA_FED = False
  config.NAIXI_LED.off()
  config.NAICHA_LED.off()
  publisher.set_notification_sent(False)

def listen():
  global NAIXI_FED
  global NAICHA_FED
  global RESET_BUTTON_PRESSED

  if not NAIXI_FED and config.NAIXI_BUTTON.value() == 0:
    NAIXI_FED = True
    publisher.set_notification_sent(False)
    config.NAIXI_LED.on()
    
  if not NAICHA_FED and config.NAICHA_BUTTON.value() == 0:
    NAICHA_FED = True
    publisher.set_notification_sent(False)
    config.NAICHA_LED.on()

  if config.RESET_BUTTON.value() == 0:
    if (not RESET_BUTTON_PRESSED):
      reset()
    RESET_BUTTON_PRESSED = True
  else:
    RESET_BUTTON_PRESSED = False

def fed():
  return NAIXI_FED, NAICHA_FED

def kill():
  config.NAIXI_LED.off()
  config.NAICHA_LED.off()
  config.PUBLISHER_LED.off()
  lcd.off()
