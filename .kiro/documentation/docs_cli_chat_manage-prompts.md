# Manage prompts
The Kiro CLI provides comprehensive prompt management capabilities for both local prompts and Model Context Protocol (MCP) prompts. This system allows you to create, edit, organize, and use reusable prompts across your development workflow.
## About prompt types[](https://kiro.dev/docs/cli/chat/manage-prompts/#about-prompt-types)
The prompt system supports three types of prompts:
  * **Local prompts** : Project-specific prompts stored in your workspace
  * **Global prompts** : User-wide prompts available across all projects
  * **MCP prompts** : Prompts provided by MCP servers with enhanced functionality


## Commands[](https://kiro.dev/docs/cli/chat/manage-prompts/#commands)
All prompt management is accessed through the `/prompts` command with various subcommands.
### List prompts[](https://kiro.dev/docs/cli/chat/manage-prompts/#list-prompts)
```

/prompts list


```

Displays all available prompts in a three-column layout showing names, descriptions, and sources. Shows prompt counts and indicates which prompts come from local storage, global storage, or MCP servers.
### Create prompts[](https://kiro.dev/docs/cli/chat/manage-prompts/#create-prompts)
```

/prompts create --name name [--content content]


```

Creates a new local prompt in the current workspace.
###### Parameters[](https://kiro.dev/docs/cli/chat/manage-prompts/#parameters)
`name` (required) : Prompt name (maximum 50 characters)
`--content content` (optional) : Direct content specification
**Behavior:**
  * If `--content` is provided, creates prompt with specified content
  * If no content provided, opens your default editor for content creation
  * Prompts are saved to `.kiro/prompts/` in the current workspace


### Edit prompts[](https://kiro.dev/docs/cli/chat/manage-prompts/#edit-prompts)
```

/prompts edit name


```

Opens an existing prompt in your default editor for modification.
**Supported prompts:**
  * Local workspace prompts
  * Global user prompts
  * MCP prompts (where supported by the server)


### View prompt details[](https://kiro.dev/docs/cli/chat/manage-prompts/#view-prompt-details)
```

/prompts details name


```

Shows comprehensive information about a prompt including:
  * Metadata and argument details
  * Complete prompt content before AI processing
  * Parameter requirements and examples
  * Source information (local, global, or MCP server)


## Using prompts[](https://kiro.dev/docs/cli/chat/manage-prompts/#using-prompts)
Once you've created prompts, invoke them in chat using the @ prefix:
```

@prompt-name


```

### Examples[](https://kiro.dev/docs/cli/chat/manage-prompts/#examples)
```

@code-review
# Uses your local code-review prompt


```

```

@team-standup
# Uses your team-standup prompt


```

## Passing arguments to MCP prompts[](https://kiro.dev/docs/cli/chat/manage-prompts/#passing-arguments-to-mcp-prompts)
MCP server prompts can accept arguments to customize their behavior. File-based prompts (local and global) do not support arguments.
### MCP prompt argument syntax[](https://kiro.dev/docs/cli/chat/manage-prompts/#mcp-prompt-argument-syntax)
```

@server-name/prompt-name <required-arg> [optional-arg]


```

Use `/prompts details prompt-name` to discover what arguments an MCP prompt accepts.
```

# Example: Using MCP prompt with arguments
@dev-tools/analyze "performance issue" "detailed"
@security-tools/scan "web-app" "high-severity"


```

## Storage locations[](https://kiro.dev/docs/cli/chat/manage-prompts/#storage-locations)
### Local prompts (workspace-specific)[](https://kiro.dev/docs/cli/chat/manage-prompts/#local-prompts-workspace-specific)
  * **Location** : `project/.kiro/prompts/`
  * **Scope** : Available only within the current project
  * **Priority** : Highest (overrides global and MCP prompts with same name)


### Global prompts (user-wide)[](https://kiro.dev/docs/cli/chat/manage-prompts/#global-prompts-user-wide)
  * **Location** : `~/.kiro/prompts/`
  * **Scope** : Available across all projects
  * **Priority** : Medium (overrides MCP prompts with same name)


### MCP prompts[](https://kiro.dev/docs/cli/chat/manage-prompts/#mcp-prompts)
  * **Source** : Provided by configured MCP servers
  * **Scope** : Depends on server configuration
  * **Priority** : Lowest (overridden by local and global prompts)


## Priority system[](https://kiro.dev/docs/cli/chat/manage-prompts/#priority-system)
When multiple prompts have the same name, the system uses this priority order:
  1. **Local prompts** (highest priority)
  2. **Global prompts**
  3. **MCP prompts** (lowest priority)


This allows you to override MCP or global prompts with project-specific versions when needed.
## Enhanced features[](https://kiro.dev/docs/cli/chat/manage-prompts/#enhanced-features)
### Content preview[](https://kiro.dev/docs/cli/chat/manage-prompts/#content-preview)
The system displays the complete prompt content before sending it to the AI model, eliminating confusion about what information was actually processed.
### Improved error handling[](https://kiro.dev/docs/cli/chat/manage-prompts/#improved-error-handling)
  * MCP server errors are converted to user-friendly messages
  * Helpful usage examples are generated from prompt metadata
  * Clear guidance for invalid parameters or missing requirements


### Visual formatting[](https://kiro.dev/docs/cli/chat/manage-prompts/#visual-formatting)
  * Consistent terminal styling across all prompt operations
  * Proper content display for all prompt message types
  * Three-column layout for improved readability in listings


## MCP integration[](https://kiro.dev/docs/cli/chat/manage-prompts/#mcp-integration)
The prompt system seamlessly integrates with MCP servers:
  * **Automatic discovery** : MCP prompts are automatically discovered from configured servers
  * **Enhanced UX** : Improved user experience for MCP prompt management
  * **Error translation** : Raw JSON errors are converted to actionable messages
  * **Content preview** : Full content preview for MCP prompts before execution


## Examples[](https://kiro.dev/docs/cli/chat/manage-prompts/#examples-1)
These examples demonstrate file-based prompt creation and MCP prompt usage.
### Basic file-based prompt creation and usage[](https://kiro.dev/docs/cli/chat/manage-prompts/#basic-file-based-prompt-creation-and-usage)
```

# Create a simple prompt without arguments
/prompts create --name code-review --content "Please review this code for best practices, security issues, and potential improvements:"

# Use the prompt (no arguments supported for file-based prompts)
@code-review


```

### MCP prompt usage with arguments[](https://kiro.dev/docs/cli/chat/manage-prompts/#mcp-prompt-usage-with-arguments)
```

# Using MCP prompts with arguments
@dev-tools/analyze "performance bottleneck" "cpu usage"
@security-tools/scan "web-app" "high-severity"
@aws-tools/deploy "my-service" "production" "us-west-2"


```

Page updated: November 16, 2025
[Planning Agent](https://kiro.dev/docs/cli/chat/planning-agent/)
[Context management](https://kiro.dev/docs/cli/chat/context/)
On this page
  * [About prompt types](https://kiro.dev/docs/cli/chat/manage-prompts/#about-prompt-types)
  * [Commands](https://kiro.dev/docs/cli/chat/manage-prompts/#commands)
  * [List prompts](https://kiro.dev/docs/cli/chat/manage-prompts/#list-prompts)
  * [Create prompts](https://kiro.dev/docs/cli/chat/manage-prompts/#create-prompts)
  * [Edit prompts](https://kiro.dev/docs/cli/chat/manage-prompts/#edit-prompts)
  * [View prompt details](https://kiro.dev/docs/cli/chat/manage-prompts/#view-prompt-details)
  * [Using prompts](https://kiro.dev/docs/cli/chat/manage-prompts/#using-prompts)
  * [Examples](https://kiro.dev/docs/cli/chat/manage-prompts/#examples)
  * [Passing arguments to MCP prompts](https://kiro.dev/docs/cli/chat/manage-prompts/#passing-arguments-to-mcp-prompts)
  * [MCP prompt argument syntax](https://kiro.dev/docs/cli/chat/manage-prompts/#mcp-prompt-argument-syntax)
  * [Storage locations](https://kiro.dev/docs/cli/chat/manage-prompts/#storage-locations)
  * [Local prompts (workspace-specific)](https://kiro.dev/docs/cli/chat/manage-prompts/#local-prompts-workspace-specific)
  * [Global prompts (user-wide)](https://kiro.dev/docs/cli/chat/manage-prompts/#global-prompts-user-wide)
  * [MCP prompts](https://kiro.dev/docs/cli/chat/manage-prompts/#mcp-prompts)
  * [Priority system](https://kiro.dev/docs/cli/chat/manage-prompts/#priority-system)
  * [Enhanced features](https://kiro.dev/docs/cli/chat/manage-prompts/#enhanced-features)
  * [Content preview](https://kiro.dev/docs/cli/chat/manage-prompts/#content-preview)
  * [Improved error handling](https://kiro.dev/docs/cli/chat/manage-prompts/#improved-error-handling)
  * [Visual formatting](https://kiro.dev/docs/cli/chat/manage-prompts/#visual-formatting)
  * [MCP integration](https://kiro.dev/docs/cli/chat/manage-prompts/#mcp-integration)
  * [Examples](https://kiro.dev/docs/cli/chat/manage-prompts/#examples-1)
  * [Basic file-based prompt creation and usage](https://kiro.dev/docs/cli/chat/manage-prompts/#basic-file-based-prompt-creation-and-usage)
  * [MCP prompt usage with arguments](https://kiro.dev/docs/cli/chat/manage-prompts/#mcp-prompt-usage-with-arguments)