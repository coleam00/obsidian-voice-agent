# Plan agent
The Plan agent is a specialized built-in agent that helps transform ideas into structured implementation plans. It guides you through requirements gathering, research, and creates detailed task breakdowns before switching to execution mode.
## Getting started[](https://kiro.dev/docs/cli/chat/planning-agent/#getting-started)
### Keyboard shortcut[](https://kiro.dev/docs/cli/chat/planning-agent/#keyboard-shortcut)
Press `Shift + Tab` to toggle between plan and execution modes.
### Slash command[](https://kiro.dev/docs/cli/chat/planning-agent/#slash-command)
bash
```

> /plan

Switched to the Kiro [plan] agent. Transform any idea into fully working code.
What do you want to build today?

[plan] >


```

### With immediate prompt[](https://kiro.dev/docs/cli/chat/planning-agent/#with-immediate-prompt)
bash
```

> /plan Build a REST API for user authentication


```

When active, you'll see:
  * `[plan]` indicator in your prompt
  * Welcome message when switching modes


## Plan workflow[](https://kiro.dev/docs/cli/chat/planning-agent/#plan-workflow)
### 1. Requirements gathering[](https://kiro.dev/docs/cli/chat/planning-agent/#1-requirements-gathering)
The planner guides you through structured questions to refine your initial idea.
bash
```

[plan] > I want to build a todo app

I understand you want to build a todo app. Let me help you plan this
implementation.

**My Understanding:** You want to create a todo application for managing tasks.

Let me gather some requirements to create a detailed plan:

[1]: What platform should this todo app target?
a. **Web Application** - Browser-based with HTML/CSS/JavaScript
b. **Mobile App** - Native iOS/Android or cross-platform
c. **Desktop App** - Electron, Tauri, or native desktop
d. **CLI Tool** - Command-line interface
e. **Other** - Provide your own answer

[2]: What's the primary use case for this todo app?
a. **Personal Task Management** - Individual productivity
b. **Team Collaboration** - Shared tasks and assignments
c. **Project Management** - Complex workflows with dependencies
d. **Other** - Describe your specific needs

(Use the chat to answer any subset: eg., "1=a, 2=b" or provide your own answers)


```

Feature | Description  
---|---  
Structured questions | Clear, numbered questions with multiple choice options  
Flexible responses | Answer individual questions or provide custom responses  
Iterative process | Builds understanding through multiple rounds of questions  
Context awareness | Adapts follow-up questions based on your answers  
### 2. Research and analysis[](https://kiro.dev/docs/cli/chat/planning-agent/#2-research-and-analysis)
The planner explores your codebase and researches relevant technologies.
Capability | Description  
---|---  
Code exploration | Uses code, grep, and glob tools to understand existing code  
Technology research | Identifies relevant frameworks, libraries, and patterns  
Architecture analysis | Reviews existing project structure and conventions  
### 3. Implementation plan[](https://kiro.dev/docs/cli/chat/planning-agent/#3-implementation-plan)
Creates a detailed, step-by-step implementation plan with clear objectives.
bash
```

**Implementation Plan - Todo CLI Command**

**Problem Statement:** Add todo management to existing Kiro CLI for task tracking.

**Requirements:**
- CLI commands for CRUD operations
- Local SQLite storage
- Priority and due date support

**Task Breakdown:**

Task 1: Create database schema and models
- Define Todo struct with required fields
- Create database migration for todos table
- Demo: Can create and query todos in database

Task 2: Implement CLI command structure
- Add todo subcommand with add/list/complete operations
- Demo: CLI accepts todo commands and shows help

Task 3: Add advanced features
- Implement due dates and priority sorting
- Demo: Complete todo system with all features


```

Each task includes:
  * **Clear objectives** - Specific, measurable goals
  * **Implementation guidance** - General approach and key considerations
  * **Demo description** - Working functionality that can be demonstrated


### 4. Plan approval and handoff[](https://kiro.dev/docs/cli/chat/planning-agent/#4-plan-approval-and-handoff)
Before switching to execution, the planner seeks your approval.
bash
```

[plan] > Does this plan look good, or would you like me to adjust anything?

> The plan looks great! Let's implement it.

*Planning complete!* Ready to exit [plan] agent to start your implementation? [y/n]:

> y


```

The handoff process:
  1. You approve the implementation plan
  2. Interactive prompt confirms switching to execution
  3. Automatically transitions back to previous agent
  4. Complete plan is passed to the execution agent


## Read-only design[](https://kiro.dev/docs/cli/chat/planning-agent/#read-only-design)
The Plan agent operates in read-only mode to keep focus on planning.
Operation | Status  
---|---  
File reading | ✓ Full access to explore codebase  
Code intelligence | ✓ LSP operations for understanding code structure  
Search (grep, glob) | ✓ Code exploration  
Web search | ✓ Documentation and research access  
File writing | ✗ Cannot create or modify files  
Command execution | ✗ Limited to read-only bash commands  
MCP tools | ✗ Cannot use MCP tools  
## Best practices[](https://kiro.dev/docs/cli/chat/planning-agent/#best-practices)
  1. **Use for complex tasks** - Most valuable for multi-step implementations
  2. **Engage with questions** - Answer structured questions thoughtfully
  3. **Let it explore** - Allow planner to analyze your existing codebase
  4. **Review plans** - Ensure plan matches expectations before handoff
  5. **Iterate as needed** - Continue refining until plan is clear


## Troubleshooting[](https://kiro.dev/docs/cli/chat/planning-agent/#troubleshooting)
Issue | Solution  
---|---  
How to exit plan agent? | Use `Shift + Tab` to return to your previous agent.  
Planning session interrupted | Use `/plan` to re-enter planning and continue where you left off.  
Plan not transferring to execution agent | Make sure to respond "y" when prompted with "Ready to exit [plan] agent to start your implementation? [y/n]".  
## Example workflow[](https://kiro.dev/docs/cli/chat/planning-agent/#example-workflow)
bash
```

> /plan Add user authentication to my web app

[plan] > I understand you want to add user authentication to your web application.

**My Understanding:** You want to implement user authentication functionality
for an existing web application.

[1]: What authentication method do you prefer?
a. **Email/Password** - Traditional username and password
b. **OAuth** - Google, GitHub, or other OAuth providers
c. **Magic Links** - Passwordless email-based authentication
d. **Multi-factor** - Combination of methods with 2FA

> 1=a

[plan] > Great! Email/password authentication it is.

[2]: What's your current tech stack?
a. **React + Node.js** - JavaScript full-stack
b. **Next.js** - React with server-side rendering
c. **Django/Flask** - Python web framework
d. **Other** - Please specify

> 2=d, I'm using Rust with Axum framework

[plan] > Perfect! Rust with Axum is an excellent choice for secure authentication.

*Researching Axum authentication patterns...*
*Exploring your existing codebase structure...*

**Implementation Plan - User Authentication System**
[Detailed plan follows...]

Does this plan look good, or would you like me to adjust anything?

> Looks perfect!

Ready to exit [plan] agent to start your implementation? [y/n]: y

[default] > Implement this plan: [Plan content transferred to execution agent]


```

Page updated: December 19, 2025
[Subagents](https://kiro.dev/docs/cli/chat/subagents/)
[Prompts](https://kiro.dev/docs/cli/chat/manage-prompts/)
On this page
  * [Getting started](https://kiro.dev/docs/cli/chat/planning-agent/#getting-started)
  * [Keyboard shortcut](https://kiro.dev/docs/cli/chat/planning-agent/#keyboard-shortcut)
  * [Slash command](https://kiro.dev/docs/cli/chat/planning-agent/#slash-command)
  * [With immediate prompt](https://kiro.dev/docs/cli/chat/planning-agent/#with-immediate-prompt)
  * [Plan workflow](https://kiro.dev/docs/cli/chat/planning-agent/#plan-workflow)
  * [1. Requirements gathering](https://kiro.dev/docs/cli/chat/planning-agent/#1-requirements-gathering)
  * [2. Research and analysis](https://kiro.dev/docs/cli/chat/planning-agent/#2-research-and-analysis)
  * [3. Implementation plan](https://kiro.dev/docs/cli/chat/planning-agent/#3-implementation-plan)
  * [4. Plan approval and handoff](https://kiro.dev/docs/cli/chat/planning-agent/#4-plan-approval-and-handoff)
  * [Read-only design](https://kiro.dev/docs/cli/chat/planning-agent/#read-only-design)
  * [Best practices](https://kiro.dev/docs/cli/chat/planning-agent/#best-practices)
  * [Troubleshooting](https://kiro.dev/docs/cli/chat/planning-agent/#troubleshooting)
  * [Example workflow](https://kiro.dev/docs/cli/chat/planning-agent/#example-workflow)