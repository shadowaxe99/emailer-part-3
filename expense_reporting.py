```python
import sqlite3
from flask import Flask, request, jsonify
from database_management import get_db_connection

app = Flask(__name__)

@app.route('/expense', methods=['POST'])
def create_expense():
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (user_id, category, amount, receipt) VALUES (?, ?, ?, ?)",
                   (data['user_id'], data['category'], data['amount'], data['receipt']))
    conn.commit()
    return jsonify({"status": "success", "message": "Expense created successfully"}), 201

@app.route('/expense', methods=['GET'])
def get_expenses():
    user_id = request.args.get('user_id')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses WHERE user_id = ?", (user_id,))
    expenses = cursor.fetchall()
    return jsonify({"status": "success", "data": expenses}), 200

@app.route('/expense/report', methods=['POST'])
def create_expense_report():
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expense_reports (user_id, expenses, total_amount, status) VALUES (?, ?, ?, ?)",
                   (data['user_id'], data['expenses'], data['total_amount'], 'Pending'))
    conn.commit()
    return jsonify({"status": "success", "message": "Expense report created successfully"}), 201

@app.route('/expense/report', methods=['GET'])
def get_expense_reports():
    user_id = request.args.get('user_id')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expense_reports WHERE user_id = ?", (user_id,))
    expense_reports = cursor.fetchall()
    return jsonify({"status": "success", "data": expense_reports}), 200

if __name__ == '__main__':
    app.run(debug=True)
```