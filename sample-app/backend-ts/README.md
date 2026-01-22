# Backend TypeScript Sample Application

A simple REST API for the GitHub Copilot Bootcamp. This application contains intentional TODOs for participants to complete using Copilot.

## Overview

This is a simple task management API with user authentication. Some features are incomplete - marked with TODO comments for bootcamp exercises.

## Features

- User registration and authentication
- Task CRUD operations
- Task filtering and sorting
- User profile management

## Tech Stack

- Node.js with TypeScript
- Express.js
- In-memory data store (for simplicity)
- JWT authentication

## Setup

```bash
cd sample-app/backend-ts
npm install
npm run dev
```

## Available Scripts

- `npm run dev` - Start development server with hot reload
- `npm run build` - Build for production
- `npm start` - Start production server
- `npm test` - Run tests
- `npm run lint` - Lint code

## API Endpoints

### Authentication

- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login user
- `POST /api/auth/logout` - Logout user (TODO)

### Tasks

- `GET /api/tasks` - Get all tasks (with filtering)
- `GET /api/tasks/:id` - Get task by ID
- `POST /api/tasks` - Create new task
- `PUT /api/tasks/:id` - Update task (TODO)
- `DELETE /api/tasks/:id` - Delete task (TODO)

### Users

- `GET /api/users/me` - Get current user profile
- `PUT /api/users/me` - Update profile (TODO)

## TODOs for Bootcamp

Throughout the codebase, you'll find TODO comments marking incomplete features:

### Week 1: Basic Setup
- Complete user registration validation
- Implement proper error responses

### Week 2: Features & Security
- Implement update task endpoint
- Implement delete task endpoint
- Add input sanitization
- Implement rate limiting

### Week 3: Testing & DevOps
- Add unit tests for services
- Add integration tests for API
- Create GitHub Actions workflow

### Week 4: Refactoring
- Refactor authentication logic
- Improve error handling
- Add request logging

## Project Structure

```
backend-ts/
├── src/
│   ├── controllers/    # Request handlers
│   ├── middleware/     # Express middleware
│   ├── models/         # Data models
│   ├── routes/         # API routes
│   ├── services/       # Business logic
│   ├── types/          # TypeScript types
│   ├── utils/          # Utility functions
│   └── index.ts        # Application entry point
├── tests/              # Test files
├── package.json
├── tsconfig.json
└── README.md
```

## Environment Variables

Create a `.env` file:

```env
PORT=3000
JWT_SECRET=your-secret-key-change-in-production
NODE_ENV=development
```

## Using with Copilot

This application is designed for learning with GitHub Copilot:

1. Read the TODO comments
2. Use Copilot to generate implementations
3. Review and test the generated code
4. Iterate and improve

## Next Steps

1. Complete the TODOs using Copilot
2. Add comprehensive tests
3. Implement additional features:
   - Task categories
   - Task priorities
   - Due dates and reminders
   - Task sharing between users

## License

MIT License - For educational purposes
