from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated user data (in-memory storage for simplicity)
users = []

# User model (should be stored in a database in a real-world scenario)
class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    if not username or not password or not email:
        return jsonify({'error': 'Username, password, and email are required'}), 400

    if any(user.username == username for user in users):
        return jsonify({'error': 'Username already exists'}), 400

    new_user = User(username, password, email)
    users.append(new_user)

    return jsonify({'message': 'User registered successfully'}), 201

# Route for user login (simple password-based authentication)
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = next((user for user in users if user.username == username), None)

    if user and user.password == password:
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'error': 'Invalid username or password'}), 401

if __name__ == '__main__':
    app.run(debug=True)
