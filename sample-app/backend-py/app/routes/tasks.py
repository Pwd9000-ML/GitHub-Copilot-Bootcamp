from flask import Blueprint, request, jsonify
from datetime import datetime
from app.middleware.auth import token_required
from app.models.data import tasks

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/', methods=['GET'])
@token_required
def get_tasks(current_user_id):
    try:
        # Get user's tasks
        user_tasks = [t for t in tasks if t['user_id'] == current_user_id]
        
        # TODO: Add filtering and sorting
        # - Filter by completed status (?completed=true/false)
        # - Sort by date, title (?sort=created_at,-title)
        # - Pagination (?page=1&limit=10)
        # - Search by title/description (?search=keyword)
        
        return jsonify({'tasks': user_tasks}), 200
    except Exception as e:
        print(f'Get tasks error: {e}')
        return jsonify({'error': 'Failed to get tasks'}), 500

@tasks_bp.route('/<task_id>', methods=['GET'])
@token_required
def get_task_by_id(current_user_id, task_id):
    try:
        task = next((t for t in tasks if t['id'] == task_id and t['user_id'] == current_user_id), None)
        
        if not task:
            return jsonify({'error': 'Task not found'}), 404
        
        return jsonify({'task': task}), 200
    except Exception as e:
        print(f'Get task error: {e}')
        return jsonify({'error': 'Failed to get task'}), 500

@tasks_bp.route('/', methods=['POST'])
@token_required
def create_task(current_user_id):
    try:
        data = request.get_json()
        title = data.get('title')
        description = data.get('description', '')
        
        # TODO: Add input validation
        # - Title required, max length 200
        # - Description optional, max length 1000
        # - Sanitize inputs to prevent XSS
        
        if not title:
            return jsonify({'error': 'Title is required'}), 400
        
        task = {
            'id': str(len(tasks) + 1),
            'user_id': current_user_id,
            'title': title,
            'description': description,
            'completed': False,
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }
        
        tasks.append(task)
        
        return jsonify({
            'message': 'Task created successfully',
            'task': task
        }), 201
        
    except Exception as e:
        print(f'Create task error: {e}')
        return jsonify({'error': 'Failed to create task'}), 500

@tasks_bp.route('/<task_id>', methods=['PUT'])
@token_required
def update_task(current_user_id, task_id):
    # TODO: Implement task update
    # - Validate task ownership
    # - Allow updating: title, description, completed
    # - Update updated_at timestamp
    # - Return updated task
    
    return jsonify({'error': 'Not implemented yet'}), 501

@tasks_bp.route('/<task_id>', methods=['DELETE'])
@token_required
def delete_task(current_user_id, task_id):
    # TODO: Implement task deletion
    # - Validate task ownership
    # - Remove task from array
    # - Return success message
    
    return jsonify({'error': 'Not implemented yet'}), 501
