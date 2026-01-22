import { Router } from 'express';
import { authenticate } from '../middleware/auth';
import { getProfile, updateProfile } from '../controllers/userController';

const router = Router();

// All user routes require authentication
router.use(authenticate);

router.get('/me', getProfile);
router.put('/me', updateProfile); // TODO: Implement

export default router;
