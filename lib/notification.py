import urequests

from lib import secrets

def notify_subscribers(message):
  for name in secrets.SUBSCRIBERS:
    phone = secrets.SUBSCRIBERS[name]
    send_whatsapp(name, phone, message)

def send_whatsapp(recipient_name, recipient_phone_number, message):
  headers = {
    'Authorization': f'Bearer {secrets.FACEBOOK_SECRET}',
    'Content-Type': 'application/json',
  }

  json_data = {
    'messaging_product': 'whatsapp',
    'to': recipient_phone_number,
    'type': 'template',
    'template': {
      'name': 'notification',
      'language': {
        'code': 'en',
      },
      'components': [
        {
          'type': 'body',
          'parameters': [
            {
              'type': 'text',
              'text': recipient_name,
            },
            {
              'type': 'text',
              'text': message,
            },
          ],
        },
      ],
    },
  }

  urequests.post('https://graph.facebook.com/v17.0/105248422661328/messages', headers=headers, json=json_data)
