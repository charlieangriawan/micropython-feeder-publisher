import time
from machine import Pin

from lib import config

LCD_RS = config.LCD_RS_PIN
LCD_E  = config.LCD_E_PIN
LCD_D4 = config.LCD_D4_PIN
LCD_D5 = config.LCD_D5_PIN
LCD_D6 = config.LCD_D6_PIN
LCD_D7 = config.LCD_D7_PIN

LCD_WIDTH = 16
LCD_CHR = 1
LCD_CMD = 0
LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
LCD_PULSE = 0.0005
LCD_DELAY = 0.0005

def configure():
  set_byte(0x33,LCD_CMD) # 110011 Initialise
  set_byte(0x32,LCD_CMD) # 110010 Initialise
  set_byte(0x06,LCD_CMD) # 000110 Cursor move direction
  set_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off
  set_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
  set_byte(0x01,LCD_CMD) # 000001 Clear display

  display("Pico Started", 1)
  display(config.APP_VERSION, 2)

  time.sleep(LCD_DELAY)

def set_byte(bits, mode):
  PinRS = Pin(LCD_RS, Pin.OUT)
  PinRS.value(mode)
  PinD4 = Pin(LCD_D4, Pin.OUT)
  PinD5 = Pin(LCD_D5, Pin.OUT)
  PinD6 = Pin(LCD_D6, Pin.OUT)
  PinD7 = Pin(LCD_D7, Pin.OUT)
  
  PinD4.value(0)
  PinD5.value(0)
  PinD6.value(0)
  PinD7.value(0)
  if bits&0x10==0x10:
    PinD4.value(1)
  if bits&0x20==0x20:
    PinD5.value(1)
  if bits&0x40==0x40:
    PinD6.value(1)
  if bits&0x80==0x80:
    PinD7.value(1)
 
  toggle_enable()
 
  PinD4.value(0)
  PinD5.value(0)
  PinD6.value(0)
  PinD7.value(0)
  if bits&0x01==0x01:
    PinD4.value(1)
  if bits&0x02==0x02:
    PinD5.value(1)
  if bits&0x04==0x04:
    PinD6.value(1)
  if bits&0x08==0x08:
    PinD7.value(1)
  toggle_enable()
 
def toggle_enable():
  PinE = Pin(LCD_E, Pin.OUT)
  time.sleep(LCD_DELAY)
  PinE.value(1)
  time.sleep(LCD_PULSE)
  PinE.value(0)
  time.sleep(LCD_DELAY)
 
def display(message, line):
  MESSAGE_SPACE = LCD_WIDTH-len(message)
  i=0
  while i<MESSAGE_SPACE:
    message = message + " "
    i+=1 

  start_byte = None
  if (line == 1):
    start_byte = LCD_LINE_1
  elif (line == 2):
    start_byte = LCD_LINE_2
  else:
    return

  set_byte(start_byte, LCD_CMD)
  for i in range(LCD_WIDTH):
    set_byte(ord(message[i]),LCD_CHR)
