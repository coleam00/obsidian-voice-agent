# CodeMentor AI - Intelligent Code Review Assistant

CodeMentor AI is an autonomous code review assistant that analyzes pull requests, provides detailed feedback, and suggests improvements using advanced AI models. Built with Kiro CLI for streamlined development workflows and intelligent automation.

## Prerequisites

- Python 3.11+
- Node.js 18+ (for frontend)
- Docker and Docker Compose
- Git
- Kiro CLI installed and authenticated

## Quick Start

1. **Clone and setup**
   ```bash
   git clone https://github.com/username/codementor-ai
   cd codementor-ai
   pip install -r requirements.txt
   npm install
   ```

2. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

3. **Run the application**
   ```bash
   docker-compose up -d
   python app.py
   ```

4. **Access the interface**
   - Web UI: http://localhost:3000
   - API: http://localhost:8000/docs

## Architecture & Codebase Overview

### System Architecture
- **Backend**: FastAPI with async processing
- **Frontend**: React with TypeScript
- **AI Engine**: OpenAI GPT-4 + Claude integration
- **Database**: PostgreSQL with Redis caching
- **Queue**: Celery for background tasks

### Directory Structure
```
codementor-ai/
├── backend/
│   ├── api/           # FastAPI routes
│   ├── services/      # Business logic
│   └── models/        # Database models
├── frontend/
│   ├── src/components/
│   └── src/pages/
├── .kiro/
│   ├── steering/      # Project guidelines
│   └── prompts/       # Custom Kiro commands
└── docker-compose.yml
```

### Key Components
- **Review Engine** (`backend/services/review.py`): Core AI analysis logic
- **GitHub Integration** (`backend/api/webhooks.py`): PR event handling
- **Dashboard** (`frontend/src/pages/Dashboard.tsx`): Main user interface
- **Custom Kiro Prompts** (`.kiro/prompts/`): Development automation

## Deep Dive

### AI Review Process
1. **Code Analysis**: Parses diff and identifies changed files
2. **Context Building**: Gathers relevant codebase context
3. **AI Processing**: Sends structured prompts to AI models
4. **Result Synthesis**: Combines multiple AI responses
5. **Feedback Generation**: Creates actionable review comments

### Kiro CLI Integration
- **Custom Prompts**: `@review-pr`, `@analyze-code`, `@suggest-tests`
- **Steering Documents**: Define code standards and review criteria
- **Automated Workflows**: Pre-commit hooks and CI integration

### Performance Optimizations
- **Caching**: Redis for API responses and AI results
- **Async Processing**: Background queue for large PRs
- **Rate Limiting**: Intelligent API usage management

## Troubleshooting

### Common Issues

**AI responses are slow**
- Check API key limits and quotas
- Verify Redis is running: `docker-compose ps`
- Monitor queue status: `celery -A app.celery inspect active`

**GitHub webhook not triggering**
- Verify webhook URL in repository settings
- Check ngrok tunnel if developing locally
- Review webhook payload in GitHub settings

**Database connection errors**
- Ensure PostgreSQL is running: `docker-compose up postgres`
- Check connection string in `.env`
- Run migrations: `python manage.py migrate`

**Frontend build fails**
- Clear node modules: `rm -rf node_modules && npm install`
- Check Node.js version: `node --version` (requires 18+)
- Verify environment variables in `.env`

### Getting Help
- Check logs: `docker-compose logs -f`
- Review Kiro CLI documentation: `kiro-cli --help`
- Open an issue on GitHub with error details
