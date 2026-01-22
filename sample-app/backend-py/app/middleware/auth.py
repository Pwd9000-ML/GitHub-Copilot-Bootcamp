from functools import wraps
from flask import request, jsonify
import jwt
import os

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        auth_header = request.headers.get('Authorization')
        
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header[7:]
        
        if not token:
            return jsonify({'error': 'Token is missing'}), 401
        
        try:
            # TODO: Add proper token validation
            # - Check token expiration
            # - Verify token signature
            # - Handle malformed tokens
            
            secret_key = os.getenv('JWT_SECRET_KEY', 'jwt-secret')
            data = jwt.decode(token, secret_key, algorithms=['HS256'])
            current_user_id = data['user_id']
        except Exception as e:
            return jsonify({'error': 'Token is invalid'}), 401
        
        return f(current_user_id, *args, **kwargs)
    
    return decorated
