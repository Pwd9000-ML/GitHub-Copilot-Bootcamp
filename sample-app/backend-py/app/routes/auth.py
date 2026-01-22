from flask import Blueprint, request, jsonify
import bcrypt
import jwt
import os
from datetime import datetime, timedelta
from app.models.data import users

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        name = data.get('name')
        
        # TODO: Add comprehensive input validation
        # - Email format validation
        # - Password strength requirements (min 8 chars, uppercase, number)
        # - Name validation (required, min/max length)
        # - Sanitize inputs to prevent XSS
        
        if not email or not password or not name:
            return jsonify({'error': 'All fields are required'}), 400
        
        # Check if user already exists
        if any(u['email'] == email for u in users):
            return jsonify({'error': 'User already exists'}), 400
        
        # Hash password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        # Create user
        user = {
            'id': str(len(users) + 1),
            'email': email,
            'password': hashed_password,
            'name': name,
            'created_at': datetime.now().isoformat()
        }
        
        users.append(user)
        
        # Generate token
        secret_key = os.getenv('JWT_SECRET_KEY', 'jwt-secret')
        token = jwt.encode({
            'user_id': user['id'],
            'email': user['email'],
            'exp': datetime.utcnow() + timedelta(days=7)
        }, secret_key, algorithm='HS256')
        
        return jsonify({
            'message': 'User registered successfully',
            'token': token,
            'user': {
                'id': user['id'],
                'email': user['email'],
                'name': user['name']
            }
        }), 201
        
    except Exception as e:
        print(f'Registration error: {e}')
        return jsonify({'error': 'Registration failed'}), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        
        # TODO: Add input validation
        # - Email format validation
        # - Rate limiting to prevent brute force attacks
        
        if not email or not password:
            return jsonify({'error': 'Email and password are required'}), 400
        
        # Find user
        user = next((u for u in users if u['email'] == email), None)
        
        if not user:
            return jsonify({'error': 'Invalid credentials'}), 401
        
        # Verify password
        if not bcrypt.checkpw(password.encode('utf-8'), user['password']):
            return jsonify({'error': 'Invalid credentials'}), 401
        
        # Generate token
        secret_key = os.getenv('JWT_SECRET_KEY', 'jwt-secret')
        token = jwt.encode({
            'user_id': user['id'],
            'email': user['email'],
            'exp': datetime.utcnow() + timedelta(days=7)
        }, secret_key, algorithm='HS256')
        
        return jsonify({
            'message': 'Login successful',
            'token': token,
            'user': {
                'id': user['id'],
                'email': user['email'],
                'name': user['name']
            }
        }), 200
        
    except Exception as e:
        print(f'Login error: {e}')
        return jsonify({'error': 'Login failed'}), 500
