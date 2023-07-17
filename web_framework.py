```python
from flask import Flask, render_template, request, redirect, url_for, session
import backend_logic
import email_processing
import calendar_integration
import sms_notifications
import meeting_creation
import database_management
import calendar_management
import travel_arrangement
import expense_reporting
import document_preparation
import communication_management
import task_management
import research_tools
import event_planning
import dashboard
import themes
import performance_optimization

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('dashboard.html')

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/email')
def email():
    return render_template('email.html')

@app.route('/tasks')
def tasks():
    return render_template('tasks.html')

@app.route('/expenses')
def expenses():
    return render_template('expenses.html')

@app.route('/documents')
def documents():
    return render_template('documents.html')

@app.route('/research')
def research():
    return render_template('research.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

if __name__ == '__main__':
    app.run(debug=True)
```