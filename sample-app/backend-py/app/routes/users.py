from flask import Blueprint, request, jsonify
from app.middleware.auth import token_required
from app.models.data import users

users_bp = Blueprint('users', __name__)

@users_bp.route('/me', methods=['GET'])
@token_required
def get_profile(current_user_id):
    try:
        user = next((u for u in users if u['id'] == current_user_id), None)
        
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        return jsonify({
            'user': {
                'id': user['id'],
                'email': user['email'],
                'name': user['name'],
                'created_at': user['created_at']
            }
        }), 200
        
    except Exception as e:
        print(f'Get profile error: {e}')
        return jsonify({'error': 'Failed to get profile'}), 500

@users_bp.route('/me', methods=['PUT'])
@token_required
def update_profile(current_user_id):
    # TODO: Implement profile update
    # - Allow updating: name, email (with verification)
    # - Validate inputs
    # - Check if new email is already taken
    # - Return updated profile
    
    return jsonify({'error': 'Not implemented yet'}), 501
