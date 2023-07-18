```python
from twilio.rest import Client
import os

# Your Account SID from twilio.com/console
account_sid = os.environ['TWILIO_ACCOUNT_SID']
# Your Auth Token from twilio.com/console
auth_token  = os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)

def send_sms(to, body):
    message = client.messages.create(
        to=to, 
        from_="+12345678901", # Your Twilio number
        body=body)

def new_email_notification(to, email_subject):
    body = f"You have a new email: {email_subject}"
    send_sms(to, body)

def new_event_notification(to, event_name):
    body = f"You have a new event: {event_name}"
    send_sms(to, body)

def task_update_notification(to, task_name):
    body = f"Task '{task_name}' has been updated."
    send_sms(to, body)

def expense_report_notification(to, report_id):
    body = f"Expense report '{report_id}' has been submitted."
    send_sms(to, body)

def travel_booking_notification(to, booking_id):
    body = f"Travel booking '{booking_id}' has been made."
    send_sms(to, body)

def document_update_notification(to, document_name):
    body = f"Document '{document_name}' has been updated."
    send_sms(to, body)
```