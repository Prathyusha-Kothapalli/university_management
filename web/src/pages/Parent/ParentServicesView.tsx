import React from 'react';
import { LibrarySummary } from '../../components/dashboard/LibrarySummary';
import { HostelSummary } from '../../components/dashboard/HostelSummary';
import { TransportSummary } from '../../components/dashboard/TransportSummary';
import { PlacementSummary } from '../../components/dashboard/PlacementSummary';
import { DocumentSummary } from '../../components/dashboard/DocumentSummary';

export const ParentServicesView: React.FC = () => {
  return (
    <div style={{ padding: '1.75rem', display: 'flex', flexDirection: 'column', gap: '1.5rem', maxWidth: '1400px', margin: '0 auto' }}>
      <div>
        <h1 style={{ fontSize: '1.5rem', fontWeight: 800, color: '#f8fafc', margin: 0 }}>
          Campus Facilities, Services & Documents
        </h1>
        <p style={{ fontSize: '0.85rem', color: '#94a3b8', margin: '4px 0 0 0' }}>
          Library books, hostel room allocation, bus routes, placement drives, and student certificates
        </p>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1.5rem' }}>
        <LibrarySummary />
        <PlacementSummary />
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1.5rem' }}>
        <HostelSummary />
        <TransportSummary />
      </div>

      <DocumentSummary />
    </div>
  );
};
