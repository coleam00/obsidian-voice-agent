# Troubleshooting custom agents
## Overview[](https://kiro.dev/docs/cli/custom-agents/troubleshooting/#overview)
This guide helps you diagnose and resolve common issues when creating and using custom agents in Kiro CLI.
### Configuration errors[](https://kiro.dev/docs/cli/custom-agents/troubleshooting/#configuration-errors)
#### Invalid JSON syntax[](https://kiro.dev/docs/cli/custom-agents/troubleshooting/#invalid-json-syntax)
**Problem** : Custom agent fails to load with JSON parsing errors.
**Symptoms** :
  * Error messages mentioning "invalid JSON" or "syntax error"
  * Custom agent not appearing in /agent list
  * Fallback to default agent behavior


**Solutions** :
  * Validate your JSON using a JSON validator or linter
  * Check for common JSON errors: 
    * Missing commas between array elements or object properties
    * Trailing commas after the last element
    * Unmatched brackets or braces
    * Unescaped quotes in string values
  * Use `/agent schema` to verify your configuration structure


#### Schema validation errors[](https://kiro.dev/docs/cli/custom-agents/troubleshooting/#schema-validation-errors)
**Problem** : Custom agent configuration doesn't match the expected schema.
**Symptoms** :
  * Warnings about unknown configuration fields
  * Custom agent behavior not matching configuration
  * Missing required fields errors


**Solutions** :
  * Compare your configuration against the schema using /agent schema
  * Check field names for typos (e.g., allowedTools vs allowedTool)
  * Verify data types match schema requirements (arrays vs strings, booleans vs strings)


### Custom agent loading issues[](https://kiro.dev/docs/cli/custom-agents/troubleshooting/#custom-agent-loading-issues)
#### Custom agent not found[](https://kiro.dev/docs/cli/custom-agents/troubleshooting/#custom-agent-not-found)
**Problem** : Custom agent doesn't appear in the list or can't be used.
**Symptoms** :
  * `/agent list` doesn't show your custom agent
  * Fallback to default agent without warning


**Solutions** :
  * Verify the custom agent file is in the correct location: 
    * Global: `~/.kiro/agents/[name].json`
    * Workspace: `.kiro/agents/[name].json`
  * Check file permissions - ensure the file is readable
  * Verify the filename matches the custom agent name you're trying to use
  * Ensure the file has a .json extension


#### Wrong custom agent version loading[](https://kiro.dev/docs/cli/custom-agents/troubleshooting/#wrong-custom-agent-version-loading)
**Problem** : A different version of your custom agent is loading than expected.
**Symptoms** :
  * Custom agent behavior doesn't match your recent configuration changes
  * Warning message about custom agent conflicts
  * Unexpected tool availability or permissions


**Solutions** :
  * Check for custom agent name conflicts between local and global directories
  * Remember that local custom agents take precedence over global custom agents
  * Use /agent list to see which version is being loaded
  * Remove or rename conflicting custom agent files if necessary


### Tool permission problems[](https://kiro.dev/docs/cli/custom-agents/troubleshooting/#tool-permission-problems)
### Tool not available[](https://kiro.dev/docs/cli/custom-agents/troubleshooting/#tool-not-available)
**Problem** : Custom agent can't access a tool you've configured.
**Symptoms** :
  * Error messages about unknown or unavailable tools
  * Custom agent asking for permission for tools in allowedTools
  * MCP server tools not working


**Solutions** :
  * Verify tool names are spelled correctly in the tools array
  * For MCP tools, ensure the server is properly configured in mcpServers
  * Check that MCP servers are running and accessible
  * Use correct syntax for MCP tools: @server_name/tool_name
  * Verify built-in tool names against the built-in tools documentation


#### /tools command returns empty list[](https://kiro.dev/docs/cli/custom-agents/troubleshooting/#tools-command-returns-empty-list)
**Problem** : The /tools command shows no available tools or fewer tools than expected.
**Symptoms** :
  * `/tools` returns an empty list
  * Expected tools are missing from the tools list
  * Custom agent appears to have no capabilities


**Common causes** :
  * Empty tools array in the custom agent configuration
  * Typos in tool names within the tools array
  * Incorrect MCP server tool names (missing server prefix)
  * MCP server configuration issues preventing tool loading


**Solutions** :
  * Check that your custom agent configuration includes a tools array with valid tool names
  * Verify tool names are spelled correctly (case-sensitive)
  * For MCP tools, ensure you're using the correct server-prefixed format: `@server-name___tool-name`
  * Test with the default agent to confirm tools are available `/tools`
  * Check MCP server status if using external tools


#### Unexpected permission prompts[](https://kiro.dev/docs/cli/custom-agents/troubleshooting/#unexpected-permission-prompts)
**Problem** : Custom agent prompts for permission for tools you thought were pre-approved.
**Symptoms** :
  * Permission prompts for tools listed in `allowedTools`
  * Workflow interruptions despite custom agent configuration


**Solutions** :
  * Ensure tools are listed in both tools and allowedTools arrays
  * Check for typos in tool names between the two arrays
  * For MCP tools, use the full server-prefixed name in`allowedTools`
  * Verify that toolAliases are correctly applied


### Debugging custom agent behavior[](https://kiro.dev/docs/cli/custom-agents/troubleshooting/#debugging-custom-agent-behavior)
#### Missing context or resources[](https://kiro.dev/docs/cli/custom-agents/troubleshooting/#missing-context-or-resources)
**Problem** : Custom agent doesn't seem to have access to expected files or context.
**Solutions** :
  * Verify file paths in the resources array are correct and files exist
  * Check that glob patterns in resources are matching the intended files
  * Ensure hook commands are executing successfully and producing output
  * Test hook commands manually to verify they work in your environment
  * Check hook timeout settings if commands are being cut off


#### MCP server issues[](https://kiro.dev/docs/cli/custom-agents/troubleshooting/#mcp-server-issues)
**Problem** : MCP servers aren't working or tools aren't available.
**Solutions** :
  * Verify MCP server commands are correct and executables are in your PATH
  * Check that required environment variables are set
  * Test MCP servers independently to ensure they're working
  * Review MCP server logs for error messages
  * Increase timeout values if servers are slow to start


#### Testing custom agent configurations[](https://kiro.dev/docs/cli/custom-agents/troubleshooting/#testing-custom-agent-configurations)
To systematically test your custom agent configuration:
  * Validate JSON syntax using a JSON validator
  * Check configuration against schema using /agent schema
  * Test custom agent loading with `/agent list`
  * Switch to the custom agent with `/agent swap [name]`
  * Test each tool individually to verify access and permissions
  * Verify that resources and hooks are providing expected context
  * Test common workflows to ensure the custom agent behaves as expected


## Next steps[](https://kiro.dev/docs/cli/custom-agents/troubleshooting/#next-steps)
  * Review the [Configuration reference](https://kiro.dev/docs/cli/custom-agents/configuration-reference) for detailed options
  * Check [Examples](https://kiro.dev/docs/cli/custom-agents/examples) for working configurations
  * Learn about [Creating custom agents](https://kiro.dev/docs/cli/custom-agents/creating)


Page updated: November 16, 2025
[Examples](https://kiro.dev/docs/cli/custom-agents/examples/)
[MCP](https://kiro.dev/docs/cli/mcp/)
On this page
  * [Overview](https://kiro.dev/docs/cli/custom-agents/troubleshooting/#overview)
  * [Configuration errors](https://kiro.dev/docs/cli/custom-agents/troubleshooting/#configuration-errors)
  * [Invalid JSON syntax](https://kiro.dev/docs/cli/custom-agents/troubleshooting/#invalid-json-syntax)
  * [Schema validation errors](https://kiro.dev/docs/cli/custom-agents/troubleshooting/#schema-validation-errors)
  * [Custom agent loading issues](https://kiro.dev/docs/cli/custom-agents/troubleshooting/#custom-agent-loading-issues)
  * [Custom agent not found](https://kiro.dev/docs/cli/custom-agents/troubleshooting/#custom-agent-not-found)
  * [Wrong custom agent version loading](https://kiro.dev/docs/cli/custom-agents/troubleshooting/#wrong-custom-agent-version-loading)
  * [Tool permission problems](https://kiro.dev/docs/cli/custom-agents/troubleshooting/#tool-permission-problems)
  * [Tool not available](https://kiro.dev/docs/cli/custom-agents/troubleshooting/#tool-not-available)
  * [/tools command returns empty list](https://kiro.dev/docs/cli/custom-agents/troubleshooting/#tools-command-returns-empty-list)
  * [Unexpected permission prompts](https://kiro.dev/docs/cli/custom-agents/troubleshooting/#unexpected-permission-prompts)
  * [Debugging custom agent behavior](https://kiro.dev/docs/cli/custom-agents/troubleshooting/#debugging-custom-agent-behavior)
  * [Missing context or resources](https://kiro.dev/docs/cli/custom-agents/troubleshooting/#missing-context-or-resources)
  * [MCP server issues](https://kiro.dev/docs/cli/custom-agents/troubleshooting/#mcp-server-issues)
  * [Testing custom agent configurations](https://kiro.dev/docs/cli/custom-agents/troubleshooting/#testing-custom-agent-configurations)
  * [Next steps](https://kiro.dev/docs/cli/custom-agents/troubleshooting/#next-steps)