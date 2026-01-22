export interface User {
  id: string;
  email: string;
  password: string; // Hashed
  name: string;
  createdAt: Date;
}

export interface Task {
  id: string;
  userId: string;
  title: string;
  description?: string;
  completed: boolean;
  createdAt: Date;
  updatedAt: Date;
}

export interface AuthRequest extends Express.Request {
  user?: {
    id: string;
    email: string;
  };
}
