import React, { useState } from 'react';
import { Card, CardHeader, CardTitle, CardDescription, CardContent } from '../../components/ui/Card';
import { Input } from '../../components/ui/Input';
import { Button } from '../../components/ui/Button';
import { Mail, ArrowLeft, CheckCircle2 } from 'lucide-react';
import { Link } from 'react-router-dom';
import { authService } from '../../services/authService';

export const ForgotPassword: React.FC = () => {
  const [email, setEmail] = useState('');
  const [submitted, setSubmitted] = useState(false);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!email) return;
    setLoading(true);
    await authService.forgotPassword(email);
    setLoading(false);
    setSubmitted(true);
  };

  return (
    <Card className="glass-panel border-slate-700/80 shadow-2xl">
      <CardHeader className="text-center pb-2">
        <CardTitle className="justify-center text-xl font-bold">Reset Password</CardTitle>
        <CardDescription>Enter your email to receive recovery instructions</CardDescription>
      </CardHeader>

      <CardContent className="space-y-4">
        {submitted ? (
          <div className="p-4 rounded-xl bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 text-xs text-center space-y-2">
            <CheckCircle2 className="w-8 h-8 mx-auto text-emerald-400" />
            <p className="font-semibold text-sm">Recovery Email Sent</p>
            <p className="text-slate-300">
              We have dispatched a password recovery link to <span className="font-mono">{email}</span>.
            </p>
          </div>
        ) : (
          <form onSubmit={handleSubmit} className="space-y-4">
            <Input
              label="Registered Email"
              type="email"
              placeholder="user@collexa.com"
              icon={<Mail className="w-4 h-4" />}
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
            <Button type="submit" className="w-full h-10 text-sm font-semibold" isLoading={loading}>
              SEND RESET INSTRUCTIONS
            </Button>
          </form>
        )}

        <div className="pt-3 text-center">
          <Link
            to="/login"
            className="text-xs text-slate-400 hover:text-sky-400 inline-flex items-center gap-1.5 transition-colors"
          >
            <ArrowLeft className="w-3.5 h-3.5" /> Back to Login
          </Link>
        </div>
      </CardContent>
    </Card>
  );
};
