import { Response } from 'express';
import { AuthRequest } from '../types';
import { users } from '../models/data';

export const getProfile = (req: AuthRequest, res: Response) => {
  try {
    const userId = req.user?.id;

    if (!userId) {
      return res.status(401).json({ error: 'Unauthorized' });
    }

    const user = users.find((u) => u.id === userId);

    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }

    res.json({
      user: {
        id: user.id,
        email: user.email,
        name: user.name,
        createdAt: user.createdAt,
      },
    });
  } catch (error) {
    console.error('Get profile error:', error);
    res.status(500).json({ error: 'Failed to get profile' });
  }
};

export const updateProfile = (req: AuthRequest, res: Response) => {
  // TODO: Implement profile update
  // - Allow updating: name, email (with verification)
  // - Validate inputs
  // - Check if new email is already taken
  // - Return updated profile

  res.status(501).json({ error: 'Not implemented yet' });
};
