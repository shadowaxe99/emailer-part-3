```python
from flask import Flask, render_template, request, session
import json

app = Flask(__name__)

@app.route('/')
def dashboard():
    user_data = session.get('user_data', {})
    return render_template('dashboard.html', user_data=user_data)

@app.route('/theme', methods=['POST'])
def set_theme():
    theme_data = request.json
    session['theme_data'] = theme_data
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

@app.route('/calendar')
def calendar_view():
    return render_template('calendar.html')

@app.route('/email')
def email_view():
    return render_template('email.html')

@app.route('/tasks')
def task_view():
    return render_template('tasks.html')

@app.route('/expenses')
def expense_view():
    return render_template('expenses.html')

@app.route('/documents')
def document_view():
    return render_template('documents.html')

@app.route('/research')
def research_view():
    return render_template('research.html')

@app.route('/events')
def event_view():
    return render_template('events.html')

if __name__ == '__main__':
    app.run(debug=True)
```