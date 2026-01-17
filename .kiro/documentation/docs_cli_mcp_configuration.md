# Configuration
This guide provides detailed information on configuring Model Context Protocol (MCP) servers with Kiro CLI, including configuration file structure, server setup, and management.
## Configuration file structure[](https://kiro.dev/docs/cli/mcp/configuration/#configuration-file-structure)
MCP configuration files use JSON format with the following structure:
json
```

{
  "mcpServers": {
    "local-server-name": {
      "command": "command-to-run-server",
      "args": ["arg1", "arg2"],
      "env": {
        "ENV_VAR1": "hard-coded-variable",
        "ENV_VAR2": "${EXPANDED_VARIABLE}"
      },
      "disabled": false,
      "disabledTools": ["tool_name3"]
    },
    "remote-server-name": {
      "url": "https://endpoint.to.connect.to",
      "headers": {
        "HEADER1": "value1",
        "HEADER2": "value2"
      },
      "disabled": false,
      "disabledTools": ["tool_name3"]
    }
  }
}


```

### Configuration properties[](https://kiro.dev/docs/cli/mcp/configuration/#configuration-properties)
#### Local server[](https://kiro.dev/docs/cli/mcp/configuration/#local-server)
Property | Type | Required | Description  
---|---|---|---  
`command` | String | Yes | The command to run the MCP server  
`args` | Array | Yes | Arguments to pass to the command  
`env` | Object | No | Environment variables for the server process  
`disabled` | Boolean | No | Whether the server is disabled (default: false)  
`autoApprove` | Array | No | Tool names to auto-approve without prompting  
`disabledTools` | Array | No | Tool names to omit when calling the Agent  
#### Remote server[](https://kiro.dev/docs/cli/mcp/configuration/#remote-server)
Property | Type | Required | Description  
---|---|---|---  
`url` | String | Yes | HTTPS endpoint for the remote MCP server (or HTTP endpoint for localhost)  
`headers` | Object | No | Headers to pass to the MCP server during connection  
`env` | Object | No | Environment variables for the server process  
`disabled` | Boolean | No | Whether the server is disabled (default: false)  
`autoApprove` | Array | No | Tool names to auto-approve without prompting  
`disabledTools` | Array | No | Tool names to omit when calling the Agent  
## Example configurations[](https://kiro.dev/docs/cli/mcp/configuration/#example-configurations)
### Local server with environment variables[](https://kiro.dev/docs/cli/mcp/configuration/#local-server-with-environment-variables)
json
```

{
  "mcpServers": {
    "web-search": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-bravesearch"
      ],
      "env": {
        "BRAVE_API_KEY": "${BRAVE_API_KEY}"
      }
    }
  }
}


```

### Remote server with headers[](https://kiro.dev/docs/cli/mcp/configuration/#remote-server-with-headers)
json
```

{
  "mcpServers": {
    "api-server": {
      "url": "https://api.example.com/mcp",
      "headers": {
        "Authorization": "Bearer ${API_TOKEN}",
        "X-Custom-Header": "value"
      }
    }
  }
}


```

### Multiple servers[](https://kiro.dev/docs/cli/mcp/configuration/#multiple-servers)
json
```

{
  "mcpServers": {
    "fetch": {
      "command": "uvx",
      "args": ["mcp-server-fetch"]
    },
    "git": {
      "command": "uvx",
      "args": ["mcp-server-git"],
      "env": {
        "GIT_CONFIG_GLOBAL": "/dev/null"
      }
    },
    "aws-docs": {
      "command": "npx",
      "args": ["-y", "@aws/aws-documentation-mcp-server"]
    }
  }
}


```

## MCP server loading priority[](https://kiro.dev/docs/cli/mcp/configuration/#mcp-server-loading-priority)
When multiple configurations define the same MCP server, they are loaded based on this hierarchy (highest to lowest priority):
  1. **Agent Config** - `mcpServers` field in agent JSON
  2. **Workspace MCP JSON** - `.kiro/settings/mcp.json`
  3. **Global MCP JSON** - `~/.kiro/settings/mcp.json`


### Example scenarios[](https://kiro.dev/docs/cli/mcp/configuration/#example-scenarios)
**Complete override:**
```

Agent config:     { "fetch": { command: "fetch-v2" } }
Workspace config: { "fetch": { command: "fetch-v1" } }
Global config:    { "fetch": { command: "fetch-old" } }

Result: Only "fetch-v2" from agent config is used


```

**Additive (different names):**
```

Agent config:     { "fetch": {...} }
Workspace config: { "git": {...} }
Global config:    { "aws": {...} }

Result: All three servers are used (fetch, git, aws)


```

**Disable via override:**
```

Agent config:     { "fetch": { command: "...", disabled: true } }
Workspace config: { "fetch": { command: "..." } }

Result: No fetch server is launched


```

## Environment variables[](https://kiro.dev/docs/cli/mcp/configuration/#environment-variables)
Many MCP servers require environment variables for authentication or configuration. Use the `${VARIABLE_NAME}` syntax to reference environment variables:
json
```

{
  "mcpServers": {
    "server-name": {
      "env": {
        "API_KEY": "${YOUR_API_KEY}",
        "DEBUG": "true",
        "TIMEOUT": "30000"
      }
    }
  }
}


```

Make sure to set these environment variables in your shell before running Kiro CLI:
bash
```

export YOUR_API_KEY="your-actual-key"
export DEBUG="true"


```

## Disabling servers[](https://kiro.dev/docs/cli/mcp/configuration/#disabling-servers)
To temporarily disable an MCP server without removing its configuration:
json
```

{
  "mcpServers": {
    "server-name": {
      "disabled": true
    }
  }
}


```

## Disabling specific tools[](https://kiro.dev/docs/cli/mcp/configuration/#disabling-specific-tools)
To prevent an agent from using specific tools from an MCP server:
json
```

{
  "mcpServers": {
    "server-name": {
      "disabledTools": ["delete_file", "execute_command"]
    }
  }
}


```

## Viewing loaded servers[](https://kiro.dev/docs/cli/mcp/configuration/#viewing-loaded-servers)
To see which MCP servers are currently loaded in an interactive chat session:
bash
```

/mcp


```

This displays all active MCP servers and their available tools.
## Troubleshooting configuration[](https://kiro.dev/docs/cli/mcp/configuration/#troubleshooting-configuration)
  1. **Validate JSON syntax**
     * Ensure your JSON is valid with no syntax errors:
     * Check for missing commas, quotes, or brackets
     * Use a JSON validator or linter
  2. **Verify command paths**
     * Make sure the command specified exists in your PATH
     * Try running the command directly in your terminal
  3. **Check environment variables**
     * Verify that all required environment variables are set
     * Check for typos in environment variable names
  4. **Review configuration loading**
     * Check which configuration files are being loaded and their priority:
bash
```

# Check workspace config
cat .kiro/settings/mcp.json

# Check user config
cat ~/.kiro/settings/mcp.json


```



## Security considerations[](https://kiro.dev/docs/cli/mcp/configuration/#security-considerations)
When configuring MCP servers, follow these security best practices:
  * Use environment variable references (e.g., `${API_TOKEN}`) instead of hardcoding sensitive values
  * Never commit configuration files with credentials to version control
  * Only connect to trusted remote servers
  * Use `disabledTools` to restrict access to dangerous operations


For comprehensive security guidance, see the [MCP Security Best Practices](https://kiro.dev/docs/cli/mcp/security) page.
Page updated: December 9, 2025
[MCP](https://kiro.dev/docs/cli/mcp/)
[Examples](https://kiro.dev/docs/cli/mcp/examples/)
On this page
  * [Configuration file structure](https://kiro.dev/docs/cli/mcp/configuration/#configuration-file-structure)
  * [Configuration properties](https://kiro.dev/docs/cli/mcp/configuration/#configuration-properties)
  * [Local server](https://kiro.dev/docs/cli/mcp/configuration/#local-server)
  * [Remote server](https://kiro.dev/docs/cli/mcp/configuration/#remote-server)
  * [Example configurations](https://kiro.dev/docs/cli/mcp/configuration/#example-configurations)
  * [Local server with environment variables](https://kiro.dev/docs/cli/mcp/configuration/#local-server-with-environment-variables)
  * [Remote server with headers](https://kiro.dev/docs/cli/mcp/configuration/#remote-server-with-headers)
  * [Multiple servers](https://kiro.dev/docs/cli/mcp/configuration/#multiple-servers)
  * [MCP server loading priority](https://kiro.dev/docs/cli/mcp/configuration/#mcp-server-loading-priority)
  * [Example scenarios](https://kiro.dev/docs/cli/mcp/configuration/#example-scenarios)
  * [Environment variables](https://kiro.dev/docs/cli/mcp/configuration/#environment-variables)
  * [Disabling servers](https://kiro.dev/docs/cli/mcp/configuration/#disabling-servers)
  * [Disabling specific tools](https://kiro.dev/docs/cli/mcp/configuration/#disabling-specific-tools)
  * [Viewing loaded servers](https://kiro.dev/docs/cli/mcp/configuration/#viewing-loaded-servers)
  * [Troubleshooting configuration](https://kiro.dev/docs/cli/mcp/configuration/#troubleshooting-configuration)
  * [Security considerations](https://kiro.dev/docs/cli/mcp/configuration/#security-considerations)