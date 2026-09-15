import React, { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import { User, Tenant, AuthResponse, RegisterTenantData, RegisterUserData } from '../../types/auth';
import { api } from '../../services/api';

interface AuthContextType {
  user: User | null;
  tenant: Tenant | null;
  token: string | null;
  isLoading: boolean;
  error: string | null;
  login: (email: string, password: string, tenantCode?: string) => Promise<void>;
  registerTenant: (data: RegisterTenantData) => Promise<void>;
  registerUser: (data: RegisterUserData) => Promise<User>;
  logout: () => void;
  clearError: () => void;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);
  const [tenant, setTenant] = useState<Tenant | null>(null);
  const [token, setToken] = useState<string | null>(localStorage.getItem('unisphere_token'));
  const [isLoading, setIsLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const initializeAuth = async () => {
      const storedToken = localStorage.getItem('unisphere_token');
      if (storedToken) {
        try {
          const currentUser = await api.getCurrentUser();
          setUser(currentUser);
          if (currentUser.tenant) {
            setTenant(currentUser.tenant);
          }
        } catch (err: any) {
          console.error('Session validation error:', err);
          logout();
        }
      }
      setIsLoading(false);
    };

    initializeAuth();
  }, []);

  const handleAuthSuccess = (data: AuthResponse) => {
    localStorage.setItem('unisphere_token', data.access_token);
    setToken(data.access_token);
    setUser(data.user);
    if (data.user.tenant) {
      setTenant(data.user.tenant);
    }
    setError(null);
  };

  const login = async (email: string, password: string, tenantCode?: string) => {
    setIsLoading(true);
    setError(null);
    try {
      const data = await api.login(email, password, tenantCode);
      handleAuthSuccess(data);
    } catch (err: any) {
      setError(err.message || 'Login failed. Please check your credentials.');
      throw err;
    } finally {
      setIsLoading(false);
    }
  };

  const registerTenant = async (data: RegisterTenantData) => {
    setIsLoading(true);
    setError(null);
    try {
      const authData = await api.registerTenant(data);
      handleAuthSuccess(authData);
    } catch (err: any) {
      setError(err.message || 'University onboarding failed.');
      throw err;
    } finally {
      setIsLoading(false);
    }
  };

  const registerUser = async (data: RegisterUserData): Promise<User> => {
    try {
      const newUser = await api.registerUser(data);
      return newUser;
    } catch (err: any) {
      throw new Error(err.message || 'Failed to register user.');
    }
  };

  const logout = () => {
    localStorage.removeItem('unisphere_token');
    setToken(null);
    setUser(null);
    setTenant(null);
    setError(null);
  };

  const clearError = () => setError(null);

  return (
    <AuthContext.Provider
      value={{
        user,
        tenant,
        token,
        isLoading,
        error,
        login,
        registerTenant,
        registerUser,
        logout,
        clearError,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = (): AuthContextType => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};

