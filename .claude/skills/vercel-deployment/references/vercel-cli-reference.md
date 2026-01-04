# Vercel CLI Deployment References

## Installation and Setup

### Installing Vercel CLI
The Vercel CLI can be installed using npm or yarn:

```bash
# Using npm
npm install -g vercel

# Using yarn
yarn global add vercel

# Using Homebrew (macOS)
brew tap vercel/vercel
brew install vercel
```

### Verifying Installation
```bash
# Check version
vercel --version

# Get help
vercel --help
```

## Authentication Methods

### Interactive Login
```bash
# Login with email verification
vercel login
```

### Token Authentication (for CI/CD)
```bash
# Login and generate token
vercel login

# Use token for authentication
vercel --token <your-token-here>

# Set token as environment variable
export VERCEL_TOKEN=<your-token-here>
```

## Project Linking and Setup

### Linking to Existing Project
```bash
# Link current directory to existing Vercel project
vercel link

# Create new project
vercel
```

### Project Configuration
```bash
# Pull project settings
vercel pull

# Inspect current project configuration
vercel inspect
```

## Advanced Configuration

### vercel.json Examples

#### Basic Static Site
```json
{
  "version": 2,
  "public": true,
  "builds": [
    {
      "src": "**/*",
      "use": "@vercel/static"
    }
  ]
}
```

#### Custom Build Configuration
```json
{
  "version": 2,
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

#### Multiple Frameworks
```json
{
  "version": 2,
  "builds": [
    {
      "src": "api/**/*.js",
      "use": "@vercel/node"
    },
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
      "src": "/api/(.*)",
      "dest": "/api/$1.js"
    },
    {
      "src": "/(.*)",
      "dest": "/index.html"
    }
  ]
}
```

## Environment Variables

### Setting Environment Variables
```bash
# Add environment variables for production
vercel env add NAME production

# Add environment variables for preview deployments
vercel env add NAME preview

# Add environment variables for all environments
vercel env add NAME development,preview,production
```

### Environment Variable File
```bash
# Pull environment variables to local file
vercel env pull .env.local
```

## Deployment Commands

### Production Deployment
```bash
# Deploy to production
vercel --prod

# Deploy with specific name
vercel --name my-app --prod
```

### Preview Deployment
```bash
# Deploy to preview URL
vercel

# Deploy without building (if already built)
vercel --prebuilt
```

### Deployment Aliases
```bash
# Deploy with custom domain
vercel --alias my-app.com

# Deploy with multiple aliases
vercel --alias my-app.com --alias www.my-app.com
```

## Framework-Specific Configurations

### Next.js
```json
{
  "version": 2,
  "builds": [
    {
      "src": "package.json",
      "use": "@vercel/next"
    }
  ]
}
```

### React
```json
{
  "version": 2,
  "builds": [
    {
      "src": "package.json",
      "use": "@vercel/static-build",
      "config": {
        "distDir": "build"
      }
    }
  ]
}
```

### Vue.js
```json
{
  "version": 2,
  "builds": [
    {
      "src": "package.json",
      "use": "@vercel/static-build",
      "config": {
        "distDir": "dist"
      }
    }
  ]
}
```

## Monitoring and Logs

### Accessing Logs
```bash
# View logs for specific deployment
vercel logs my-app.vercel.app

# View logs for specific deployment URL
vercel logs https://my-app-git-branch-user.vercel.app
```

### Deployment Management
```bash
# List all deployments
vercel ls

# Remove deployments
vercel rm <deployment-id>

# Inspect deployment details
vercel inspect
```

## Custom Domains

### Adding Custom Domain
```bash
# Add domain to project
vercel domains add my-app.com

# List domains
vercel domains ls
```

### DNS Configuration
```bash
# Get DNS configuration
vercel domains inspect my-app.com
```

## Rollbacks and Promotions

### Promoting Deployments
```bash
# Promote preview deployment to production
vercel promote <deployment-id>
```

### Rollback Deployments
```bash
# Rollback to previous deployment
vercel rollback
```