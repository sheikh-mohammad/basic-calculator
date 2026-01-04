# Sample Vercel Configuration Files

## Basic vercel.json for Static Site
```json
{
  "version": 2,
  "public": true,
  "builds": [
    {
      "src": "**/*",
      "use": "@vercel/static"
    }
  ],
  "routes": [
    {
      "src": "/api/(.*)",
      "dest": "/api/index.js"
    },
    {
      "src": "/(.*)",
      "dest": "/index.html"
    }
  ]
}
```

## vercel.json for HTML/CSS/JS Calculator App
```json
{
  "version": 2,
  "public": true,
  "builds": [
    {
      "src": "package.json",
      "use": "@vercel/static-build",
      "config": {
        "distDir": "dist"
      }
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "/index.html"
    }
  ]
}
```

## vercel.json for Python Backend + Frontend Calculator
```json
{
  "version": 2,
  "public": false,
  "builds": [
    {
      "src": "api/**/*.py",
      "use": "@vercel/python"
    },
    {
      "src": "package.json",
      "use": "@vercel/static-build",
      "config": {
        "distDir": "public"
      }
    }
  ],
  "routes": [
    {
      "src": "/api/(.*)",
      "dest": "/api/index.py"
    },
    {
      "src": "/(.*)",
      "dest": "/index.html"
    }
  ]
}
```

## Deployment Scripts

### Deploy to Vercel Script
```bash
#!/bin/bash

# Deploy to Vercel with error handling
set -e

echo "Starting Vercel deployment..."

# Check if vercel CLI is installed
if ! command -v vercel &> /dev/null; then
    echo "Vercel CLI not found. Installing..."
    npm install -g vercel
fi

# Login to Vercel (optional, for private projects)
# vercel login

# Deploy to production
echo "Deploying to production..."
vercel --prod --force

echo "Deployment completed successfully!"
```

### Local Development Script
```bash
#!/bin/bash

# Test Vercel deployment locally
set -e

echo "Starting local Vercel development server..."

# Check if vercel CLI is installed
if ! command -v vercel &> /dev/null; then
    echo "Vercel CLI not found. Installing..."
    npm install -g vercel
fi

# Start local development server
vercel dev
```

## Environment Configuration

### .env.example for Vercel Environment Variables
```
# API Keys
API_KEY=your_api_key_here

# Database Configuration
DATABASE_URL=your_database_url_here

# Other Environment Variables
NODE_ENV=production
DEBUG=false
```

### vercel.json with Environment Variables
```json
{
  "version": 2,
  "public": true,
  "builds": [
    {
      "src": "package.json",
      "use": "@vercel/static-build",
      "config": {
        "distDir": "build"
      }
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "/index.html"
    }
  ],
  "env": {
    "NODE_ENV": "production",
    "DEBUG": "false"
  }
}
```