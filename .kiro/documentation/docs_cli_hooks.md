# Hooks
Hooks allow you to execute custom commands at specific points during agent lifecycle and tool execution. This enables security validation, logging, formatting, context gathering, and other custom behaviors.
## Defining hooks[](https://kiro.dev/docs/cli/hooks/#defining-hooks)
Hooks are defined in the agent configuration file. See the [Agent Configuration Reference](https://kiro.dev/docs/cli/custom-agents/configuration-reference#hooks-field) for the complete syntax and examples.
## Hook event[](https://kiro.dev/docs/cli/hooks/#hook-event)
Hooks receive hook event in JSON format via STDIN:
json
```

{
  "hook_event_name": "agentSpawn",
  "cwd": "/current/working/directory"
}


```

For tool-related hooks, additional fields are included:
  * `tool_name`: Name of the tool being executed
  * `tool_input`: Tool-specific parameters (see individual tool documentation)
  * `tool_response`: Tool execution results (PostToolUse only)


## Hook output[](https://kiro.dev/docs/cli/hooks/#hook-output)
  * **Exit code 0** : Hook succeeded. STDOUT is captured but not shown to user.
  * **Exit code 2** : (PreToolUse only) Block tool execution. STDERR is returned to the LLM.
  * **Other exit codes** : Hook failed. STDERR is shown as warning to user.


## Tool matching[](https://kiro.dev/docs/cli/hooks/#tool-matching)
Use the `matcher` field to specify which tools the hook applies to:
### Examples[](https://kiro.dev/docs/cli/hooks/#examples)
  * `"write"` - Exact match for built-in tools
  * `"@git"` - All tools from git MCP server
  * `"@git/status"` - Specific tool from git MCP server
  * `"*"` - All tools (built-in and MCP)
  * `"@builtin"` - All built-in tools only
  * No matcher - Applies to all tools


For complete tool reference format, see [Agent Configuration Reference](https://kiro.dev/docs/cli/custom-agents/configuration-reference#tools-field).
## Hook types[](https://kiro.dev/docs/cli/hooks/#hook-types)
### AgentSpawn[](https://kiro.dev/docs/cli/hooks/#agentspawn)
Runs when agent is activated. No tool context provided.
**Hook Event**
json
```

{
  "hook_event_name": "agentSpawn",
  "cwd": "/current/working/directory"
}


```

**Exit Code Behavior:**
  * **0** : Hook succeeded, STDOUT is added to agent's context
  * **Other** : Show STDERR warning to user


### UserPromptSubmit[](https://kiro.dev/docs/cli/hooks/#userpromptsubmit)
Runs when user submits a prompt. Output is added to conversation context.
**Hook Event**
json
```

{
  "hook_event_name": "userPromptSubmit",
  "cwd": "/current/working/directory",
  "prompt": "user's input prompt"
}


```

**Exit Code Behavior:**
  * **0** : Hook succeeded, STDOUT is added to agent's context
  * **Other** : Show STDERR warning to user


### PreToolUse[](https://kiro.dev/docs/cli/hooks/#pretooluse)
Runs before tool execution. Can validate and block tool usage.
**Hook Event**
json
```

{
  "hook_event_name": "preToolUse",
  "cwd": "/current/working/directory",
  "tool_name": "read",
  "tool_input": {
    "operations": [
      {
        "mode": "Line",
        "path": "/current/working/directory/docs/hooks.md"
      }
    ]
  }
}


```

**Exit Code Behavior:**
  * **0** : Allow tool execution.
  * **2** : Block tool execution, return STDERR to LLM.
  * **Other** : Show STDERR warning to user, allow tool execution.


### PostToolUse[](https://kiro.dev/docs/cli/hooks/#posttooluse)
Runs after tool execution with access to tool results.
**Hook Event**
json
```

{
  "hook_event_name": "postToolUse",
  "cwd": "/current/working/directory",
  "tool_name": "read",
  "tool_input": {
    "operations": [
      {
        "mode": "Line",
        "path": "/current/working/directory/docs/hooks.md"
      }
    ]
  },
  "tool_response": {
    "success": true,
    "result": ["# Hooks\n\nHooks allow you to execute..."]
  }
}


```

**Exit Code Behavior:**
  * **0** : Hook succeeded.
  * **Other** : Show STDERR warning to user. Tool already ran.


### Stop[](https://kiro.dev/docs/cli/hooks/#stop)
Runs when the assistant finishes responding to the user (at the end of each turn). This is useful for running post-processing tasks like code compilation, testing, formatting, or cleanup after the assistant's response.
**Hook Event**
json
```

{
  "hook_event_name": "stop",
  "cwd": "/current/working/directory"
}


```

**Exit Code Behavior:**
  * **0** : Hook succeeded.
  * **Other** : Show STDERR warning to user.


**Note** : Stop hooks do not use matchers since they don't relate to specific tools.
### MCP Example[](https://kiro.dev/docs/cli/hooks/#mcp-example)
For MCP tools, the tool name includes the full namespaced format including the MCP Server name:
**Hook Event**
json
```

{
  "hook_event_name": "preToolUse",
  "cwd": "/current/working/directory",
  "tool_name": "@postgres/query",
  "tool_input": {
    "sql": "SELECT * FROM orders LIMIT 10;"
  }
}


```

## Timeout[](https://kiro.dev/docs/cli/hooks/#timeout)
Default timeout is 30 seconds (30,000ms). Configure with `timeout_ms` field.
## Caching[](https://kiro.dev/docs/cli/hooks/#caching)
Successful hook results are cached based on `cache_ttl_seconds`:
  * `0`: No caching (default)
  * `> 0`: Cache successful results for specified seconds
  * AgentSpawn hooks are never cached


Page updated: November 24, 2025
[Delegate](https://kiro.dev/docs/cli/experimental/delegate/)
[Auto complete](https://kiro.dev/docs/cli/autocomplete/)
On this page
  * [Defining hooks](https://kiro.dev/docs/cli/hooks/#defining-hooks)
  * [Hook event](https://kiro.dev/docs/cli/hooks/#hook-event)
  * [Hook output](https://kiro.dev/docs/cli/hooks/#hook-output)
  * [Tool matching](https://kiro.dev/docs/cli/hooks/#tool-matching)
  * [Examples](https://kiro.dev/docs/cli/hooks/#examples)
  * [Hook types](https://kiro.dev/docs/cli/hooks/#hook-types)
  * [AgentSpawn](https://kiro.dev/docs/cli/hooks/#agentspawn)
  * [UserPromptSubmit](https://kiro.dev/docs/cli/hooks/#userpromptsubmit)
  * [PreToolUse](https://kiro.dev/docs/cli/hooks/#pretooluse)
  * [PostToolUse](https://kiro.dev/docs/cli/hooks/#posttooluse)
  * [Stop](https://kiro.dev/docs/cli/hooks/#stop)
  * [MCP Example](https://kiro.dev/docs/cli/hooks/#mcp-example)
  * [Timeout](https://kiro.dev/docs/cli/hooks/#timeout)
  * [Caching](https://kiro.dev/docs/cli/hooks/#caching)