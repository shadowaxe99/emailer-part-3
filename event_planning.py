```python
import sqlite3
from flask import Flask, request, jsonify
from googleapiclient.discovery import build

app = Flask(__name__)

# Database connection
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Google Calendar API setup
service = build('calendar', 'v3')

@app.route('/planEvent', methods=['POST'])
def plan_event():
    event_data = request.get_json()
    event_name = event_data['event_name']
    event_date = event_data['event_date']
    event_location = event_data['event_location']
    attendees = event_data['attendees']

    # Insert event into database
    c.execute("INSERT INTO events (event_name, event_date, event_location, attendees) VALUES (?, ?, ?, ?)",
              (event_name, event_date, event_location, attendees))
    conn.commit()

    # Create event in Google Calendar
    event = {
        'summary': event_name,
        'location': event_location,
        'start': {
            'dateTime': event_date,
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': event_date,
            'timeZone': 'America/Los_Angeles',
        },
        'attendees': [
            {'email': attendee} for attendee in attendees
        ],
    }

    event = service.events().insert(calendarId='primary', body=event).execute()

    return jsonify({'message': 'Event planned successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
```