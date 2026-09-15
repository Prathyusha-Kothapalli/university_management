import React, { useState } from 'react';
import { Card } from '../../components/Card';
import { Button } from '../../components/Button';
import { Building, DoorOpen, Users, Accessibility, Layers, Plus } from 'lucide-react';

interface BuildingItem {
  id: string;
  name: string;
  code: string;
  floors: number;
  capacity: number;
  hasElevator: boolean;
  accessible: boolean;
}

export const CampusManagerPage: React.FC = () => {
  const [buildings, setBuildings] = useState<BuildingItem[]>([
    { id: '1', name: 'Alan Turing Science Complex', code: 'SC', floors: 6, capacity: 1200, hasElevator: true, accessible: true },
    { id: '2', name: 'Ada Lovelace Engineering Block', code: 'EB', floors: 5, capacity: 950, hasElevator: true, accessible: true },
    { id: '3', name: 'Main Academic Quad', code: 'AQ', floors: 4, capacity: 1500, hasElevator: false, accessible: true },
    { id: '4', name: 'Biotech Innovation Labs', code: 'IL', floors: 3, capacity: 450, hasElevator: true, accessible: true },
  ]);

  return (
    <div style={{ padding: '2rem', maxWidth: '1200px', margin: '0 auto' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem' }}>
        <div>
          <h1 style={{ fontSize: '1.8rem', fontWeight: 800, color: '#f8fafc', margin: 0 }}>
            Campus Buildings & Facility Management
          </h1>
          <p style={{ color: '#94a3b8', margin: '4px 0 0 0', fontSize: '0.9rem' }}>
            Manage campus building structures, lecture hall allocations, and accessibility specs.
          </p>
        </div>
        <Button variant="primary">
          <Plus size={16} style={{ marginRight: '6px' }} /> Add Campus Building
        </Button>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))', gap: '1.25rem' }}>
        {buildings.map((bld) => (
          <Card
            key={bld.id}
            style={{
              padding: '1.25rem',
              backgroundColor: 'rgba(15, 23, 42, 0.6)',
              border: '1px solid rgba(255, 255, 255, 0.08)',
              borderRadius: '16px',
            }}
          >
            <div style={{ display: 'flex', alignItems: 'center', gap: '12px', marginBottom: '1rem' }}>
              <div
                style={{
                  width: '42px',
                  height: '42px',
                  borderRadius: '12px',
                  backgroundColor: 'rgba(37, 99, 235, 0.15)',
                  color: '#38bdf8',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  fontWeight: 800,
                }}
              >
                {bld.code}
              </div>
              <div>
                <h3 style={{ margin: 0, fontSize: '1rem', color: '#f8fafc', fontWeight: 700 }}>{bld.name}</h3>
                <span style={{ fontSize: '0.75rem', color: '#94a3b8' }}>Code: {bld.code}</span>
              </div>
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '0.75rem', padding: '10px 0', borderTop: '1px solid rgba(255,255,255,0.06)', borderBottom: '1px solid rgba(255,255,255,0.06)', marginBottom: '1rem', fontSize: '0.8rem', color: '#cbd5e1' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                <Layers size={14} color="#94a3b8" /> {bld.floors} Floors
              </div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                <Users size={14} color="#94a3b8" /> Cap: {bld.capacity}
              </div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                <DoorOpen size={14} color="#94a3b8" /> {bld.hasElevator ? 'Elevator' : 'Stairs'}
              </div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                <Accessibility size={14} color="#10b981" /> Accessible
              </div>
            </div>

            <Button variant="outline" size="sm" style={{ width: '100%' }}>
              Manage Classrooms & Labs
            </Button>
          </Card>
        ))}
      </div>
    </div>
  );
};
