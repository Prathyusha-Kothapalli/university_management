import React, { useState } from 'react';
import { Card, CardHeader, CardTitle, CardDescription, CardContent } from '../../components/ui/Card';
import { Input } from '../../components/ui/Input';
import { Button } from '../../components/ui/Button';
import { Lock, CheckCircle2 } from 'lucide-react';
import { useNavigate } from 'react-router-dom';
import { authService } from '../../services/authService';

export const ResetPassword: React.FC = () => {
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [success, setSuccess] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (password !== confirmPassword) {
      setError('Passwords do not match');
      return;
    }
    setLoading(true);
    try {
      await authService.resetPassword('mock-token', password);
      setSuccess(true);
      setTimeout(() => navigate('/login'), 2000);
    } catch {
      setError('Failed to update password');
    } finally {
      setLoading(false);
    }
  };

  return (
    <Card className="glass-panel border-slate-700/80 shadow-2xl">
      <CardHeader className="text-center pb-2">
        <CardTitle className="justify-center text-xl font-bold">New Password</CardTitle>
        <CardDescription>Enter your new secure password</CardDescription>
      </CardHeader>

      <CardContent className="space-y-4">
        {success ? (
          <div className="p-4 rounded-xl bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 text-xs text-center space-y-2">
            <CheckCircle2 className="w-8 h-8 mx-auto text-emerald-400" />
            <p className="font-semibold text-sm">Password Updated!</p>
            <p className="text-slate-300">Redirecting to login screen...</p>
          </div>
        ) : (
          <form onSubmit={handleSubmit} className="space-y-4">
            {error && <p className="text-xs text-rose-400 font-medium">{error}</p>}
            <Input
              label="New Password"
              type="password"
              placeholder="••••••••"
              icon={<Lock className="w-4 h-4" />}
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
            <Input
              label="Confirm New Password"
              type="password"
              placeholder="••••••••"
              icon={<Lock className="w-4 h-4" />}
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              required
            />
            <Button type="submit" className="w-full h-10 text-sm font-semibold" isLoading={loading}>
              UPDATE PASSWORD
            </Button>
          </form>
        )}
      </CardContent>
    </Card>
  );
};
