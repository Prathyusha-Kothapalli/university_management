import React from 'react';
import { BrowserRouter } from 'react-router-dom';
import { AuthProvider } from '../context/AuthContext';
import { QueryProvider } from './providers/QueryProvider';
import { AppRouter } from './router/AppRouter';

export const App: React.FC = () => {
  return (
    <QueryProvider>
      <AuthProvider>
        <BrowserRouter>
          <AppRouter />
        </BrowserRouter>
      </AuthProvider>
    </QueryProvider>
  );
};

export default App;
