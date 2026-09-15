import { AuthResponse, Tenant, User, RegisterTenantData, RegisterUserData, UserRole } from '../types/auth';

const getApiBaseUrls = (): string[] => {
  const customUrl = (import.meta as any).env?.VITE_API_URL;
  if (customUrl) return [customUrl];
  
  if (typeof window !== 'undefined') {
    const host = window.location.hostname || '127.0.0.1';
    const primary = `http://${host}:5000/api/v1`;
    const fallback = host === '127.0.0.1' ? 'http://localhost:5000/api/v1' : 'http://127.0.0.1:5000/api/v1';
    return [primary, fallback];
  }
  return ['http://127.0.0.1:5000/api/v1', 'http://localhost:5000/api/v1'];
};

class ApiService {
  private getToken(): string | null {
    return localStorage.getItem('unisphere_token');
  }

  private getHeaders(customHeaders: Record<string, string> = {}): Record<string, string> {
    const headers: Record<string, string> = {
      'Content-Type': 'application/json',
      ...customHeaders,
    };
    const token = this.getToken();
    if (token) {
      headers['Authorization'] = `Bearer ${token}`;
    }
    return headers;
  }

  private async request<T>(endpoint: string, options: RequestInit = {}): Promise<T> {
    const baseUrls = getApiBaseUrls();
    let lastError: any = null;

    for (const baseUrl of baseUrls) {
      try {
        const url = `${baseUrl}${endpoint}`;
        const response = await fetch(url, {
          ...options,
          headers: this.getHeaders(options.headers as Record<string, string>),
        });

        if (!response.ok) {
          let errorMessage = `HTTP Error ${response.status}`;
          try {
            const errorData = await response.json();
            errorMessage = errorData.detail || errorData.message || errorMessage;
          } catch {
            // use default error message
          }
          throw new Error(errorMessage);
        }

        if (response.status === 204) {
          return {} as T;
        }

        return await response.json();
      } catch (err: any) {
        lastError = err;
        // If it's an HTTP error with a response message, don't fallback across hosts
        if (err.message && !err.message.includes('Failed to fetch') && !err.message.includes('NetworkError') && !err.message.includes('Load failed')) {
          throw err;
        }
      }
    }

    throw lastError || new Error('Unable to connect to backend server. Please verify port 5000.');
  }

  // Auth Endpoints
  async login(email: string, password: string, tenantCode?: string): Promise<AuthResponse> {
    return this.request<AuthResponse>('/auth/login', {
      method: 'POST',
      body: JSON.stringify({ email, password, tenant_code: tenantCode || undefined }),
    });
  }

  async registerTenant(data: RegisterTenantData): Promise<AuthResponse> {
    return this.request<AuthResponse>('/auth/register-tenant', {
      method: 'POST',
      body: JSON.stringify(data),
    });
  }

  async registerUser(data: RegisterUserData): Promise<User> {
    return this.request<User>('/auth/register-user', {
      method: 'POST',
      body: JSON.stringify(data),
    });
  }

  async getCurrentUser(): Promise<User> {
    return this.request<User>('/auth/me');
  }

  // Tenants Endpoints
  async getTenants(): Promise<Tenant[]> {
    return this.request<Tenant[]>('/tenants');
  }

  async getTenant(id: string): Promise<Tenant> {
    return this.request<Tenant>(`/tenants/${id}`);
  }

  async createTenant(data: { name: string; code: string; domain?: string; description?: string }): Promise<Tenant> {
    return this.request<Tenant>('/tenants', {
      method: 'POST',
      body: JSON.stringify(data),
    });
  }

  // Users Endpoints
  async getUsers(params?: { tenant_id?: string; role?: UserRole }): Promise<User[]> {
    const query = new URLSearchParams();
    if (params?.tenant_id) query.append('tenant_id', params.tenant_id);
    if (params?.role) query.append('role', params.role);
    const queryString = query.toString() ? `?${query.toString()}` : '';
    return this.request<User[]>(`/users${queryString}`);
  }

  async deleteUser(userId: string): Promise<void> {
    return this.request<void>(`/users/${userId}`, {
      method: 'DELETE',
    });
  }
}

export const api = new ApiService();
