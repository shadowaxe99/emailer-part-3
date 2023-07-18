```python
from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Load theme data from a JSON file (or any other source)
with open('theme_data.json') as json_file:
    themes = json.load(json_file)

@app.route('/change_theme', methods=['POST'])
def change_theme():
    user_id = request.form.get('user_id')
    theme_name = request.form.get('theme_name')

    if theme_name not in themes:
        return "Invalid theme name", 400

    # Update the user's theme in the database
    # This is a placeholder, replace with actual database update code
    # db.execute("UPDATE users SET theme = ? WHERE id = ?", (theme_name, user_id))

    return "Theme updated successfully", 200

@app.route('/get_theme', methods=['GET'])
def get_theme():
    user_id = request.args.get('user_id')

    # Get the user's theme from the database
    # This is a placeholder, replace with actual database query code
    # theme = db.execute("SELECT theme FROM users WHERE id = ?", (user_id,)).fetchone()

    if theme is None:
        return "User not found", 404

    return themes[theme], 200

if __name__ == "__main__":
    app.run(debug=True)
```