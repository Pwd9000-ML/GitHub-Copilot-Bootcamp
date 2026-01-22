import { Router } from 'express';
import { authenticate } from '../middleware/auth';
import {
  getTasks,
  getTaskById,
  createTask,
  updateTask,
  deleteTask,
} from '../controllers/taskController';

const router = Router();

// All task routes require authentication
router.use(authenticate);

router.get('/', getTasks);
router.get('/:id', getTaskById);
router.post('/', createTask);
router.put('/:id', updateTask); // TODO: Implement
router.delete('/:id', deleteTask); // TODO: Implement

export default router;
