import { Router } from 'express';
import { register, login } from '../controllers/authController';

const router = Router();

router.post('/register', register);
router.post('/login', login);

// TODO: Add logout endpoint
// - Invalidate token
// - Clear session if using sessions

export default router;
