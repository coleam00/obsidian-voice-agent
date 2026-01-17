# Model Context Protocol (MCP)
Model Context Protocol (MCP) extends Kiro's capabilities by connecting to specialized servers that provide additional tools and context. This guide helps you set up, configure, and use MCP servers with Kiro CLI.
**Tip**
Within an interactive chat session, you can use the `/mcp` slash command to see which MCP servers are currently loaded. See [Slash Commands](https://kiro.dev/docs/cli/reference/slash-commands) for more details.
## What is MCP?[](https://kiro.dev/docs/cli/mcp/#what-is-mcp)
MCP is a protocol that allows Kiro to communicate with external servers to access specialized tools and information. For example, the AWS Documentation MCP server provides tools to search, read, and get recommendations from AWS documentation directly within Kiro.
With MCP, you can:
  * Access specialized knowledge bases and documentation
  * Integrate with external services and APIs
  * Extend Kiro's capabilities with domain-specific tools
  * Create custom tools for your specific workflows


## Setting up MCP[](https://kiro.dev/docs/cli/mcp/#setting-up-mcp)
Before using MCP, make sure you have any specific prerequisites for the MCP servers you want to use (listed in each server's documentation)
There are two ways of configuring MCP servers in Kiro CLI:
### Command line[](https://kiro.dev/docs/cli/mcp/#command-line)
bash
```

# Add new MCP server
kiro-cli mcp add \
  --name "awslabs.aws-documentation-mcp-server" \
  --scope global \
  --command "uvx" \
  --args "awslabs.aws-documentation-mcp-server@latest" \
  --env "FASTMCP_LOG_LEVEL=ERROR" \
  --env "AWS_DOCUMENTATION_PARTITION=aws"


```

### mcp.json file[](https://kiro.dev/docs/cli/mcp/#mcpjson-file)
MCP servers can be loaded from the MCP configuration file in your workspace (`<project-root>/.kiro/settings/mcp.json`) or from user level settings (`~/.kiro/settings/mcp.json`)
json
```

{
  "mcpServers": {
    "local-server-name": {
      "command": "command-to-run-server",
      "args": ["arg1", "arg2"],
      "env": {
        "ENV_VAR1": "value1",
        "ENV_VAR2": "value2"
      },
      "disabled": false
    }
  }  
}


```

### Agent configuration[](https://kiro.dev/docs/cli/mcp/#agent-configuration)
The `mcpServers` field specifies which MCP servers the agent has access to. Each server is defined with a command and optional arguments.
json
```

{
  "name": "myagent",
  "description": "My special agent",
  "mcpServers": {
    "fetch": {
      "command": "fetch3.1",
      "args": []
    }
  },
  "includeMcpJson": false
}


```

The `includeMcpJson` field determines whether to include MCP servers defined in the workspace and user level MCP configuration files. When set to `true`, the agent will have access to all MCP servers defined in the user and workspace level configurations in addition to those defined in the agent's `mcpServers` field.
## Troubleshooting[](https://kiro.dev/docs/cli/mcp/#troubleshooting)
### Common issues and solutions[](https://kiro.dev/docs/cli/mcp/#common-issues-and-solutions)
Issue | Solution  
---|---  
Connection failures | Verify prerequisites are installed correctly  
Permission errors | Check that tokens and API keys are valid  
Tool not responding | Review MCP logs for specific error messages  
Configuration not loading | Validate JSON syntax and save the config file  
## Additional resources[](https://kiro.dev/docs/cli/mcp/#additional-resources)
  * [Official MCP Documentation](https://modelcontextprotocol.io/introduction)


## Next steps[](https://kiro.dev/docs/cli/mcp/#next-steps)
Now that you understand MCP basics, explore these resources:
  * **[Examples](https://kiro.dev/docs/cli/mcp/examples/)** - Practical examples of using MCP servers with Kiro CLI
  * **[Security Best Practices](https://kiro.dev/docs/cli/mcp/security/)** - Best practices for secure MCP usage


Page updated: December 9, 2025
[Troubleshooting](https://kiro.dev/docs/cli/custom-agents/troubleshooting/)
[Configuration](https://kiro.dev/docs/cli/mcp/configuration/)
On this page
  * [What is MCP?](https://kiro.dev/docs/cli/mcp/#what-is-mcp)
  * [Setting up MCP](https://kiro.dev/docs/cli/mcp/#setting-up-mcp)
  * [Command line](https://kiro.dev/docs/cli/mcp/#command-line)
  * [mcp.json file](https://kiro.dev/docs/cli/mcp/#mcpjson-file)
  * [Agent configuration](https://kiro.dev/docs/cli/mcp/#agent-configuration)
  * [Troubleshooting](https://kiro.dev/docs/cli/mcp/#troubleshooting)
  * [Common issues and solutions](https://kiro.dev/docs/cli/mcp/#common-issues-and-solutions)
  * [Additional resources](https://kiro.dev/docs/cli/mcp/#additional-resources)
  * [Next steps](https://kiro.dev/docs/cli/mcp/#next-steps)