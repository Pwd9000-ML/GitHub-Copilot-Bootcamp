# Backend Python Sample Application

A simple REST API for the GitHub Copilot Bootcamp (Python alternative). This application contains intentional TODOs for participants to complete using Copilot.

## Overview

This is a simple task management API with user authentication, built with Flask. Some features are incomplete - marked with TODO comments for bootcamp exercises.

## Features

- User registration and authentication
- Task CRUD operations
- Task filtering (TODO)
- User profile management

## Tech Stack

- Python 3.9+
- Flask
- In-memory data store (for simplicity)
- JWT authentication

## Setup

```bash
cd sample-app/backend-py
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

## Available Commands

- `python run.py` - Start development server
- `pytest` - Run tests
- `pylint app` - Lint code
- `black app` - Format code

## API Endpoints

### Authentication

- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login user

### Tasks

- `GET /api/tasks` - Get all tasks (with filtering)
- `GET /api/tasks/<id>` - Get task by ID
- `POST /api/tasks` - Create new task
- `PUT /api/tasks/<id>` - Update task (TODO)
- `DELETE /api/tasks/<id>` - Delete task (TODO)

### Users

- `GET /api/users/me` - Get current user profile
- `PUT /api/users/me` - Update profile (TODO)

## TODOs for Bootcamp

Throughout the codebase, you'll find TODO comments marking incomplete features.

## Project Structure

```
backend-py/
├── app/
│   ├── __init__.py          # Flask app initialization
│   ├── controllers/         # Request handlers
│   ├── middleware/          # Flask middleware
│   ├── models/              # Data models
│   └── routes/              # API routes
├── tests/                   # Test files
├── requirements.txt
├── run.py                   # Application entry point
└── README.md
```

## Environment Variables

Create a `.env` file:

```env
FLASK_ENV=development
SECRET_KEY=your-secret-key-change-in-production
JWT_SECRET_KEY=your-jwt-secret
```

## Using with Copilot

This application is designed for learning with GitHub Copilot:

1. Read the TODO comments
2. Use Copilot to generate implementations
3. Review and test the generated code
4. Iterate and improve

## License

MIT License - For educational purposes
