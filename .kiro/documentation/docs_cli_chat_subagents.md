# Subagents
Subagents are specialized agents that can autonomously execute complex tasks on your behalf. They have their own context, tool access, and decision-making capabilities, making them ideal for sophisticated multi-step operations.
## Key capabilities[](https://kiro.dev/docs/cli/chat/subagents/#key-capabilities)
  * **Autonomous execution** - Run independently with their own context, with the level of autonomy depending on agent configuration
  * **Live progress tracking** - Monitor real-time status updates as subagents work through tasks
  * **Core tool access** - Read files, execute commands, write files, and use MCP tools
  * **Parallel execution** - Run multiple subagents simultaneously for efficient task execution
  * **Result aggregation** - Results automatically returned to the main agent when complete


## Default subagent[](https://kiro.dev/docs/cli/chat/subagents/#default-subagent)
Kiro includes a default subagent that can handle general-purpose tasks. When you assign a task to a subagent, the default subagent is used unless you specify a custom agent configuration.
## Custom subagents[](https://kiro.dev/docs/cli/chat/subagents/#custom-subagents)
You can spawn subagents using your own agent configurations. This allows you to create specialized subagents tailored to specific workflows:
bash
```

> Use the backend agent to refactor the payment module


```

To use a custom agent as a subagent, reference it by name when assigning tasks. The subagent will inherit the tool access and settings from that agent's configuration.
## How subagents work[](https://kiro.dev/docs/cli/chat/subagents/#how-subagents-work)
  1. **Task assignment** - You describe a task, and Kiro determines if a subagent is appropriate
  2. **Subagent initialization** - The subagent is created with its own context and tool access based on its agent configuration
  3. **Autonomous execution** - The subagent works through the task independently, though it may pause to request user approval for certain tool permissions
  4. **Progress updates** - You receive live progress updates showing current work
  5. **Result return** - When complete, results are returned to the main agent


## Tool availability[](https://kiro.dev/docs/cli/chat/subagents/#tool-availability)
Subagents run in a separate runtime environment. Some tools available in normal chat are not yet implemented in subagents.
**Available tools:**
  * `read` - Read files and directories
  * `write` - Create and edit files
  * `shell` - Execute bash commands
  * MCP tools


**Not available:**
  * `web_search` - Web research
  * `web_fetch` - Fetch URLs
  * `introspect` - CLI info
  * `thinking` - Reasoning tool
  * `todo_list` - Task tracking
  * `use_aws` - AWS commands
  * `grep` - Search file contents
  * `glob` - Find files by pattern


**Agent configuration**
If your custom agent configuration includes tools that aren't available in subagents, those tools will simply be unavailable when the agent runs as a subagent. The agent will still function with the available tools.
## Best practices[](https://kiro.dev/docs/cli/chat/subagents/#best-practices)
  1. **Use for complex tasks** - Most valuable for multi-step operations that benefit from isolation
  2. **Provide clear instructions** - Specific task descriptions lead to better results
  3. **Monitor progress** - Check on long-running subagents periodically
  4. **Review results** - Verify subagent output before acting on recommendations


## Troubleshooting[](https://kiro.dev/docs/cli/chat/subagents/#troubleshooting)
Issue | Solution  
---|---  
Subagent not starting | Verify the task description is clear and actionable  
Missing tool access | Check if the required tool is available in subagent runtime (see table above)  
Incomplete results | Provide more specific instructions or break into smaller tasks  
Page updated: December 18, 2025
[Model selection](https://kiro.dev/docs/cli/chat/model-selection/)
[Planning Agent](https://kiro.dev/docs/cli/chat/planning-agent/)
On this page
  * [Key capabilities](https://kiro.dev/docs/cli/chat/subagents/#key-capabilities)
  * [Default subagent](https://kiro.dev/docs/cli/chat/subagents/#default-subagent)
  * [Custom subagents](https://kiro.dev/docs/cli/chat/subagents/#custom-subagents)
  * [How subagents work](https://kiro.dev/docs/cli/chat/subagents/#how-subagents-work)
  * [Tool availability](https://kiro.dev/docs/cli/chat/subagents/#tool-availability)
  * [Best practices](https://kiro.dev/docs/cli/chat/subagents/#best-practices)
  * [Troubleshooting](https://kiro.dev/docs/cli/chat/subagents/#troubleshooting)