from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:Passw0rd#123@database-1.cjljs4a3o9y3.us-east-1.rds.amazonaws.com/database-1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Simulated user data (in-memory storage for simplicity)
# users = []

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)


# @app.route('/tasks', methods=['POST'])
# def create_task():
#     data = request.get_json()

#     if 'title' not in data:
#         return jsonify({'error': 'Title is required'}), 400

#     title = data['title']
#     new_task = Task(title=title)

#     db.session.add(new_task)
#     db.session.commit()

#     return jsonify({'message': 'Task created successfully'}), 201


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
    # users.append(new_user)
    Task.append(new_user)

    db.session.add(username,password,email)
    db.session.commit()

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
    
    db.session.add(username,password)
    db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
    # db.create_all()
