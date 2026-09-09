import React from 'react';
import { Card, CardContent } from '../ui/Card';
import { Badge } from '../ui/Badge';
import { ArrowUpRight, ArrowDownRight, AlertTriangle } from 'lucide-react';
import { cn } from '../../lib/utils';

export interface StatCardProps {
  title: string;
  value: string | number;
  change?: string;
  changeType?: 'positive' | 'negative' | 'neutral' | 'warning';
  description?: string;
  icon?: React.ReactNode;
  iconBg?: string;
  className?: string;
}

export const StatCard: React.FC<StatCardProps> = ({
  title,
  value,
  change,
  changeType = 'positive',
  description,
  icon,
  iconBg = 'bg-primary/10 text-primary',
  className,
}) => {
  return (
    <Card className={cn('glass-card-hover overflow-hidden relative', className)}>
      <CardContent className="p-5">
        <div className="flex items-center justify-between">
          <p className="text-xs font-medium text-slate-400 tracking-wide uppercase">{title}</p>
          {icon && (
            <div className={cn('p-2.5 rounded-xl flex items-center justify-center shadow-inner', iconBg)}>
              {icon}
            </div>
          )}
        </div>

        <div className="mt-3 flex items-baseline justify-between gap-2">
          <h4 className="text-2xl font-bold tracking-tight text-white">{value}</h4>
          {change && (
            <Badge
              variant={
                changeType === 'positive'
                  ? 'success'
                  : changeType === 'negative'
                  ? 'destructive'
                  : changeType === 'warning'
                  ? 'warning'
                  : 'outline'
              }
              className="gap-0.5 text-[10px] px-1.5 py-0.5"
            >
              {changeType === 'positive' && <ArrowUpRight className="w-3 h-3" />}
              {changeType === 'negative' && <ArrowDownRight className="w-3 h-3" />}
              {changeType === 'warning' && <AlertTriangle className="w-3 h-3" />}
              {change}
            </Badge>
          )}
        </div>

        {description && <p className="mt-2 text-xs text-slate-400">{description}</p>}
      </CardContent>
    </Card>
  );
};
