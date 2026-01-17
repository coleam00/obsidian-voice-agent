# Kiro CLI Reference Guide

## Quick Start

### Installation

**macOS:**
```bash
curl -fsSL https://cli.kiro.dev/install | bash
```

**Linux (Ubuntu):**
```bash
# Download and install .deb package
wget https://desktop-release.q.us-east-1.amazonaws.com/latest/kiro-cli.deb
sudo dpkg -i kiro-cli.deb
sudo apt-get install -f
```

**Windows:**
1. Install Ubuntu through WSL (Windows Subsystem for Linux):
   - Open PowerShell as Administrator
   - Run: `wsl --install`
   - Restart computer when prompted
   - Ubuntu will be installed automatically
2. Once Ubuntu is set up, use the Linux installation method above

### Authentication
```bash
# Authenticate (opens browser)
kiro-cli login

# Start chatting
kiro-cli
```

**Authentication Options:**
- AWS Builder ID (individual developers)
- AWS IAM Identity Center (enterprise)

### First Steps
```bash
# Basic chat
kiro-cli

# Start with specific agent
kiro-cli --agent my-agent

# Resume previous conversation
/chat resume

# Non-interactive mode
kiro-cli "List files in current directory"
```

## Core Components

### 1. Models & Selection

**Available Models:**
- **Auto** (recommended): Smart routing, 23% cheaper than Sonnet 4, best value
- **Claude Haiku 4.5**: Fastest, near-frontier intelligence at 1/3 cost
- **Claude Sonnet 4.0/4.5**: Consistent behavior, advanced coding
- **Claude Opus 4.5**: Maximum intelligence for complex tasks

**Model Management:**
```bash
# Switch models in chat
/model

# Set default model
/model set-current-as-default

# Via settings
kiro-cli settings chat.defaultModel claude-sonnet-4
```

### 2. Steering (Project Knowledge)

**Steering provides persistent project context through markdown files.**

**Locations:**
- Global: `~/.kiro/steering/`
- Project: `.kiro/steering/`

**Foundational Files:**
- `product.md`: Product overview, goals, users
- `tech.md`: Technology stack, frameworks, constraints
- `structure.md`: File organization, naming conventions

**Custom Steering Examples:**
- `api-standards.md`: REST conventions, error formats
- `testing-standards.md`: Unit test patterns, coverage
- `security-policies.md`: Authentication, validation rules

### 3. Prompts System

**Prompt Types:**
- **Local**: Project-specific (`.kiro/prompts/`)
- **Global**: User-wide (`~/.kiro/prompts/`)
- **MCP**: From MCP servers with arguments

**Prompt Commands:**
```bash
# List prompts
/prompts list

# Create prompt
/prompts create --name code-review --content "Review this code for..."

# Use prompts
@code-review
@mcp-server/analyze "performance" "detailed"
```

**Argument Handling for Local/Global Prompts:**
Since Kiro CLI local and global prompts don't support native argument passing (unlike MCP server prompts), prompts that require arguments must:

1. **Check for missing arguments** when invoked
2. **Ask the user to provide them** if not specified
3. **Use the arguments** once provided

Example prompt behavior:
```
User: @plan-feature
Assistant: I need to know what feature to plan. Please specify the feature name or description.
User: User authentication system
Assistant: [Proceeds with planning the user authentication system]
```

This ensures all argument-dependent prompts work correctly even without native argument support.

### 4. MCP (Model Context Protocol)

**MCP enables external tools and services integration.**

**Configuration Locations:**
- Global: `~/.kiro/settings/mcp.json`
- Project: `.kiro/settings/mcp.json`

**MCP Configuration:**
```json
{
  "mcpServers": {
    "aws-docs": {
      "command": "uvx",
      "args": ["awslabs.aws-documentation-mcp-server@latest"],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      }
    },
    "git": {
      "command": "git-mcp-server",
      "args": []
    }
  }
}
```

**MCP Commands:**
```bash
# Add MCP server
kiro-cli mcp add --name my-server --command "node server.js"

# List servers
/mcp

# View server status
kiro-cli mcp status --name my-server
```

### 5. Custom Agents

**Agent Structure:**
```json
{
  "name": "my-agent",
  "description": "Specialized agent for my workflow",
  "prompt": "You are an expert in...",
  "tools": ["read", "write", "shell", "@git"],
  "allowedTools": ["read", "@git/status"],
  "resources": ["file://README.md"],
  "model": "claude-sonnet-4"
}
```

**Agent Management:**
```bash
# Create agent interactively
/agent generate

# List agents
/agent list

# Switch agents
/agent swap my-agent

# Set default agent
kiro-cli settings chat.defaultAgent my-agent
```

**Agent Locations:**
- Global: `~/.kiro/agents/`
- Project: `.kiro/agents/`

### 6. Context Management

**Three Context Approaches:**

| Approach | Context Impact | Persistence | Best For |
|----------|---------------|-------------|----------|
| Agent Resources | Always active | Persistent | Essential files, standards |
| Session Context | Always active | Current session | Temporary files |
| Knowledge Bases | Only when searched | Persistent | Large codebases, docs |

**Context Commands:**
```bash
# View context usage
/context show

# Add temporary context
/context add README.md
/context add "src/**/*.py"

# Remove context
/context remove src/temp.py
/context clear
```

**Agent Resources (Persistent):**
```json
{
  "resources": [
    "file://README.md",
    "file://.kiro/steering/**/*.md",
    "file://docs/**/*.md"
  ]
}
```

### 7. Hooks (Automation)

**Hooks execute commands at specific lifecycle points.**

```json
{
  "hooks": {
    "agentSpawn": [
      {"command": "git status"}
    ],
    "preToolUse": [
      {
        "matcher": "shell",
        "command": "echo 'Executing: ' && cat"
      }
    ],
    "postToolUse": [
      {
        "matcher": "write",
        "command": "cargo fmt --all"
      }
    ]
  }
}
```

**Hook Types:**
- `agentSpawn`: When agent starts
- `userPromptSubmit`: When user sends message
- `preToolUse`: Before tool execution (can block)
- `postToolUse`: After tool execution
- `stop`: When assistant finishes

## Essential Slash Commands

### Core Commands
```bash
/help                    # Show available commands
/quit                    # Exit chat
/clear                   # Clear conversation display

# Context Management
/context show            # View context usage
/context add file.py     # Add temporary context
/context remove file.py  # Remove context

# Model & Agent Management
/model                   # Switch models
/agent list              # List available agents
/agent swap my-agent     # Switch to agent

# Session Management
/chat resume             # Resume previous session
/save /path/file.json    # Save conversation
/load /path/file.json    # Load conversation
```

### Advanced Commands
```bash
# Tool Management
/tools                   # View tool permissions
/tools trust write       # Trust tool for session
/tools trust-all         # Trust all tools (use carefully)

# Prompt Management
/prompts list            # List available prompts
/prompts create my-prompt # Create new prompt
@my-prompt               # Use prompt

# Code Intelligence
/code init               # Initialize LSP servers
/code status             # Check LSP status

# Experimental Features
/experiment              # Toggle experimental features
/tangent                 # Enter/exit tangent mode
/todo view               # View TODO lists
/checkpoint list         # View checkpoints
```

## Built-in Tools

### File Operations
- `read`: Read files, directories, images
- `write`: Create and modify files
- `glob`: Find files by pattern (respects .gitignore)
- `grep`: Search file contents with regex

### Execution
- `shell`: Execute bash commands
- `aws`: Make AWS CLI calls
- `use_subagent`: Delegate to specialized subagents

### Web & Research
- `web_search`: Search the internet
- `web_fetch`: Fetch content from URLs
- `introspect`: Get Kiro CLI help and documentation

### Experimental Tools
- `knowledge`: Persistent knowledge base with semantic search
- `thinking`: Show AI reasoning process
- `todo`: Create and manage TODO lists

## Configuration & Settings

### Key Settings
```bash
# Enable experimental features
kiro-cli settings chat.enableKnowledge true
kiro-cli settings chat.enableTangentMode true
kiro-cli settings chat.enableThinking true
kiro-cli settings chat.enableCheckpoint true

# Configure defaults
kiro-cli settings chat.defaultModel auto
kiro-cli settings chat.defaultAgent my-agent

# Knowledge base settings
kiro-cli settings knowledge.indexType Fast  # or Best
kiro-cli settings knowledge.maxFiles 10000
```

### Configuration Hierarchy
1. **Agent Config** (highest priority)
2. **Project Config** (`.kiro/`)
3. **Global Config** (`~/.kiro/`)

## Experimental Features

### Knowledge Management
```bash
# Enable and use
kiro-cli settings chat.enableKnowledge true
/knowledge add --name "project-docs" --path ./docs --index-type Best
/knowledge show
```

### Tangent Mode
```bash
# Enable and use
kiro-cli settings chat.enableTangentMode true
/tangent  # or Ctrl+T
# Explore side topics without disrupting main conversation
/tangent  # Return to main conversation
```

### Checkpointing
```bash
# Enable and use
kiro-cli settings chat.enableCheckpoint true
/checkpoint list
/checkpoint diff 1 2
/checkpoint restore 1
```

### Subagents
```bash
# Use subagents for parallel task execution
> Use the backend agent to refactor the payment module
# Kiro automatically spawns specialized subagent
```

## Best Practices

### Agent Design
1. **Start restrictive**: Minimal tool access, expand as needed
2. **Use descriptive names**: Clear purpose indication
3. **Organize by workflow**: Different agents for different tasks
4. **Version control**: Store local agents in project repository

### Context Management
1. **Essential files in agent resources**: README, configs, standards
2. **Large datasets in knowledge bases**: Semantic search without context consumption
3. **Temporary files in session context**: Current task files only
4. **Monitor usage**: Use `/context show` to track consumption

### Security
1. **Review tool permissions**: Understand what agents can do
2. **Use specific patterns**: Avoid wildcards in `allowedTools`
3. **Configure tool settings**: Restrict paths and commands
4. **Test in safe environments**: Try new agents on non-critical projects

### Workflow Integration
1. **Plan Agent**: Use `Shift+Tab` for complex task planning
2. **Subagents**: Delegate independent subtasks
3. **Tangent Mode**: Explore alternatives without losing context
4. **Checkpointing**: Track progress and enable experimentation

## Common Workflows

### Setting Up a New Project
```bash
# 1. Initialize in project directory
cd my-project
kiro-cli

# 2. Create project agent
/agent generate
# Follow prompts to configure tools, resources, MCP servers

# 3. Set up steering
mkdir -p .kiro/steering
# Create product.md, tech.md, structure.md

# 4. Configure context
# Add essential files to agent resources

# 5. Enable features as needed
/experiment  # Enable experimental features
```

### Code Review Workflow
```bash
# 1. Create specialized agent
{
  "name": "code-reviewer",
  "tools": ["read", "shell"],
  "allowedTools": ["read"],
  "resources": ["file://CONTRIBUTING.md", "file://docs/coding-standards.md"],
  "prompt": "You are a code review specialist..."
}

# 2. Use for reviews
kiro-cli --agent code-reviewer
> Review the changes in the latest commit
```

### AWS Infrastructure Management
```bash
# 1. Create AWS specialist agent
{
  "name": "aws-specialist",
  "tools": ["read", "write", "aws"],
  "allowedTools": ["read", "aws"],
  "toolsSettings": {
    "aws": {
      "allowedServices": ["s3", "lambda", "cloudformation"]
    }
  }
}

# 2. Use for AWS tasks
kiro-cli --agent aws-specialist
> Deploy the CloudFormation stack in staging
```

## Troubleshooting

### Common Issues
1. **Agent not found**: Check agent file location and JSON syntax
2. **Tool permissions**: Review `allowedTools` and `toolsSettings`
3. **Context not loading**: Verify file paths and glob patterns
4. **MCP servers failing**: Check command paths and environment variables

### Debugging Commands
```bash
kiro-cli doctor           # Diagnose common issues
kiro-cli settings list    # View current configuration
/tools                    # Check tool permissions
/context show             # View context usage
/mcp                      # Check MCP server status
```

### Getting Help
```bash
/help                     # In-chat help
kiro-cli --help           # CLI help
/issue                    # Report bugs or request features
```

---

This guide covers the essential components and workflows for effective Kiro CLI usage. Start with the Quick Start section, then explore the components relevant to your workflow. Use the experimental features to enhance productivity, and refer to the troubleshooting section when needed.
