import { Request, Response, NextFunction } from 'express';

export const errorHandler = (
  err: Error,
  req: Request,
  res: Response,
  next: NextFunction
) => {
  console.error('Error:', err);

  // TODO: Implement proper error handling with different error types
  // - ValidationError: 400
  // - AuthenticationError: 401
  // - AuthorizationError: 403
  // - NotFoundError: 404
  // - Generic errors: 500

  res.status(500).json({
    error: 'Internal Server Error',
    message: process.env.NODE_ENV === 'development' ? err.message : undefined,
  });
};
