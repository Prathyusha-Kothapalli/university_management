# UniSphere AI - Web Frontend

This is the React + TypeScript web frontend application for UniSphere AI.

## Project Structure

```text
web/
├── src/
│   ├── components/  # Shared reusable UI components
│   ├── pages/       # Top-level page views
│   ├── layouts/     # Application layout wrappers
│   ├── features/    # Feature-based modular slices
│   ├── hooks/       # Custom React hooks
│   ├── services/    # API & HTTP services
│   ├── types/       # TypeScript interfaces and types
│   ├── utils/       # Utility functions & helpers
│   ├── routes/      # Application routing definitions
│   ├── App.tsx      # Main application component
│   └── main.tsx     # Application entry point
├── public/          # Static assets
├── package.json     # Node dependencies & scripts
├── tsconfig.json    # TypeScript configuration
├── vite.config.ts   # Vite bundler configuration
└── README.md        # Web documentation
```

## Running Locally

1. Install dependencies:
   ```bash
   npm install
   ```

2. Start the development server:
   ```bash
   npm run dev
   ```

3. Open your browser at `http://localhost:3000`.
