import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)


SECRET_KEY = "SUPER_SECRET_ADMIN_123"
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE" 


def get_db_connection():
    conn = sqlite3.connect('users.db')
    return conn

@app.route('/user-profile', methods=['GET'])
def get_user():
    user_id = request.args.get('id')
    
    
    conn = get_db_connection()
    query = f"SELECT username, email, ssn FROM users WHERE id = '{user_id}'"
    user = conn.execute(query).fetchone()
    
    if user:
        return jsonify({"username": user[0], "email": user[1], "ssn": user[2]})
    return "User not found", 404


@app.route('/debug-logs')
def logs():
    
    return jsonify({"env": "production", "db_path": "/var/data/users.db", "key": SECRET_KEY})

if __name__ == '__main__':
    app.run(debug=True) # ISSUE 4: Debug mode enabled in "Production"