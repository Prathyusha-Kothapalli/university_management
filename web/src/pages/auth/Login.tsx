import React, { useState } from 'react';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';
import { useAuth } from '../../hooks/useAuth';
import { useNavigate, Link } from 'react-router-dom';
import { Card, CardHeader, CardTitle, CardDescription, CardContent } from '../../components/ui/Card';
import { Input } from '../../components/ui/Input';
import { Button } from '../../components/ui/Button';
import { DEMO_USERS } from '../../services/authService';
import { Eye, EyeOff, Lock, Mail, Sparkles, ShieldAlert } from 'lucide-react';
import { Badge } from '../../components/ui/Badge';

const loginSchema = z.object({
  email: z.string().email('Please enter a valid email address'),
  password: z.string().min(6, 'Password must be at least 6 characters'),
  rememberMe: z.boolean().optional(),
});

type LoginFormData = z.infer<typeof loginSchema>;

export const Login: React.FC = () => {
  const { login, error } = useAuth();
  const navigate = useNavigate();
  const [showPassword, setShowPassword] = useState(false);
  const [formError, setFormError] = useState<string | null>(null);

  const {
    register,
    handleSubmit,
    setValue,
    formState: { errors, isSubmitting },
  } = useForm<LoginFormData>({
    resolver: zodResolver(loginSchema),
    defaultValues: {
      email: 'student@collexa.com',
      password: 'password123',
      rememberMe: true,
    },
  });

  const onSubmit = async (data: LoginFormData) => {
    setFormError(null);
    try {
      await login(data);
      // Determine dashboard based on persona
      const normalizedEmail = data.email.toLowerCase();
      const user = DEMO_USERS[normalizedEmail];
      const role = user?.role || 'STUDENT';

      switch (role) {
        case 'SUPER_ADMIN':
          navigate('/super-admin/dashboard');
          break;
        case 'MANAGEMENT':
          navigate('/management/dashboard');
          break;
        case 'PRINCIPAL':
          navigate('/principal/dashboard');
          break;
        case 'DEAN':
          navigate('/dean/dashboard');
          break;
        case 'HOD':
          navigate('/hod/dashboard');
          break;
        case 'FACULTY':
          navigate('/faculty/dashboard');
          break;
        case 'STUDENT':
          navigate('/student/dashboard');
          break;
        case 'PARENT':
          navigate('/parent/dashboard');
          break;
        case 'FINANCE':
          navigate('/finance/dashboard');
          break;
        case 'LMS_ADMIN':
          navigate('/lms/dashboard');
          break;
        case 'BI_ANALYST':
          navigate('/bi/dashboard');
          break;
        default:
          navigate('/student/dashboard');
          break;
      }
    } catch (err: any) {
      setFormError(err?.message || 'Invalid credentials');
    }
  };

  const handleSelectPersona = (email: string) => {
    setValue('email', email);
    setValue('password', 'password123');
  };

  return (
    <div className="space-y-6">
      <Card className="glass-panel border-slate-700/80 shadow-2xl">
        <CardHeader className="text-center pb-2">
          <CardTitle className="justify-center text-xl font-bold">Welcome Back</CardTitle>
          <CardDescription>Sign in to access your COLLEXA ERP workspace</CardDescription>
        </CardHeader>

        <CardContent className="space-y-5">
          {(formError || error) && (
            <div className="p-3 rounded-xl bg-rose-500/10 border border-rose-500/30 text-rose-400 text-xs flex items-start gap-2.5">
              <ShieldAlert className="w-4 h-4 shrink-0 mt-0.5" />
              <span>{formError || error}</span>
            </div>
          )}

          <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
            <Input
              label="Email Address"
              type="email"
              placeholder="Enter your email"
              icon={<Mail className="w-4 h-4" />}
              error={errors.email?.message}
              {...register('email')}
            />

            <div className="space-y-1.5">
              <label className="block text-xs font-medium text-slate-300">Password</label>
              <div className="relative">
                <div className="absolute left-3 top-3 text-slate-400 pointer-events-none">
                  <Lock className="w-4 h-4" />
                </div>
                <input
                  type={showPassword ? 'text' : 'password'}
                  placeholder="Enter your password"
                  className="flex h-10 w-full rounded-lg border border-slate-700/80 bg-slate-900/60 pl-9 pr-10 py-2 text-sm text-slate-100 placeholder:text-slate-500 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary transition-all"
                  {...register('password')}
                />
                <button
                  type="button"
                  onClick={() => setShowPassword(!showPassword)}
                  className="absolute right-3 top-2.5 text-slate-400 hover:text-white transition-colors"
                >
                  {showPassword ? <EyeOff className="w-4 h-4" /> : <Eye className="w-4 h-4" />}
                </button>
              </div>
              {errors.password && (
                <p className="text-xs text-rose-400 font-medium">{errors.password.message}</p>
              )}
            </div>

            <div className="flex items-center justify-between text-xs">
              <label className="flex items-center gap-2 text-slate-400 cursor-pointer">
                <input
                  type="checkbox"
                  className="rounded border-slate-700 bg-slate-900 text-sky-500 focus:ring-sky-500/50"
                  {...register('rememberMe')}
                />
                <span>Remember me</span>
              </label>
              <Link to="/forgot-password" className="text-sky-400 hover:underline">
                Forgot password?
              </Link>
            </div>

            <Button type="submit" className="w-full h-11 text-sm font-semibold" isLoading={isSubmitting}>
              SIGN IN TO ERP
            </Button>
          </form>

          {/* Quick Demo Persona Switcher */}
          <div className="pt-4 border-t border-slate-800 space-y-3">
            <div className="flex items-center justify-between">
              <span className="text-[11px] font-semibold text-slate-400 uppercase tracking-wider flex items-center gap-1">
                <Sparkles className="w-3 h-3 text-amber-400" /> Demo Personas Quick Select
              </span>
              <Badge variant="outline" className="text-[10px]">
                27 Roles Enabled
              </Badge>
            </div>

            <div className="grid grid-cols-2 gap-2 max-h-48 overflow-y-auto pr-1">
              {Object.entries(DEMO_USERS).map(([email, user]) => (
                <button
                  key={email}
                  type="button"
                  onClick={() => handleSelectPersona(email)}
                  className="p-2 rounded-lg bg-slate-900/80 hover:bg-sky-500/10 border border-slate-800 hover:border-sky-500/40 text-left transition-all group"
                >
                  <p className="text-xs font-semibold text-slate-200 group-hover:text-sky-400 truncate">
                    {user.name}
                  </p>
                  <span className="text-[10px] text-slate-500 uppercase tracking-tight block">
                    {user.role}
                  </span>
                </button>
              ))}
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  );
};
