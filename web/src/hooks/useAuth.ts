import { useContext } from 'react';
<<<<<<< HEAD
import { AuthContext } from '../context/AuthContext';

export const useAuth = () => {
=======
import { AuthContext, AuthContextType } from '../context/AuthContext';

export function useAuth(): AuthContextType {
>>>>>>> origin/web
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
<<<<<<< HEAD
};
=======
}
>>>>>>> origin/web
