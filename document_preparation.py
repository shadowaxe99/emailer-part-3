```python
import sqlite3
from flask import Flask, request, render_template

app = Flask(__name__)

def connect_db():
    return sqlite3.connect('user_data.db')

@app.route('/create_document', methods=['POST'])
def create_document():
    db = connect_db()
    cursor = db.cursor()
    user_id = request.form['user_id']
    document_content = request.form['document_content']
    cursor.execute("INSERT INTO documents (user_id, content) VALUES (?, ?)", (user_id, document_content))
    db.commit()
    return 'Document created successfully', 200

@app.route('/edit_document', methods=['POST'])
def edit_document():
    db = connect_db()
    cursor = db.cursor()
    document_id = request.form['document_id']
    new_content = request.form['new_content']
    cursor.execute("UPDATE documents SET content = ? WHERE id = ?", (new_content, document_id))
    db.commit()
    return 'Document updated successfully', 200

@app.route('/get_document', methods=['GET'])
def get_document():
    db = connect_db()
    cursor = db.cursor()
    document_id = request.args.get('document_id')
    cursor.execute("SELECT content FROM documents WHERE id = ?", (document_id,))
    document_content = cursor.fetchone()
    return render_template('document_view.html', document_content=document_content)

if __name__ == '__main__':
    app.run(debug=True)
```