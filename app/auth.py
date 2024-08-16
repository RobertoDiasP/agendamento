from flask import Blueprint, request, jsonify
from .models import User
from . import db, jwt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

auth_blueprint = Blueprint('auth', __name__)


@auth_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    # Verifica se o usuário já existe
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'Email already registered'}), 400

    user = User(username=data['username'], email=data['email'])
    user.password = data['password']
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201


@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user and user.check_password(data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    return jsonify({'message': 'Invalid credentials'}), 401
