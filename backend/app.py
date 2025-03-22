from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1q2w3e@localhost/movie_reco'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50),unique=True ,nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'User {self.username}'

@app.route('/')
def home():
    return "Serverul Flask și baza de date funcționează!"

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/singup', methods=['POST'])
def singup():
    data = request.get_json()

    username = data.get['username']
    email = data.get['email']
    password = data.get['password']

    if not username or not email or not password:
        return jsonify(message="All the fields are required!"), 400
    
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify(message="That email is already taken!"), 400
    
    hashed_password = generate_password_hash(password, method='sha256')
    user = User(username=username, password=hashed_password)
    db.session.add(user)
    db.session.commit()
    return jsonify(message="User created successfully!"), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)