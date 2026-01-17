# Agent configuration reference
Every agent configuration file can include the following sections:
  * [`name`](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#name-field) — The name of the agent (optional, derived from filename if not specified).
  * [`description`](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#description-field) — A description of the agent.
  * [`prompt`](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#prompt-field) — High-level context for the agent.
  * [`mcpServers`](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#mcpservers-field) — The MCP servers the agent has access to.
  * [`tools`](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#tools-field) — The tools available to the agent.
  * [`toolAliases`](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#toolaliases-field) — Tool name remapping for handling naming collisions.
  * [`allowedTools`](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#allowedtools-field) — Tools that can be used without prompting.
  * [`toolsSettings`](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#toolssettings-field) — Configuration for specific tools.
  * [`resources`](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#resources-field) — Resources available to the agent.
  * [`hooks`](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#hooks-field) — Commands run at specific trigger points.
  * [`includeMcpJson`](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#includemcpjson-field) — Whether to include MCP servers from mcp.json files.
  * [`model`](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#model-field) — The model ID to use for this agent.


## Name field[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#name-field)
The `name` field specifies the name of the agent. This is used for identification and display purposes.
json
```

{
  "name": "aws-expert"
}


```

## Description field[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#description-field)
The `description` field provides a description of what the agent does. This is primarily for human readability and helps users distinguish between different agents.
json
```

{
  "description": "An agent specialized for AWS infrastructure tasks"
}


```

## Prompt field[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#prompt-field)
The `prompt` field is intended to provide high-level context to the agent, similar to a system prompt. It supports both inline text and file:// URIs to reference external files.
### Inline prompt[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#inline-prompt)
json
```

{
  "prompt": "You are an expert AWS infrastructure specialist"
}


```

### File URI prompt[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#file-uri-prompt)
You can reference external files using `file://` URIs. This allows you to maintain long, complex prompts in separate files for better organization and version control, while keeping your agent configuration clean and readable.
json
```

{
  "prompt": "file://./my-agent-prompt.md"
}


```

#### File URI path resolution[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#file-uri-path-resolution)
  * **Relative paths** : Resolved relative to the agent configuration file's directory 
    * `"file://./prompt.md"` → `prompt.md` in the same directory as the agent config
    * `"file://../shared/prompt.md"` → `prompt.md` in a parent directory
  * **Absolute paths** : Used as-is 
    * `"file:///home/user/prompts/agent.md"` → Absolute path to the file


#### File URI examples[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#file-uri-examples)
json
```

{
  "prompt": "file://./prompts/aws-expert.md"
}


```

json
```

{
  "prompt": "file:///Users/developer/shared-prompts/rust-specialist.md"
}


```

## McpServers field[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#mcpservers-field)
The `mcpServers` field specifies which Model Context Protocol (MCP) servers the agent has access to. Each server is defined with a command and optional arguments.
json
```

{
  "mcpServers": {
    "fetch": {
      "command": "fetch3.1",
      "args": []
    },
    "git": {
      "command": "git-mcp",
      "args": [],
      "env": {
        "GIT_CONFIG_GLOBAL": "/dev/null"
      },
      "timeout": 120000
    }
  }
}


```

Each MCP server configuration can include:
  * `command` (required): The command to execute to start the MCP server
  * `args` (optional): Arguments to pass to the command
  * `env` (optional): Environment variables to set for the server
  * `timeout` (optional): Timeout for each MCP request in milliseconds (default: 120000)


## Tools field[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#tools-field)
The `tools` field lists all tools that the agent can potentially use. Tools include built-in tools and tools from MCP servers.
  * Built-in tools are specified by their name (e.g., `read`, `shell`)
  * MCP server tools are prefixed with `@` followed by the server name (e.g., `@git`)
  * To specify a specific tool from an MCP server, use `@server_name/tool_name`
  * Use `*` as a special wildcard to include all available tools (both built-in and from MCP servers)
  * Use `@builtin` to include all built-in tools
  * Use `@server_name` to include all tools from a specific MCP server


json
```

{
  "tools": [
    "read",
    "write",
    "shell",
    "@git",
    "@rust-analyzer/check_code"
  ]
}


```

To include all available tools, you can simply use:
json
```

{
  "tools": ["*"]
}


```

## ToolAliases field[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#toolaliases-field)
The `toolAliases` field is an advanced feature that allows you to remap tool names. This is primarily used to resolve naming collisions between tools from different MCP servers, or to create more intuitive names for specific tools.
For example, if both `@github-mcp` and `@gitlab-mcp` servers provide a tool called `get_issues`, you would have a naming collision. You can use `toolAliases` to disambiguate them:
json
```

{
  "toolAliases": {
    "@github-mcp/get_issues": "github_issues",
    "@gitlab-mcp/get_issues": "gitlab_issues"
  }
}


```

With this configuration, the tools will be available to the agent as `github_issues` and `gitlab_issues` instead of having a collision on `get_issues`.
You can also use aliases to create shorter or more intuitive names for frequently used tools:
json
```

{
  "toolAliases": {
    "@aws-cloud-formation/deploy_stack_with_parameters": "deploy_cf",
    "@kubernetes-tools/get_pod_logs_with_namespace": "pod_logs"
  }
}


```

The key is the original tool name (including server prefix for MCP tools), and the value is the new name to use.
## AllowedTools field[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#allowedtools-field)
The `allowedTools` field specifies which tools can be used without prompting the user for permission. This is a security feature that helps prevent unauthorized tool usage.
json
```

{
  "allowedTools": [
    "read",
    "write",
    "@git/git_status",
    "@server/read_*",
    "@fetch"
  ]
}


```

You can allow tools using several patterns:
### Exact matches[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#exact-matches)
  * **Built-in tools** : `"read"`, `"shell"`, `"knowledge"`
  * **Specific MCP tools** : `"@server_name/tool_name"` (e.g., `"@git/git_status"`)
  * **All tools from MCP server** : `"@server_name"` (e.g., `"@fetch"`)


### Wildcard patterns[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#wildcard-patterns)
The `allowedTools` field supports glob-style wildcard patterns using `*` and `?`:
#### MCP tool patterns[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#mcp-tool-patterns)
  * **Tool prefix** : `"@server/read_*"` → matches `@server/read_file`, `@server/read_config`
  * **Tool suffix** : `"@server/*_get"` → matches `@server/issue_get`, `@server/data_get`
  * **Server pattern** : `"@*-mcp/read_*"` → matches `@git-mcp/read_file`, `@db-mcp/read_data`
  * **Any tool from pattern servers** : `"@git-*/*"` → matches any tool from servers matching `git-*`


Optionally, you can also prefix native tools with the namespace `@builtin`.
### Examples[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#examples)
json
```

{
  "allowedTools": [
    // Exact matches
    "read",
    "knowledge",
    "@server/specific_tool",
    
    // Native tool wildcards
    "r*",                    // Read
    "w*",               // Write
    @builtin,                // All native tools
    
    // MCP tool wildcards
    "@server/api_*",           // All API tools from server
    "@server/read_*",          // All read tools from server
    "@git-server/get_*_info",  // Tools like get_user_info, get_repo_info
    "@*/status",               // Status tool from any server
    
    // Server-level permissions
    "@fetch",                  // All tools from fetch server
    "@git-*"                   // All tools from any git-* server
  ]
}


```

### Pattern matching rules[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#pattern-matching-rules)
  * **`*`**matches any sequence of characters (including none)
  * **`?`**matches exactly one character
  * **Exact matches** take precedence over patterns
  * **Server-level permissions** (`@server_name`) allow all tools from that server
  * **Case-sensitive** matching


Unlike the `tools` field, the `allowedTools` field does not support the `"*"` wildcard for allowing all tools. To allow tools, you must use specific patterns or server-level permissions.
## ToolsSettings field[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#toolssettings-field)
The `toolsSettings` field provides configuration for specific tools. Each tool can have its own unique configuration options. Note that specifications that configure allowable patterns will be overridden if the tool is also included in `allowedTools`.
json
```

{
  "toolsSettings": {
    "write": {
      "allowedPaths": ["~/**"]
    },
    "@git/git_status": {
      "git_user": "$GIT_USER"
    }
  }
}


```

## Resources field[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#resources-field)
The `resources` field gives an agent access to local resources. Currently, only file resources are supported, and all resource paths must start with `file://`.
json
```

{
  "resources": [
    "file://AmazonQ.md",
    "file://README.md",
    "file://.amazonq/rules/**/*.md"
  ]
}


```

Resources can include:
  * Specific files
  * Glob patterns for multiple files
  * Absolute or relative paths


## Hooks field[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#hooks-field)
The `hooks` field defines commands to run at specific trigger points during agent lifecycle and tool execution.
For detailed information about hook behavior, input/output formats, and examples, see the [Hooks documentation](https://kiro.dev/docs/cli/hooks).
json
```

{
  "hooks": {
    "agentSpawn": [
      {
        "command": "git status"
      }
    ],
    "userPromptSubmit": [
      {
        "command": "ls -la"
      }
    ],
    "preToolUse": [
      {
        "matcher": "shell",
        "command": "{ echo \"$(date) - Bash command:\"; cat; echo; } >> /tmp/bash_audit_log"
      },
      {
        "matcher": "aws",
        "command": "{ echo \"$(date) - AWS CLI call:\"; cat; echo; } >> /tmp/aws_audit_log"
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

Each hook is defined with:
  * `command` (required): The command to execute
  * `matcher` (optional): Pattern to match tool names for `preToolUse` and `postToolUse` hooks. See [built-in tools documentation](https://kiro.dev/docs/cli/custom-agents/configuration-reference/built-in-tools.md) for available tool names.


Available hook triggers:
  * `agentSpawn`: Triggered when the agent is initialized.
  * `userPromptSubmit`: Triggered when the user submits a message.
  * `preToolUse`: Triggered before a tool is executed. Can block the tool use.
  * `postToolUse`: Triggered after a tool is executed.
  * `stop`: Triggered when the assistant finishes responding.


## includeMcpJson field[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#includemcpjson-field)
The `includeMcpJson` field determines whether to include MCP servers defined in the MCP configuration files (`~/.kiro/settings/mcp.json` for global and `<cwd>/.kiro/settings/mcp.json` for workspace).
json
```

{
  "includeMcpJson": true
}


```

When set to `true`, the agent will have access to all MCP servers defined in the global and local configurations in addition to those defined in the agent's `mcpServers` field.
## Model field[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#model-field)
The `model` field specifies the model ID to use for this agent. If not specified, the agent will use the default model.
json
```

{
  "model": "claude-sonnet-4"
}


```

The model ID must match one of the available models returned by the Kiro CLI's model service. You can see available models by using the `/model` command in an active chat session.
If the specified model is not available, the agent will fall back to the default model and display a warning.
## Complete example[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#complete-example)
Here's a complete example of an agent configuration file:
json
```

{
  "name": "aws-rust-agent",
  "description": "A specialized agent for AWS and Rust development tasks",
  "mcpServers": {
    "fetch": {
      "command": "fetch3.1",
      "args": []
    },
    "git": {
      "command": "git-mcp",
      "args": []
    }
  },
  "tools": [
    "read",
    "write",
    "shell",
    "aws",
    "@git",
    "@fetch/fetch_url"
  ],
  "toolAliases": {
    "@git/git_status": "status",
    "@fetch/fetch_url": "get"
  },
  "allowedTools": [
    "read",
    "@git/git_status"
  ],
  "toolsSettings": {
    "write": {
      "allowedPaths": ["src/**", "tests/**", "Cargo.toml"]
    },
    "aws": {
      "allowedServices": ["s3", "lambda"]
    }
  },
  "resources": [
    "file://README.md",
    "file://docs/**/*.md"
  ],
  "hooks": {
    "agentSpawn": [
      {
        "command": "git status"
      }
    ],
    "userPromptSubmit": [
      {
        "command": "ls -la"
      }
    ]
  },
  "useLegacyMcpJson": true,
  "model": "claude-sonnet-4"
}


```

Agent configuration files are JSON files that define how your custom agents behave. The filename (without `.json`) becomes the agent's name.
## Quick start[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#quick-start)
We recommend using the `/agent generate` command within your active Kiro session to intelligently generate agent configurations with AI assistance.
## File locations[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#file-locations)
You can define local agents and global agents.
### Local agents (project-specific)[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#local-agents-project-specific)
```

.kiro/agents/


```

Local agents are specific to the current workspace and only available when running Kiro CLI from that directory or its subdirectories.
**Example:**
```

my-project/
├── .kiro/
│   └── agents/
│       ├── dev-agent.json
│       └── aws-specialist.json
└── src/
    └── main.py


```

### Global agents (user-wide)[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#global-agents-user-wide)
```

~/.kiro/agents/


```

Global agents are available from any directory.
**Example:**
```

~/.kiro/agents/
├── general-assistant.json
├── code-reviewer.json
└── documentation-writer.json


```

### Agent precedence[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#agent-precedence)
When Kiro CLI looks for an agent:
  1. **Local first** : Checks `.kiro/agents/` in the current directory
  2. **Global fallback** : Checks `~/.kiro/agents/` in the HOME directory


If both locations have agents with the same name, the local agent takes precedence with a warning message.
## Configuration fields[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#configuration-fields)
### name[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#name)
The agent's name for identification and display.
json
```

{
  "name": "aws-expert"
}


```

### description[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#description)
Human-readable description of the agent's purpose.
json
```

{
  "description": "An agent specialized for AWS infrastructure tasks"
}


```

### prompt[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#prompt)
High-level context for the agent, similar to a system prompt. Supports inline text or `file://` URIs.
**Inline:**
json
```

{
  "prompt": "You are an expert AWS infrastructure specialist"
}


```

**File URI:**
json
```

{
  "prompt": "file://./my-agent-prompt.md"
}


```

**Path Resolution:**
  * Relative paths: Resolved relative to agent config file 
    * `"file://./prompt.md"` → Same directory as agent config
    * `"file://../shared/prompt.md"` → Parent directory
  * Absolute paths: Used as-is 
    * `"file:///home/user/prompts/agent.md"`


### mcpServers[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#mcpservers)
MCP servers the agent can access.
json
```

{
  "mcpServers": {
    "fetch": {
      "command": "fetch-server",
      "args": []
    },
    "git": {
      "command": "git-mcp",
      "args": [],
      "env": {
        "GIT_CONFIG_GLOBAL": "/dev/null"
      },
      "timeout": 120000
    }
  }
}


```

**Fields:**
  * `command` (required): Command to start the MCP server
  * `args` (optional): Arguments for the command
  * `env` (optional): Environment variables
  * `timeout` (optional): Request timeout in milliseconds (default: 120000)


### tools[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#tools)
Tools available to the agent.
json
```

{
  "tools": [
    "read",
    "write",
    "shell",
    "@git",
    "@rust-analyzer/check_code"
  ]
}


```

**Tool References:**
  * Built-in tools: `"read"`, `"shell"`
  * All MCP server tools: `"@server_name"`
  * Specific MCP tool: `"@server_name/tool_name"`
  * All tools: `"*"`
  * All built-in tools: `"@builtin"`


### toolAliases[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#toolaliases)
Remap tool names to resolve naming collisions or create intuitive names.
json
```

{
  "toolAliases": {
    "@github-mcp/get_issues": "github_issues",
    "@gitlab-mcp/get_issues": "gitlab_issues",
    "@aws-cloud-formation/deploy_stack_with_parameters": "deploy_cf"
  }
}


```

### allowedTools[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#allowedtools)
Tools that can be used without prompting for permission.
json
```

{
  "allowedTools": [
    "read",
    "@git/git_status",
    "@server/read_*",
    "@fetch"
  ]
}


```

**Pattern Support:**
**Exact Matches:**
  * Built-in: `"read"`, `"shell"`
  * MCP tool: `"@server_name/tool_name"`
  * All server tools: `"@server_name"`


**Wildcards:**
  * Prefix: `"code_*"` → `code_review`, `code_analysis`
  * Suffix: `"*_bash"` → `execute_bash`, `run_bash`
  * Single char: `"?ead"` → `read`, `head`
  * MCP patterns: `"@server/read_*"`, `"@git-*/status"`


### toolsSettings[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#toolssettings)
Configuration for specific tools.
json
```

{
  "toolsSettings": {
    "write": {
      "allowedPaths": ["~/**"]
    },
    "shell": {
      "allowedCommands": ["git status", "git fetch"],
      "deniedCommands": ["git commit .*", "git push .*"],
      "autoAllowReadonly": true
    },
    "@git/git_status": {
      "git_user": "$GIT_USER"
    }
  }
}


```

See [Built-in Tools](https://kiro.dev/docs/cli/reference/built-in-tools) for tool-specific options.
### resources[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#resources)
Local resources available to the agent. All paths must start with `file://`.
json
```

{
  "resources": [
    "file://README.md",
    "file://.kiro/steering/**/*.md",
    "file://docs/**/*.md"
  ]
}


```

Supports:
  * Specific files
  * Glob patterns
  * Absolute or relative paths


### hooks[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#hooks)
Commands to run at specific trigger points.
json
```

{
  "hooks": {
    "agentSpawn": [
      {
        "command": "git status"
      }
    ],
    "userPromptSubmit": [
      {
        "command": "ls -la"
      }
    ],
    "preToolUse": [
      {
        "matcher": "shell",
        "command": "{ echo \"$(date) - Bash:\"; cat; } >> /tmp/audit.log"
      }
    ],
    "postToolUse": [
      {
        "matcher": "write",
        "command": "cargo fmt --all"
      }
    ],
    "stop": [
      {
        "command": "npm test"
      }
    ]
  }
}


```

**Hook Types:**
  * `agentSpawn`: When agent is activated
  * `userPromptSubmit`: When user submits a prompt
  * `preToolUse`: Before tool execution (can block)
  * `postToolUse`: After tool execution
  * `stop`: When assistant finishes responding


See [Hooks](https://kiro.dev/docs/cli/hooks) for detailed documentation.
### model[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#model)
Model ID to use for this agent.
json
```

{
  "model": "claude-sonnet-4"
}


```

If not specified or unavailable, falls back to default model.
## Complete example[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#complete-example-1)
json
```

{
  "name": "aws-rust-agent",
  "description": "Specialized agent for AWS and Rust development",
  "prompt": "file://./prompts/aws-rust-expert.md",
  "mcpServers": {
    "fetch": {
      "command": "fetch-server",
      "args": []
    },
    "git": {
      "command": "git-mcp",
      "args": []
    }
  },
  "tools": [
    "read",
    "write",
    "shell",
    "aws",
    "@git",
    "@fetch/fetch_url"
  ],
  "toolAliases": {
    "@git/git_status": "status",
    "@fetch/fetch_url": "get"
  },
  "allowedTools": [
    "read",
    "@git/git_status"
  ],
  "toolsSettings": {
    "write": {
      "allowedPaths": ["src/**", "tests/**", "Cargo.toml"]
    },
    "aws": {
      "allowedServices": ["s3", "lambda"],
      "autoAllowReadonly": true
    }
  },
  "resources": [
    "file://README.md",
    "file://docs/**/*.md"
  ],
  "hooks": {
    "agentSpawn": [
      {
        "command": "git status"
      }
    ],
    "postToolUse": [
      {
        "matcher": "write",
        "command": "cargo fmt --all"
      }
    ]
  },
  "model": "claude-sonnet-4"
}


```

## Best practices[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#best-practices)
  1. Start restrictive: Begin with minimal tool access and expand as needed
  2. Name clearly: Use descriptive names that indicate the agent's purpose
  3. Document usage: Add clear descriptions to help team members understand the agent
  4. Version control: Store agent configurations in your project repository
  5. Test thoroughly: Verify tool permissions work as expected before sharing


### Local vs global agents[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#local-vs-global-agents)
**Use Local Agents For:**
  * Project-specific configurations
  * Agents needing project files/tools
  * Development environments with unique requirements
  * Sharing with team via version control


**Use Global Agents For:**
  * General-purpose agents across projects
  * Personal productivity agents
  * Agents without project-specific context
  * Commonly used tools and workflows


### Security[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#security)
  * Review `allowedTools` carefully
  * Use specific patterns over wildcards
  * Configure `toolsSettings` for sensitive operations
  * Test agents in safe environments first


### Organization[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#organization)
  * Use descriptive agent names
  * Document agent purposes in descriptions
  * Keep prompt files organized
  * Version control local agents with projects


## Next steps[](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#next-steps)
  * [Creating Custom Agents](https://kiro.dev/docs/cli/custom-agents/creating)
  * [Built-in Tools Reference](https://kiro.dev/docs/cli/built-in-tools)
  * [Hooks Documentation](https://kiro.dev/docs/cli/hooks)
  * [Agent Examples](https://kiro.dev/docs/cli/custom-agents/examples)


Page updated: November 27, 2025
[Creating custom agents](https://kiro.dev/docs/cli/custom-agents/creating/)
[Examples](https://kiro.dev/docs/cli/custom-agents/examples/)
On this page
  * [Name field](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#name-field)
  * [Description field](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#description-field)
  * [Prompt field](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#prompt-field)
  * [Inline prompt](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#inline-prompt)
  * [File URI prompt](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#file-uri-prompt)
  * [File URI path resolution](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#file-uri-path-resolution)
  * [File URI examples](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#file-uri-examples)
  * [McpServers field](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#mcpservers-field)
  * [Tools field](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#tools-field)
  * [ToolAliases field](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#toolaliases-field)
  * [AllowedTools field](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#allowedtools-field)
  * [Exact matches](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#exact-matches)
  * [Wildcard patterns](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#wildcard-patterns)
  * [MCP tool patterns](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#mcp-tool-patterns)
  * [Examples](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#examples)
  * [Pattern matching rules](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#pattern-matching-rules)
  * [ToolsSettings field](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#toolssettings-field)
  * [Resources field](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#resources-field)
  * [Hooks field](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#hooks-field)
  * [includeMcpJson field](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#includemcpjson-field)
  * [Model field](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#model-field)
  * [Complete example](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#complete-example)
  * [Quick start](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#quick-start)
  * [File locations](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#file-locations)
  * [Local agents (project-specific)](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#local-agents-project-specific)
  * [Global agents (user-wide)](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#global-agents-user-wide)
  * [Agent precedence](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#agent-precedence)
  * [Configuration fields](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#configuration-fields)
  * [name](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#name)
  * [description](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#description)
  * [prompt](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#prompt)
  * [mcpServers](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#mcpservers)
  * [tools](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#tools)
  * [toolAliases](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#toolaliases)
  * [allowedTools](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#allowedtools)
  * [toolsSettings](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#toolssettings)
  * [resources](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#resources)
  * [hooks](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#hooks)
  * [model](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#model)
  * [Complete example](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#complete-example-1)
  * [Best practices](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#best-practices)
  * [Local vs global agents](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#local-vs-global-agents)
  * [Security](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#security)
  * [Organization](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#organization)
  * [Next steps](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#next-steps)