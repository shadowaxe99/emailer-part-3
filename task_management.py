```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    deadline = db.Column(db.DateTime, nullable=False)
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'Task {self.title}'

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = Task(title=data['title'], description=data['description'], deadline=datetime.strptime(data['deadline'], '%Y-%m-%d %H:%M:%S'))
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'message': 'New task created!'}), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify({'tasks': [task.title for task in tasks]})

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    task = Task.query.get(task_id)
    if 'title' in data:
        task.title = data['title']
    if 'description' in data:
        task.description = data['description']
    if 'deadline' in data:
        task.deadline = datetime.strptime(data['deadline'], '%Y-%m-%d %H:%M:%S')
    if 'completed' in data:
        task.completed = data['completed']
    db.session.commit()
    return jsonify({'message': 'Task updated!'})

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted!'})

if __name__ == '__main__':
    app.run(debug=True)
```