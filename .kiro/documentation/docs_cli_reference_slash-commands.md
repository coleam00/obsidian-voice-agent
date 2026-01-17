# Slash commands
## Overview[](https://kiro.dev/docs/cli/reference/slash-commands/#overview)
Slash commands are special commands you can use within an interactive chat session to quickly perform actions without leaving the conversation. They start with a forward slash (`/`) and provide shortcuts for common tasks.
## Using slash commands[](https://kiro.dev/docs/cli/reference/slash-commands/#using-slash-commands)
Slash commands are only available in interactive chat mode:
bash
```

kiro chat
> /help


```

## Available commands[](https://kiro.dev/docs/cli/reference/slash-commands/#available-commands)
###  `/help`[](https://kiro.dev/docs/cli/reference/slash-commands/#help)
Display available slash commands and their usage.
bash
```

> /help


```

###  `/quit`[](https://kiro.dev/docs/cli/reference/slash-commands/#quit)
Exit the interactive chat session.
bash
```

> /quit


```

Aliases: /exit, /q
###  `/clear`[](https://kiro.dev/docs/cli/reference/slash-commands/#clear)
Clear the current conversation history.
bash
```

> /clear


```

Note: This only clears the display, not the saved conversation.
###  `/context`[](https://kiro.dev/docs/cli/reference/slash-commands/#context)
Manage context files and view context window usage. Context rules determine which files are included in your Kiro session and are derived from the current active agent.
bash
```

# Display context rule configuration and matched files
> /context show

# Add context rules (filenames or glob patterns)
> /context add src/app.js
> /context add "*.py"
> /context add "src/**/*.js"

# Remove specified rules
> /context remove src/app.js

# Remove all rules
> /context clear


```

**Available subcommands:**
  * `show` - Display the context rule configuration and matched files
  * `add` - Add context rules (filenames or glob patterns)
  * `remove` - Remove specified rules


**Notes:**
  * You can add specific files or use glob patterns (e.g., `*.py`, `src/**/*.js`)
  * Agent rules apply only to the current agent
  * Context changes are NOT preserved between chat sessions. To make changes permanent, edit the agent config file.
  * The files matched by these rules provide Kiro with additional information about your project or environment


See [Context Management](https://kiro.dev/docs/cli/chat/context) for detailed documentation.
###  `/model`[](https://kiro.dev/docs/cli/reference/slash-commands/#model)
Switch to a different AI model or set your default model preference.
bash
```

# Show current model
> /model

# Save current model as default for future sessions
> /model set-current-as-default


```

**Available subcommands:**
  * `set-current-as-default` - Persist your current model selection as the default for all future sessions


**Note:** The `set-current-as-default` command saves your current model preference to `~/.kiro/settings/cli.json`, so it will be used automatically in all future chat sessions.
###  `/agent`[](https://kiro.dev/docs/cli/reference/slash-commands/#agent)
Manage agents and switch between different agent configurations.
bash
```

# List all available agents
> /agent list

# Create a new agent
> /agent create my-agent

# Edit an existing agent configuration
> /agent edit my-agent

# Generate an agent configuration using AI
> /agent generate

# Show agent config schema
> /agent schema

# Set default agent for new chat sessions
> /agent set-default my-agent

# Swap to a different agent at runtime
> /agent swap code-reviewer


```

**Available subcommands:**
  * `list` - List all available agents
  * `create` - Create a new agent with the specified name
  * `edit` - Edit an existing agent configuration
  * `generate` - Generate an agent configuration using AI
  * `schema` - Show agent config schema
  * `set-default` - Define a default agent to use when kiro-cli chat launches
  * `swap` - Swap to a new agent at runtime


**Notes:**
  * Agents can be stored globally in `~/.kiro/agents/` or per-workspace in `.kiro/agents/`
  * Launch kiro-cli chat with a specific agent using `kiro-cli chat --agent agent_name`
  * Set default agent with `kiro-cli settings chat.defaultAgent agent_name`


See [Custom Agents](https://kiro.dev/docs/cli/custom-agents) for detailed documentation.
###  `/chat`[](https://kiro.dev/docs/cli/reference/slash-commands/#chat)
Manage chat sessions, including saving, loading, and switching between sessions. Kiro CLI automatically saves all chat sessions on every conversation turn.
bash
```

# Open interactive session picker to resume a previous session
> /chat resume

# Save current session to a file
> /chat save /myproject/codereview.json

# Load a session from a file
> /chat load /myproject/codereview.json


```

**Available subcommands:**
  * `resume` - Open interactive session picker to choose a session to resume
  * `save` - Save current session to a file
  * `load` - Load a session from a file (`.json` extension is optional)
  * `save-via-script` - Save session using a custom script (receives JSON via stdin)
  * `load-via-script` - Load session using a custom script (outputs JSON to stdout)


**Notes:**
  * Sessions are automatically saved on every conversation turn
  * Sessions are stored per directory, so each project has its own set of sessions
  * The session picker shows session name, last activity, and message preview
  * Use keyboard shortcuts in the picker: `↑`/`↓` to navigate, `Enter` to select, `/` to filter


#### Custom session storage[](https://kiro.dev/docs/cli/reference/slash-commands/#custom-session-storage)
You can use custom scripts to control where chat sessions are saved to and loaded from. This allows you to store sessions in version control systems, cloud storage, databases, or any custom location.
**Save via script:**
bash
```

> /chat save-via-script ./scripts/save-to-git.sh


```

Your script receives the chat session JSON via stdin. Example script to save to Git notes:
bash
```

#!/bin/bash
set -ex
COMMIT=$(git rev-parse HEAD)
TEMP=$(mktemp)
cat > "$TEMP"
git notes --ref=kiro/notes add -F "$TEMP" "$COMMIT" --force
rm "$TEMP"
echo "Saved to commit ${COMMIT:0:8}" >&2


```

**Load via script:**
bash
```

> /chat load-via-script ./scripts/load-from-git.sh


```

Your script should output the chat session JSON to stdout. Example script to load from Git notes:
bash
```

#!/bin/bash
set -ex
COMMIT=$(git rev-parse HEAD)
git notes --ref=kiro/notes show "$COMMIT"


```

###  `/save`[](https://kiro.dev/docs/cli/reference/slash-commands/#save)
Save the current conversation to a file.
bash
```

# Save <PATH>
> /save /myproject/codereview.json


```

###  `/load`[](https://kiro.dev/docs/cli/reference/slash-commands/#load)
Load a previously saved conversation.
bash
```

# List available conversations
> /load /myproject/codereview.json


```

###  `/editor`[](https://kiro.dev/docs/cli/reference/slash-commands/#editor)
Open your default editor (defaults to vi) to compose a prompt.
bash
```

> /editor


```

Opens `$EDITOR` to compose a longer message.
###  `/reply`[](https://kiro.dev/docs/cli/reference/slash-commands/#reply)
Open your editor with the most recent assistant message quoted for reply.
bash
```

> /reply


```

Useful for referencing and responding to specific parts of the AI's response.
###  `/compact`[](https://kiro.dev/docs/cli/reference/slash-commands/#compact)
Summarize the conversation to free up context space.
bash
```

> /compact


```

Condenses the conversation history while preserving key information, useful when approaching context limits.
###  `/paste`[](https://kiro.dev/docs/cli/reference/slash-commands/#paste)
Paste an image from clipboard.
bash
```

> /paste


```

Adds an image from your system clipboard to the conversation.
###  `/tools`[](https://kiro.dev/docs/cli/reference/slash-commands/#tools)
View tools and permissions. By default, Kiro will ask for your permission to use certain tools. You can control which tools you trust so that no confirmation is required.
bash
```

# View all tools and their permissions
> /tools

# Show the input schema for all available tools
> /tools schema

# Trust a specific tool for the session
> /tools trust write

# Revert a tool to per-request confirmation
> /tools untrust write

# Trust all tools (equivalent to deprecated /acceptall)
> /tools trust-all

# Reset all tools to default permission levels
> /tools reset


```

**Available subcommands:**
  * `schema` - Show the input schema for all available tools
  * `trust` - Trust a specific tool or tools for the session
  * `untrust` - Revert a tool or tools to per-request confirmation
  * `trust-all` - Trust all tools (equivalent to deprecated /acceptall)
  * `reset` - Reset all tools to default permission levels


**Note:** For permanent tool configuration, see [Agent Configuration Reference](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#tools-field).
###  `/prompts`[](https://kiro.dev/docs/cli/reference/slash-commands/#prompts)
View and retrieve prompts. Prompts are reusable templates that help you quickly access common workflows and tasks. These templates are provided by the MCP servers you have installed and configured.
bash
```

# List available prompts from a tool or show all available prompts
> /prompts list

# Show detailed information about a specific prompt
> /prompts details code-review

# Get a specific prompt by name
> /prompts get code-review [arg]

# Quick retrieval (without /prompts prefix)
> @code-review [arg]

# Create a new local prompt
> /prompts create my-prompt

# Edit an existing local prompt
> /prompts edit my-prompt

# Remove an existing local prompt
> /prompts remove my-prompt


```

**Available subcommands:**
  * `list` - List available prompts from a tool or show all available prompts
  * `details` - Show detailed information about a specific prompt
  * `get` - Get a specific prompt by name
  * `create` - Create a new local prompt
  * `edit` - Edit an existing local prompt
  * `remove` - Remove an existing local prompt


**Quick tip:** To retrieve a prompt directly, use `@<prompt name> [arg]` without the `/prompts get` prefix.
See [Manage Prompts](https://kiro.dev/docs/cli/chat/manage-prompts) for detailed documentation.
###  `/hooks`[](https://kiro.dev/docs/cli/reference/slash-commands/#hooks)
View context hooks.
bash
```

> /hooks


```

Display active context hooks for the current session.
###  `/usage`[](https://kiro.dev/docs/cli/reference/slash-commands/#usage)
Show billing and credits information.
bash
```

> /usage


```

View your current usage statistics and remaining credits.
###  `/mcp`[](https://kiro.dev/docs/cli/reference/slash-commands/#mcp)
See MCP servers loaded.
bash
```

> /mcp


```

Display Model Context Protocol servers currently active.
###  `/code`[](https://kiro.dev/docs/cli/reference/slash-commands/#code)
Manage code intelligence configuration and get feedback.
bash
```

# Initialize code intelligence in the current directory
> /code init

# Force reinitialization in the current directory - restarts LSP servers
> /code init -f

# Get workspace status and LSP server statuses
> /code status

# View LSP logs for troubleshooting
> /code logs # Show last 20 ERROR logs

> /code logs -l INFO            # Show INFO level and above

> /code logs -n 50              # Show last 50 entries

> /code logs -l DEBUG -n 100    # Show last 100 DEBUG+ logs

> /code logs -p ./lsp-logs.json # Export logs to JSON file



```

**Available subcommands:**
  * `init` - initialize LSP servers
  * `status` - Show the detailed status of the LSP servers and workspace status
  * `logs` - View logs


###  `/experiment`[](https://kiro.dev/docs/cli/reference/slash-commands/#experiment)
Toggle experimental features.
bash
```

> /experiment


```

Enable or disable experimental CLI features.
###  `/tangent`[](https://kiro.dev/docs/cli/reference/slash-commands/#tangent)
Create conversation checkpoints to explore side topics.
bash
```

> /tangent


```

Enter or exit [tangent mode](https://kiro.dev/docs/cli/experimental/tangent-mode) to explore tangential topics without disrupting your main conversation. Use `Ctrl+T` as a keyboard shortcut (when tangent mode is enabled).
###  `/todos`[](https://kiro.dev/docs/cli/reference/slash-commands/#todos)
View, manage, and resume to-do lists.
bash
```

# View todo
> /todo

# Add todo
> /todo add "Fix authentication bug"

# Complete todo
> /todo complete 1


```

###  `/issue`[](https://kiro.dev/docs/cli/reference/slash-commands/#issue)
Create a new GitHub issue or make a feature request.
bash
```

> /issue


```

Opens a workflow to submit issues or feature requests to the Kiro team.
###  `/logdump`[](https://kiro.dev/docs/cli/reference/slash-commands/#logdump)
Create a zip file with logs for support investigation.
bash
```

> /logdump


```

Generates a diagnostic log bundle for troubleshooting with support.
###  `/changelog`[](https://kiro.dev/docs/cli/reference/slash-commands/#changelog)
View changelog for Kiro CLI.
bash
```

> /changelog


```

Display recent updates and changes to the CLI.
### Keyboard shortcuts[](https://kiro.dev/docs/cli/reference/slash-commands/#keyboard-shortcuts)
In interactive mode, you can also use:
  * `Ctrl+C` - Cancel current input
  * `Ctrl+J` - To insert new-line for multi-line prompt
  * `Ctrl+S` - Fuzzy search commands and context files, use tab to select multiple items
  * `Ctrl+T` - Toggle tangent mode for isolated conversations (if Tangent mode is enabled)
  * `Up/Down arrows` - Navigate command history


## Next steps[](https://kiro.dev/docs/cli/reference/slash-commands/#next-steps)
  * Learn about [CLI Commands](https://kiro.dev/docs/cli/reference/cli-commands) for terminal usage
  * Explore [Interactive Chat Mode](https://kiro.dev/docs/cli/chat/interactive-mode)
  * Check [Context Management](https://kiro.dev/docs/cli/chat/context) for advanced context handling


Page updated: December 19, 2025
[CLI commands](https://kiro.dev/docs/cli/reference/cli-commands/)
[Built-in tools](https://kiro.dev/docs/cli/reference/built-in-tools/)
On this page
  * [Overview](https://kiro.dev/docs/cli/reference/slash-commands/#overview)
  * [Using slash commands](https://kiro.dev/docs/cli/reference/slash-commands/#using-slash-commands)
  * [Available commands](https://kiro.dev/docs/cli/reference/slash-commands/#available-commands)
  * [`/help`](https://kiro.dev/docs/cli/reference/slash-commands/#help)
  * [`/quit`](https://kiro.dev/docs/cli/reference/slash-commands/#quit)
  * [`/clear`](https://kiro.dev/docs/cli/reference/slash-commands/#clear)
  * [`/context`](https://kiro.dev/docs/cli/reference/slash-commands/#context)
  * [`/model`](https://kiro.dev/docs/cli/reference/slash-commands/#model)
  * [`/agent`](https://kiro.dev/docs/cli/reference/slash-commands/#agent)
  * [`/chat`](https://kiro.dev/docs/cli/reference/slash-commands/#chat)
  * [Custom session storage](https://kiro.dev/docs/cli/reference/slash-commands/#custom-session-storage)
  * [`/save`](https://kiro.dev/docs/cli/reference/slash-commands/#save)
  * [`/load`](https://kiro.dev/docs/cli/reference/slash-commands/#load)
  * [`/editor`](https://kiro.dev/docs/cli/reference/slash-commands/#editor)
  * [`/reply`](https://kiro.dev/docs/cli/reference/slash-commands/#reply)
  * [`/compact`](https://kiro.dev/docs/cli/reference/slash-commands/#compact)
  * [`/paste`](https://kiro.dev/docs/cli/reference/slash-commands/#paste)
  * [`/tools`](https://kiro.dev/docs/cli/reference/slash-commands/#tools)
  * [`/prompts`](https://kiro.dev/docs/cli/reference/slash-commands/#prompts)
  * [`/hooks`](https://kiro.dev/docs/cli/reference/slash-commands/#hooks)
  * [`/usage`](https://kiro.dev/docs/cli/reference/slash-commands/#usage)
  * [`/mcp`](https://kiro.dev/docs/cli/reference/slash-commands/#mcp)
  * [`/code`](https://kiro.dev/docs/cli/reference/slash-commands/#code)
  * [`/experiment`](https://kiro.dev/docs/cli/reference/slash-commands/#experiment)
  * [`/tangent`](https://kiro.dev/docs/cli/reference/slash-commands/#tangent)
  * [`/todos`](https://kiro.dev/docs/cli/reference/slash-commands/#todos)
  * [`/issue`](https://kiro.dev/docs/cli/reference/slash-commands/#issue)
  * [`/logdump`](https://kiro.dev/docs/cli/reference/slash-commands/#logdump)
  * [`/changelog`](https://kiro.dev/docs/cli/reference/slash-commands/#changelog)
  * [Keyboard shortcuts](https://kiro.dev/docs/cli/reference/slash-commands/#keyboard-shortcuts)
  * [Next steps](https://kiro.dev/docs/cli/reference/slash-commands/#next-steps)