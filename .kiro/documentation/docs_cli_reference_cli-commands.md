# CLI commands
This page provides a comprehensive reference for all Kiro CLI commands and their arguments.
## Global arguments[](https://kiro.dev/docs/cli/reference/cli-commands/#global-arguments)
These arguments work with any Kiro CLI command:
Argument | Short | Description  
---|---|---  
`--verbose` | `-v` | Increase logging verbosity (can be repeated: `-v`, `-vv`, `-vvv`)  
`--agent` | `-v` | Start a conversation using a specific custom agent configuration  
`--help` | `-h` | Show help information  
`--version` | `-V` | Show version information  
`--help-all` |  | Print help for all subcommands  
## Commands[](https://kiro.dev/docs/cli/reference/cli-commands/#commands)
### kiro-cli agent[](https://kiro.dev/docs/cli/reference/cli-commands/#kiro-cli-agent)
Manage agent configurations.
**Syntax:**
bash
```

kiro-cli agent [SUBCOMMAND] [OPTIONS]


```

**Subcommands:**
Subcommand | Description  
---|---  
`list` | List the available agents  
`create` | Create an agent config  
`edit` | Edit an existing agent config  
`validate` | Validate a config with the given path  
`migrate` | Migrate profiles to agents (potentially destructive to existing agents)  
`set-default` | Define a default agent to use when starting a session  
**Examples:**
bash
```

kiro-cli agent list
kiro-cli agent create my-agent
kiro-cli agent edit my-agent
kiro-cli agent validate ./my-agent.json
kiro-cli agent set-default my-agent


```

### kiro-cli chat[](https://kiro.dev/docs/cli/reference/cli-commands/#kiro-cli-chat)
Start an interactive chat session with Kiro. When no subcommand is specified, `kiro` defaults to `kiro-cli chat`.
**Syntax:**
bash
```

kiro-cli chat [OPTIONS] [INPUT]


```

**Arguments:**
Argument | Description  
---|---  
`--no-interactive` | Print first response to STDOUT without interactive mode  
`--resume` / `-r` | Resume the previous conversation from this directory  
`--resume-picker` | Open interactive session picker to choose which session to resume  
`--list-sessions` | List all saved chat sessions for the current directory  
`--delete-session <ID>` | Delete a saved chat session by ID  
`--agent` | Specify which agent to use  
`--trust-all-tools` | Allow the model to use any tool without confirmation  
`--trust-tools` | Trust only specified tools (comma-separated list)  
`INPUT` | The first question to ask (positional argument)  
**Examples:**
bash
```

# Start interactive chat
kiro-cli 

# Ask a question directly
kiro-cli chat "How do I list files in Linux?"

# Non-interactive mode with trusted tools
kiro-cli chat --no-interactive --trust-all-tools "Show me the current directory"

# Resume previous conversation
kiro-cli chat --resume

# Open session picker to choose which session to resume
kiro-cli chat --resume-picker

# List all saved sessions
kiro-cli chat --list-sessions

# Use specific agent
kiro-cli chat --agent my-agent "Help me with AWS CLI"


```

### kiro-cli translate[](https://kiro.dev/docs/cli/reference/cli-commands/#kiro-cli-translate)
Translate natural language instructions to executable shell commands using AI.
**Syntax:**
bash
```

kiro-cli translate [OPTIONS] [INPUT...]


```

**Arguments:**
Argument | Short | Description  
---|---|---  
`--n` | `-n` | Number of completions to generate (max 5)  
`INPUT` |  | Natural language description (positional arguments)  
**Examples:**
bash
```

kiro-cli translate "list all files in the current directory"
kiro-cli translate "find all Python files modified in the last week"
kiro-cli translate "compress all log files older than 30 days"
kiro-cli translate -n 3 "search for text in files"


```

### kiro-cli doctor[](https://kiro.dev/docs/cli/reference/cli-commands/#kiro-cli-doctor)
Diagnose and fix common installation and configuration issues.
**Syntax:**
bash
```

kiro-cli doctor [OPTIONS]


```

**Arguments:**
Argument | Short | Description  
---|---|---  
`--all` | `-a` | Run all diagnostic tests without fixes  
`--strict` | `-s` | Error on warnings  
`--format` | `-f` | Output format: `plain`, `json`, `json-pretty`  
**Examples:**
bash
```

kiro-cli doctor
kiro-cli doctor --all
kiro-cli doctor --strict


```

### kiro-cli update[](https://kiro.dev/docs/cli/reference/cli-commands/#kiro-cli-update)
Update Kiro CLI to the latest version.
**Syntax:**
bash
```

kiro-cli update [OPTIONS]


```

**Arguments:**
Argument | Short | Description  
---|---|---  
`--non-interactive` | `-y` | Don't prompt for confirmation  
`--relaunch-dashboard` |  | Relaunch dashboard after update (default: true)  
**Examples:**
bash
```

kiro-cli update
kiro-cli update --non-interactive


```

### kiro-cli theme[](https://kiro.dev/docs/cli/reference/cli-commands/#kiro-cli-theme)
Get or set the visual theme for the autocomplete dropdown menu.
**Syntax:**
bash
```

kiro-cli theme [OPTIONS] [THEME]


```

**Arguments:**
Argument | Description  
---|---  
`--list` | List all available themes  
`--folder` | Show the theme directory path  
`THEME` | Theme name: `dark`, `light`, `system`  
**Examples:**
bash
```

kiro-cli theme --list
kiro-cli theme dark
kiro-cli theme light
kiro-cli theme system


```

### kiro-cli integrations[](https://kiro.dev/docs/cli/reference/cli-commands/#kiro-cli-integrations)
Manage system integrations for Kiro.
**Syntax:**
bash
```

kiro-cli integrations [SUBCOMMAND] [OPTIONS]


```

**Subcommands:**
Subcommand | Description  
---|---  
`install` | Install an integration  
`uninstall` | Uninstall an integration  
`reinstall` | Reinstall an integration  
`status` | Check integration status  
**Options:**
  * `--silent` / `-s`: Suppress status messages
  * `--format` / `-f`: Output format (for status command)


**Examples:**
bash
```

kiro-cli integrations install
kiro-cli integrations status
kiro-cli integrations uninstall --silent


```

### kiro-cli inline[](https://kiro.dev/docs/cli/reference/cli-commands/#kiro-cli-inline)
Manage inline suggestions (ghost text) that appear as you type.
**Syntax:**
bash
```

kiro-cli inline [SUBCOMMAND] [OPTIONS]


```

**Subcommands:**
Subcommand | Description  
---|---  
`enable` | Enable inline suggestions  
`disable` | Disable inline suggestions  
`status` | Show current status  
`set-customization` | Select a customization model  
`show-customizations` | Show available customizations  
**Examples:**
bash
```

kiro-cli inline enable
kiro-cli inline disable
kiro-cli inline status
kiro-cli inline set-customization
kiro-cli inline show-customizations --format json


```

### kiro-cli login[](https://kiro.dev/docs/cli/reference/cli-commands/#kiro-cli-login)
Authenticate with Kiro.
**Syntax:**
bash
```

kiro-cli login [OPTIONS]


```

**Arguments:**
Argument | Description  
---|---  
`--use-device-flow` | Use OAuth device flow for authentication  
**Examples:**
bash
```

kiro-cli login
kiro-cli login --use-device-flow


```

### kiro-cli logout[](https://kiro.dev/docs/cli/reference/cli-commands/#kiro-cli-logout)
Sign out of your kiro-cli session.
**Syntax:**
bash
```

kiro-cli logout


```

### kiro-cli whoami[](https://kiro.dev/docs/cli/reference/cli-commands/#kiro-cli-whoami)
Display information about the current user and authentication status.
**Syntax:**
bash
```

kiro-cli whoami [OPTIONS]


```

**Arguments:**
Argument | Short | Description  
---|---|---  
`--format` | `-f` | Output format: `plain`, `json`, `json-pretty`  
**Examples:**
bash
```

kiro-cli whoami
kiro-cli whoami --format json


```

### kiro-cli settings[](https://kiro.dev/docs/cli/reference/cli-commands/#kiro-cli-settings)
Manage kiro-cli configuration settings.
**Syntax:**
bash
```

kiro-cli settings [SUBCOMMAND] [OPTIONS] [KEY] [VALUE]


```

**Arguments:**
Argument | Short | Description  
---|---|---  
`--delete` | `-d` | Delete a setting  
`--format` | `-f` | Output format: `plain`, `json`, `json-pretty`  
`KEY` |  | Setting key (positional)  
`VALUE` |  | Setting value (positional)  
**Subcommands:**
Subcommand | Description  
---|---  
`open` | Open settings file in default editor  
`list` | List configured settings  
`list --all` | List all available settings with descriptions  
**Examples:**
bash
```

# View all settings
kiro-cli settings list

# View all available settings
kiro-cli settings list --all

# Get a specific setting
kiro-cli settings telemetry.enabled

# Set a setting
kiro-cli settings telemetry.enabled true

# Delete a setting
kiro-cli settings --delete chat.defaultModel

# Open settings file
kiro-cli settings open

# JSON output
kiro-cli settings list --format json-pretty


```

### kiro-cli diagnostic[](https://kiro.dev/docs/cli/reference/cli-commands/#kiro-cli-diagnostic)
Run diagnostic tests to troubleshoot issues.
**Syntax:**
bash
```

kiro-cli diagnostic [OPTIONS]


```

**Arguments:**
Argument | Short | Description  
---|---|---  
`--format` | `-f` | Output format: `plain`, `json`, `json-pretty`  
`--force` |  | Force limited diagnostic output  
### kiro-cli issue[](https://kiro.dev/docs/cli/reference/cli-commands/#kiro-cli-issue)
Create a GitHub issue for feedback or bug reports.
**Syntax:**
bash
```

kiro-cli issue [OPTIONS] [DESCRIPTION...]


```

**Arguments:**
Argument | Short | Description  
---|---|---  
`--force` | `-f` | Force issue creation  
`DESCRIPTION` |  | Issue description (positional)  
**Examples:**
bash
```

kiro-cli issue
kiro-cli issue "Autocomplete not working in zsh"


```

### kiro-cli version[](https://kiro.dev/docs/cli/reference/cli-commands/#kiro-cli-version)
Display version information and changelog.
**Syntax:**
bash
```

kiro-cli version [OPTIONS]


```

**Arguments:**
Argument | Description  
---|---  
`--changelog` | Show changelog for current version  
`--changelog=all` | Show changelog for all versions  
`--changelog=x.x.x` | Show changelog for specific version  
**Examples:**
bash
```

kiro-cli version
kiro-cli version --changelog
kiro-cli version --changelog=all
kiro-cli version --changelog=1.5.0


```

### kiro-cli mcp[](https://kiro.dev/docs/cli/reference/cli-commands/#kiro-cli-mcp)
Manage Model Context Protocol (MCP) servers.
**Syntax:**
bash
```

kiro-cli mcp [SUBCOMMAND] [OPTIONS]


```

**Subcommands:**
#### kiro-cli mcp add[](https://kiro.dev/docs/cli/reference/cli-commands/#kiro-cli-mcp-add)
Add or replace a configured MCP server.
**Arguments:**
Argument | Description  
---|---  
`--name` | Server name (required)  
`--command` | Launch command (required)  
`--scope` | Scope: `workspace` or `global`  
`--env` | Environment variables: `key1=value1,key2=value2`  
`--timeout` | Launch timeout in milliseconds  
`--force` | Overwrite existing server  
**Example:**
bash
```

kiro-cli mcp add --name my-server --command "node server.js" --scope workspace


```

#### kiro-cli mcp remove[](https://kiro.dev/docs/cli/reference/cli-commands/#kiro-cli-mcp-remove)
Remove an MCP server.
**Arguments:**
Argument | Description  
---|---  
`--name` | Server name (required)  
`--scope` | Scope: `workspace` or `global`  
**Example:**
bash
```

kiro-cli mcp remove --name my-server --scope workspace


```

#### kiro-cli mcp list[](https://kiro.dev/docs/cli/reference/cli-commands/#kiro-cli-mcp-list)
List configured MCP servers.
**Syntax:**
bash
```

kiro-cli mcp list [SCOPE]


```

**Example:**
bash
```

kiro-cli mcp list
kiro-cli mcp list workspace
kiro-cli mcp list global


```

#### kiro-cli mcp import[](https://kiro.dev/docs/cli/reference/cli-commands/#kiro-cli-mcp-import)
Import server configuration from a file.
**Arguments:**
Argument | Description  
---|---  
`--file` | Configuration file (required)  
`--force` | Overwrite existing servers  
`SCOPE` | Scope: `workspace` or `global`  
**Example:**
bash
```

kiro-cli mcp import --file config.json workspace


```

#### kiro-cli mcp status[](https://kiro.dev/docs/cli/reference/cli-commands/#kiro-cli-mcp-status)
Get the status of an MCP server.
**Arguments:**
Argument | Description  
---|---  
`--name` | Server name (required)  
**Example:**
bash
```

kiro-cli mcp status --name my-server


```

## Session management[](https://kiro.dev/docs/cli/reference/cli-commands/#session-management)
Kiro CLI automatically saves all chat sessions on every conversation turn. You can resume from any previous chat session at any time.
### From the command line[](https://kiro.dev/docs/cli/reference/cli-commands/#from-the-command-line)
bash
```

# Resume the most recent chat session
kiro-cli chat --resume

# Interactively pick a chat session to resume
kiro-cli chat --resume-picker

# List all saved chat sessions for the current directory
kiro-cli chat --list-sessions

# Delete a saved chat session
kiro-cli chat --delete-session <SESSION_ID>


```

### From within a chat session[](https://kiro.dev/docs/cli/reference/cli-commands/#from-within-a-chat-session)
Use the `/chat` command to manage sessions:
bash
```

# Resume a chat session (interactive selector)
/chat resume

# Save current session to a file
/chat save <FILE_PATH>

# Load a session from a file
/chat load <FILE_PATH>


```

The `.json` extension is optional when loading - Kiro will try both with and without the extension.
### Custom session storage[](https://kiro.dev/docs/cli/reference/cli-commands/#custom-session-storage)
You can use custom scripts to control where chat sessions are saved to and loaded from. This allows you to store sessions in version control systems, cloud storage, databases, or any custom location.
bash
```

# Save session via custom script (receives JSON via stdin)
/chat save-via-script <SCRIPT_PATH>

# Load session via custom script (outputs JSON to stdout)
/chat load-via-script <SCRIPT_PATH>


```

**Tips:**
  * Session IDs are UUIDs that uniquely identify each chat session
  * Sessions are stored per directory, so each project has its own set of sessions
  * The most recently updated sessions appear first in the list


## Log files[](https://kiro.dev/docs/cli/reference/cli-commands/#log-files)
Kiro CLI maintains log files for troubleshooting:
**Locations:**
  * **macOS** : `$TMPDIR/kiro-log/`
  * **Linux** : `$XDG_RUNTIME_DIR` or `/tmp/kiro-log/`


**Log Levels:**
Set via `KIRO_LOG_LEVEL` environment variable:
  * `error`: Only errors (default)
  * `warn`: Warnings and errors
  * `info`: Info, warnings, and errors
  * `debug`: Debug info and above
  * `trace`: All messages including detailed traces


**Example:**
bash
```

# Enable debug logging
export KIRO_LOG_LEVEL=debug
kiro-cli chat

# For fish shell
set -x KIRO_LOG_LEVEL debug
kiro-cli chat


```

**Warning:** Log files may contain sensitive information including file paths, code snippets, and command outputs. Be cautious when sharing logs.
## Next steps[](https://kiro.dev/docs/cli/reference/cli-commands/#next-steps)
  * [Slash Commands Reference](https://kiro.dev/docs/cli/reference/slash-commands)
  * [Settings Configuration](https://kiro.dev/docs/cli/settings)
  * [Troubleshooting Guide](https://kiro.dev/docs/cli/reference/troubleshooting)


Page updated: December 18, 2025
[VPC endpoints (AWS PrivateLink)](https://kiro.dev/docs/cli/privacy-and-security/vpc-endpoints/)
[Slash commands](https://kiro.dev/docs/cli/reference/slash-commands/)
On this page
  * [Global arguments](https://kiro.dev/docs/cli/reference/cli-commands/#global-arguments)
  * [Commands](https://kiro.dev/docs/cli/reference/cli-commands/#commands)
  * [kiro-cli agent](https://kiro.dev/docs/cli/reference/cli-commands/#kiro-cli-agent)
  * [kiro-cli chat](https://kiro.dev/docs/cli/reference/cli-commands/#kiro-cli-chat)
  * [kiro-cli translate](https://kiro.dev/docs/cli/reference/cli-commands/#kiro-cli-translate)
  * [kiro-cli doctor](https://kiro.dev/docs/cli/reference/cli-commands/#kiro-cli-doctor)
  * [kiro-cli update](https://kiro.dev/docs/cli/reference/cli-commands/#kiro-cli-update)
  * [kiro-cli theme](https://kiro.dev/docs/cli/reference/cli-commands/#kiro-cli-theme)
  * [kiro-cli integrations](https://kiro.dev/docs/cli/reference/cli-commands/#kiro-cli-integrations)
  * [kiro-cli inline](https://kiro.dev/docs/cli/reference/cli-commands/#kiro-cli-inline)
  * [kiro-cli login](https://kiro.dev/docs/cli/reference/cli-commands/#kiro-cli-login)
  * [kiro-cli logout](https://kiro.dev/docs/cli/reference/cli-commands/#kiro-cli-logout)
  * [kiro-cli whoami](https://kiro.dev/docs/cli/reference/cli-commands/#kiro-cli-whoami)
  * [kiro-cli settings](https://kiro.dev/docs/cli/reference/cli-commands/#kiro-cli-settings)
  * [kiro-cli diagnostic](https://kiro.dev/docs/cli/reference/cli-commands/#kiro-cli-diagnostic)
  * [kiro-cli issue](https://kiro.dev/docs/cli/reference/cli-commands/#kiro-cli-issue)
  * [kiro-cli version](https://kiro.dev/docs/cli/reference/cli-commands/#kiro-cli-version)
  * [kiro-cli mcp](https://kiro.dev/docs/cli/reference/cli-commands/#kiro-cli-mcp)
  * [kiro-cli mcp add](https://kiro.dev/docs/cli/reference/cli-commands/#kiro-cli-mcp-add)
  * [kiro-cli mcp remove](https://kiro.dev/docs/cli/reference/cli-commands/#kiro-cli-mcp-remove)
  * [kiro-cli mcp list](https://kiro.dev/docs/cli/reference/cli-commands/#kiro-cli-mcp-list)
  * [kiro-cli mcp import](https://kiro.dev/docs/cli/reference/cli-commands/#kiro-cli-mcp-import)
  * [kiro-cli mcp status](https://kiro.dev/docs/cli/reference/cli-commands/#kiro-cli-mcp-status)
  * [Session management](https://kiro.dev/docs/cli/reference/cli-commands/#session-management)
  * [From the command line](https://kiro.dev/docs/cli/reference/cli-commands/#from-the-command-line)
  * [From within a chat session](https://kiro.dev/docs/cli/reference/cli-commands/#from-within-a-chat-session)
  * [Custom session storage](https://kiro.dev/docs/cli/reference/cli-commands/#custom-session-storage)
  * [Log files](https://kiro.dev/docs/cli/reference/cli-commands/#log-files)
  * [Next steps](https://kiro.dev/docs/cli/reference/cli-commands/#next-steps)