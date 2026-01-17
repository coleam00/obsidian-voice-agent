# Creating custom agents
Custom agents allow you to tailor Kiro CLI behavior for specific tasks by defining which tools are available, what permissions are granted, and what context is automatically included.
## Quick start[](https://kiro.dev/docs/cli/custom-agents/creating/#quick-start)
You can create an agent configuration using a slash command from within a Kiro CLI chat session. It will guide you through the process of configuring the agent:
```

> /agent generate

✔ Enter agent name:  · backend-specialist
✔ Enter agent description:  · You are specialist in backend coding practices 
✔ Agent scope · Local (current workspace)
Select MCP servers (use Space to toggle, Enter to confirm): markdown-downloader (node), code-analysis (uv)

✓ Agent 'backend-specialist' has been created and saved successfully!


```

Alternatively, you can also use the CLI command to create a new custom agent:
bash
```

kiro-cli agent create --name my-agent


```

This will guide you through the setup process and create a configuration file at `~/.kiro/agents/my-agent.json`.
## Agent configuration file[](https://kiro.dev/docs/cli/custom-agents/creating/#agent-configuration-file)
Custom agents are defined using JSON configuration files. Here's a basic example:
json
```

{
  "name": "my-agent",
  "description": "A custom agent for my workflow",
  "tools": ["read","write"],
  "allowedTools": ["read"],
  "resources": ["file://README.md", "file://.kiro/steering/**/*.md"],
  "prompt": "You are a helpful coding assistant",
  "model": "claude-sonnet-4"
}


```

## Using your custom agent[](https://kiro.dev/docs/cli/custom-agents/creating/#using-your-custom-agent)
Start a new chat session - which uses the default agent ("kiro_default") and swap to an agent using the agent slash command
bash
```

> /agent swap

 Choose one of the following agents 
❯ rust-developer-agent
  kiro_default
  backend-specialist


```

After selecting an agent, you will see the following:
bash
```

✔ Choose one of the following agents · backend-specialist

[backend-specialist] > 


```

Alternatively, start a chat session with your custom agent:
bash
```

kiro-cli --agent my-agent


```

## Next steps[](https://kiro.dev/docs/cli/custom-agents/creating/#next-steps)
  * Explore [Agent Configuration](https://kiro.dev/docs/cli/custom-agents/configuration-reference) options in detail


Page updated: November 18, 2025
[Custom agents](https://kiro.dev/docs/cli/custom-agents/)
[Configuration reference](https://kiro.dev/docs/cli/custom-agents/configuration-reference/)
On this page
  * [Quick start](https://kiro.dev/docs/cli/custom-agents/creating/#quick-start)
  * [Agent configuration file](https://kiro.dev/docs/cli/custom-agents/creating/#agent-configuration-file)
  * [Using your custom agent](https://kiro.dev/docs/cli/custom-agents/creating/#using-your-custom-agent)
  * [Next steps](https://kiro.dev/docs/cli/custom-agents/creating/#next-steps)