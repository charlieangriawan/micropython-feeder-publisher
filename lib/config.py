from machine import Pin

APP_VERSION = "v1.0.0"
APP_CYCLE_SECOND = 0.1

LCD_RS_PIN = 0
LCD_E_PIN  = 1
LCD_D4_PIN = 2
LCD_D5_PIN = 3
LCD_D6_PIN = 4
LCD_D7_PIN = 5

NAIXI_LED = Pin(11, Pin.OUT)
NAICHA_LED = Pin(15, Pin.OUT)
PUBLISHER_LED = Pin(28, Pin.OUT)

NAIXI_BUTTON = Pin(10, Pin.IN, Pin.PULL_UP)
NAICHA_BUTTON = Pin(14, Pin.IN, Pin.PULL_UP)
RESET_BUTTON = Pin(13, Pin.IN, Pin.PULL_UP)
