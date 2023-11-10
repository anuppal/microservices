from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:Passw0rd#123@database-1.cjljs4a3o9y3.us-east-1.rds.amazonaws.com/database-1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.get_json()

    if 'username' not in data or 'password' not in data or 'email' not in data:
        return jsonify({'error': 'Username, password, and email are required'}), 400

    new_user = User(username=data['username'], password=data['password'], email=data['email'])

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201

@app.route('/update_user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)

    if user is None:
        return jsonify({'error': 'User not found'}), 404

    data = request.get_json()

    if 'username' in data:
        user.username = data['username']
    if 'password' in data:
        user.password = data['password']
    if 'email' in data:
        user.email = data['email']

    db.session.commit()

    return jsonify({'message': 'User updated successfully'}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    
    app.run(debug=True)
