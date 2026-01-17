# Security
Security is critical when integrating external MCP servers with your development workflow. The MCP security model in Kiro CLI is designed with these principles:
  1. **Explicit Permission** : Tools require explicit user permission before execution
  2. **Local Execution** : MCP servers run locally on your machine
  3. **Isolation** : Each MCP server runs as a separate process
  4. **Transparency** : Users can see what tools are available and what they do


## Security considerations[](https://kiro.dev/docs/cli/mcp/security/#security-considerations)
When using MCP servers with Kiro CLI, keep these security principles in mind:
### Trust and verification[](https://kiro.dev/docs/cli/mcp/security/#trust-and-verification)
  * Only install MCP servers from trusted sources
  * Review tool descriptions and documentation before installation
  * Check for security advisories and updates


### Access control[](https://kiro.dev/docs/cli/mcp/security/#access-control)
  * Use least-privilege principles for server permissions
  * Limit file system access to necessary directories only
  * Restrict network access where possible
  * Use environment variables for sensitive credentials


### Credential management[](https://kiro.dev/docs/cli/mcp/security/#credential-management)
  * Never hardcode API keys or tokens in configuration files
  * Use environment variables for sensitive data
  * Rotate credentials regularly
  * Store credentials securely using system keychains


### Network security[](https://kiro.dev/docs/cli/mcp/security/#network-security)
  * Use HTTPS for remote MCP servers
  * Verify SSL/TLS certificates
  * Be cautious with servers that require broad network access
  * Monitor network traffic for unusual activity


### Monitoring and auditing[](https://kiro.dev/docs/cli/mcp/security/#monitoring-and-auditing)
  * Review MCP server logs regularly
  * Monitor for unexpected behavior
  * Keep track of installed servers and their permissions
  * Remove unused or untrusted servers promptly


## Best practices[](https://kiro.dev/docs/cli/mcp/security/#best-practices)
### Configuration security[](https://kiro.dev/docs/cli/mcp/security/#configuration-security)
bash
```

# Use environment variables for sensitive data
export MCP_API_KEY="your-secure-key"
export DATABASE_URL="your-connection-string"

# Configure MCP server with environment variables
kiro-cli mcp add my-server --env MCP_API_KEY --env DATABASE_URL


```

## Next steps[](https://kiro.dev/docs/cli/mcp/security/#next-steps)
  * Explore [Examples](https://kiro.dev/docs/cli/mcp/examples)
  * Return to [MCP Overview](https://kiro.dev/docs/cli/mcp)


Page updated: November 16, 2025
[Examples](https://kiro.dev/docs/cli/mcp/examples/)
[Governance](https://kiro.dev/docs/cli/mcp/governance/)
On this page
  * [Security considerations](https://kiro.dev/docs/cli/mcp/security/#security-considerations)
  * [Trust and verification](https://kiro.dev/docs/cli/mcp/security/#trust-and-verification)
  * [Access control](https://kiro.dev/docs/cli/mcp/security/#access-control)
  * [Credential management](https://kiro.dev/docs/cli/mcp/security/#credential-management)
  * [Network security](https://kiro.dev/docs/cli/mcp/security/#network-security)
  * [Monitoring and auditing](https://kiro.dev/docs/cli/mcp/security/#monitoring-and-auditing)
  * [Best practices](https://kiro.dev/docs/cli/mcp/security/#best-practices)
  * [Configuration security](https://kiro.dev/docs/cli/mcp/security/#configuration-security)
  * [Next steps](https://kiro.dev/docs/cli/mcp/security/#next-steps)