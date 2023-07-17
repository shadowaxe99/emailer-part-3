```python
import os
from zoomus import ZoomClient

# Get API keys from environment variables
ZOOM_API_KEY = os.getenv('ZOOM_API_KEY')
ZOOM_API_SECRET = os.getenv('ZOOM_API_SECRET')

# Initialize Zoom client
client = ZoomClient(ZOOM_API_KEY, ZOOM_API_SECRET)

def create_meeting(topic, start_time, duration, timezone='UTC'):
    """
    Function to create a Zoom meeting.
    """
    meeting_info = client.meeting.create(
        user_id='me',
        topic=topic,
        type=2,
        start_time=start_time,
        duration=duration,
        timezone=timezone
    )
    return meeting_info

def list_meetings():
    """
    Function to list all Zoom meetings.
    """
    meetings = client.meeting.list(user_id='me')
    return meetings

def get_meeting(meeting_id):
    """
    Function to get details of a specific Zoom meeting.
    """
    meeting_info = client.meeting.get(id=meeting_id)
    return meeting_info

def update_meeting(meeting_id, topic, start_time, duration, timezone='UTC'):
    """
    Function to update a Zoom meeting.
    """
    meeting_info = client.meeting.update(
        id=meeting_id,
        topic=topic,
        type=2,
        start_time=start_time,
        duration=duration,
        timezone=timezone
    )
    return meeting_info

def delete_meeting(meeting_id):
    """
    Function to delete a Zoom meeting.
    """
    response = client.meeting.delete(id=meeting_id)
    return response
```