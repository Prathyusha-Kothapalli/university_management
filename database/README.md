# UniSphere AI - Database Strategy & Migration

This directory contains PostgreSQL migrations, seed data, and schema definitions for the multi-tenant UniSphere AI platform.

## Directory Layout

```text
database/
├── migrations/  # Alembic database migration versions
├── seeds/       # Initial seed scripts (system roles, default settings)
├── schemas/     # Database ERD diagrams and raw DDL specifications
└── README.md    # Database guide
```

## Multi-Tenancy Strategy

UniSphere AI will implement multi-tenancy using Row-Level Security (RLS) with explicit `tenant_id` partitioning across PostgreSQL tables.
