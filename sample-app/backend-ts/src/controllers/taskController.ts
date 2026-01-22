import { Response } from 'express';
import { AuthRequest, Task } from '../types';
import { tasks } from '../models/data';

export const getTasks = (req: AuthRequest, res: Response) => {
  try {
    const userId = req.user?.id;

    if (!userId) {
      return res.status(401).json({ error: 'Unauthorized' });
    }

    // Get user's tasks
    const userTasks = tasks.filter((t) => t.userId === userId);

    // TODO: Add filtering and sorting
    // - Filter by completed status (?completed=true/false)
    // - Sort by date, title (?sort=createdAt,-title)
    // - Pagination (?page=1&limit=10)
    // - Search by title/description (?search=keyword)

    res.json({ tasks: userTasks });
  } catch (error) {
    console.error('Get tasks error:', error);
    res.status(500).json({ error: 'Failed to get tasks' });
  }
};

export const getTaskById = (req: AuthRequest, res: Response) => {
  try {
    const { id } = req.params;
    const userId = req.user?.id;

    if (!userId) {
      return res.status(401).json({ error: 'Unauthorized' });
    }

    const task = tasks.find((t) => t.id === id && t.userId === userId);

    if (!task) {
      return res.status(404).json({ error: 'Task not found' });
    }

    res.json({ task });
  } catch (error) {
    console.error('Get task error:', error);
    res.status(500).json({ error: 'Failed to get task' });
  }
};

export const createTask = (req: AuthRequest, res: Response) => {
  try {
    const { title, description } = req.body;
    const userId = req.user?.id;

    if (!userId) {
      return res.status(401).json({ error: 'Unauthorized' });
    }

    // TODO: Add input validation
    // - Title required, max length 200
    // - Description optional, max length 1000
    // - Sanitize inputs to prevent XSS

    if (!title) {
      return res.status(400).json({ error: 'Title is required' });
    }

    const task: Task = {
      id: Date.now().toString(),
      userId,
      title,
      description,
      completed: false,
      createdAt: new Date(),
      updatedAt: new Date(),
    };

    tasks.push(task);

    res.status(201).json({
      message: 'Task created successfully',
      task,
    });
  } catch (error) {
    console.error('Create task error:', error);
    res.status(500).json({ error: 'Failed to create task' });
  }
};

export const updateTask = (req: AuthRequest, res: Response) => {
  // TODO: Implement task update
  // - Validate task ownership
  // - Allow updating: title, description, completed
  // - Update updatedAt timestamp
  // - Return updated task

  res.status(501).json({ error: 'Not implemented yet' });
};

export const deleteTask = (req: AuthRequest, res: Response) => {
  // TODO: Implement task deletion
  // - Validate task ownership
  // - Remove task from array
  // - Return success message

  res.status(501).json({ error: 'Not implemented yet' });
};
