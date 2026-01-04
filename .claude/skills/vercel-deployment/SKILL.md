---
name: vercel-deployment
description: This skill should be used when deploying web applications to Vercel using the Vercel CLI, including setup, configuration, and deployment workflows.
---

# Vercel Deployment Automation

Automates the deployment of web applications to Vercel using the Vercel CLI, including setup, configuration, and deployment workflows.

## Core Deployment Concepts

### Vercel CLI
- Command-line interface for interacting with Vercel platform
- Enables deployment management, log retrieval, and configuration
- Works with various frameworks and build tools

### Deployment Workflow
- Local development and testing
- Configuration with vercel.json
- Authentication and project linking
- Deployment to Vercel's global edge network

## Before Implementation

Gather context to ensure successful implementation:

| Source | Gather |
|--------|--------|
| **Codebase** | Project structure, framework used, build configuration to integrate with |
| **Conversation** | User's specific deployment requirements, environment preferences, domain needs |
| **Skill References** | Vercel CLI commands, configuration options, best practices |
| **User Guidelines** | Project-specific conventions, team standards, security requirements |

Ensure all required context is gathered before implementing.

## Implementation Standards

### Prerequisites
- Node.js installed (required for Vercel CLI)
- Vercel account created
- Project ready for deployment (buildable and tested)

### Installation
- Install Vercel CLI globally using npm or yarn
- Verify installation with version check
- Set up authentication for private projects

### Configuration
- Create vercel.json for custom configuration
- Set environment variables as needed
- Configure build settings and routing rules

## Vercel CLI Commands

### Installation
```bash
# Install Vercel CLI globally
npm install -g vercel

# Verify installation
vercel --version
```

### Authentication
```bash
# Login to Vercel account
vercel login

# For CI/CD environments, use token authentication
vercel --token <your-token>
```

### Project Setup
```bash
# Initialize a new project or link to existing
vercel

# Link to existing Vercel project
vercel link
```

### Local Development
```bash
# Test deployment locally
vercel dev
```

### Deployment
```bash
# Deploy to production
vercel

# Deploy to preview/staging environment
vercel --prebuilt

# Deploy with specific settings
vercel --prod  # Force production deployment
```

### Management Commands
```bash
# View deployment logs
vercel logs <deployment-url>

# List deployments
vercel ls

# Pull environment variables
vercel env pull .env.local
```

## Configuration Files

### vercel.json
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
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "/index.html"
    }
  ],
  "github": {
    "enabled": true
  }
}
```

### Common Configuration Options
- `version`: Specify the configuration version (2 is current)
- `builds`: Define how your project should be built
- `routes`: Define URL routing rules
- `functions`: Configure serverless functions
- `headers`: Set custom HTTP headers
- `redirects`: Set up URL redirects
- `rewrites`: Configure URL rewrites

## Deployment Workflow

1. **Prerequisites Check**
   - Verify Node.js is installed
   - Confirm Vercel account exists
   - Ensure project builds successfully locally

2. **Install Vercel CLI**
   - Install globally using npm
   - Verify installation with version check

3. **Authenticate**
   - Login to Vercel account
   - For CI/CD, use token authentication

4. **Project Configuration**
   - Create vercel.json if needed
   - Set environment variables
   - Configure build settings

5. **Deploy**
   - Run vercel command to deploy
   - Confirm deployment settings
   - Verify successful deployment

6. **Post-Deployment**
   - Test deployed application
   - Configure custom domains if needed
   - Set up monitoring and analytics

## Output Specifications

### Deployment Structure
```
project/
├── vercel.json          # Vercel configuration
├── package.json         # Project dependencies
├── public/              # Static assets (if applicable)
└── dist/                # Build output directory
```

### Quality Checklist
- [ ] Vercel CLI installed and verified
- [ ] Authentication completed
- [ ] vercel.json configured properly
- [ ] Project builds successfully locally
- [ ] Environment variables set if needed
- [ ] Deployment successful and accessible
- [ ] Custom domain configured (if applicable)

## Common Deployment Scenarios

### Static Site Deployment
- Simple HTML/CSS/JS projects
- Frameworks like React, Vue, Angular builds
- JAMstack applications

### Framework-Specific Deployment
- Next.js: Automatic configuration
- Nuxt.js: Framework-specific settings
- Gatsby: Static site generation
- SvelteKit: Modern web application framework

### Environment Management
- Development: Local testing with vercel dev
- Preview: Pull requests and feature branches
- Production: Main branch deployments

## Troubleshooting

### Common Issues
- Build failures: Check build logs and dependencies
- Environment variables: Ensure properly set in Vercel dashboard
- Custom domains: Verify DNS configuration
- Routing: Check vercel.json routing rules

### Debugging Commands
```bash
# View detailed logs
vercel logs <deployment-url>

# Test locally
vercel dev

# Check project configuration
vercel inspect
```