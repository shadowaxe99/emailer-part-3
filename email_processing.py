```python
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these SCOPES, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def get_service():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    try:
        service = build('gmail', 'v1', credentials=creds)
    except Exception as e:
        print(e)
        return None

    return service

def list_emails(service):
    results = service.users().messages().list(userId='me').execute()
    messages = results.get('messages', [])

    if not messages:
        print('No new messages.')
    else:
        print('Messages:')
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            print(msg['snippet'])

def send_email(service, to, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = 'me'
    message['subject'] = subject
    raw_message = base64.urlsafe_b64encode(message.as_bytes())
    raw_message = raw_message.decode()
    body = {'raw': raw_message}
    try:
        message = (service.users().messages().send(userId='me', body=body).execute())
        print('Message Id: %s' % message['id'])
        return message
    except Exception as error:
        print('An error occurred: %s' % error)

def main():
    service = get_service()
    list_emails(service)
    send_email(service, 'test@example.com', 'Test', 'This is a test email')

if __name__ == '__main__':
    main()
```