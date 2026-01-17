# Settings
Kiro CLI provides extensive customization through settings. You can configure everything from telemetry to chat behavior, key bindings, and feature toggles.
## Accessing settings[](https://kiro.dev/docs/cli/reference/settings/#accessing-settings)
Manage settings directly from the command line:
bash
```

# List all configured settings
kiro-cli settings list

# List all available settings with descriptions
kiro-cli settings list --all

# View a specific setting
kiro-cli settings telemetry.enabled

# Set a setting
kiro-cli settings telemetry.enabled true

# Delete a setting
kiro-cli settings --delete chat.defaultModel

# Open settings file in editor
kiro-cli settings open


```

### Output formats[](https://kiro.dev/docs/cli/reference/settings/#output-formats)
bash
```

# Plain text (default)
kiro-cli settings list

# JSON
kiro-cli settings list --format json

# Formatted JSON
kiro-cli settings list --format json-pretty


```

## Settings reference[](https://kiro.dev/docs/cli/reference/settings/#settings-reference)
### Telemetry and privacy[](https://kiro.dev/docs/cli/reference/settings/#telemetry-and-privacy)
Setting | Type | Description | Example  
---|---|---|---  
`telemetry.enabled` | boolean | Enable/disable telemetry collection | `kiro-cli settings telemetry.enabled true`  
`telemetryClientId` | string | Client identifier for telemetry | `kiro-cli settings telemetryClientId "client-123"`  
### Chat interface[](https://kiro.dev/docs/cli/reference/settings/#chat-interface)
Setting | Type | Description | Example  
---|---|---|---  
`chat.defaultModel` | string | Default AI model for conversations | `kiro-cli settings chat.defaultModel "claude-3-sonnet"`  
`chat.defaultAgent` | string | Default agent configuration | `kiro-cli settings chat.defaultAgent "my-agent"`  
`chat.greeting.enabled` | boolean | Show greeting message on chat start | `kiro-cli settings chat.greeting.enabled false`  
`chat.editMode` | boolean | Enable edit mode for chat interface | `kiro-cli settings chat.editMode true`  
`chat.enableNotifications` | boolean | Enable desktop notifications | `kiro-cli settings chat.enableNotifications true`  
`chat.disableMarkdownRendering` | boolean | Disable markdown formatting | `kiro-cli settings chat.disableMarkdownRendering false`  
`chat.disableAutoCompaction` | boolean | Disable automatic conversation summarization | `kiro-cli settings chat.disableAutoCompaction true`  
`chat.enableHistoryHints` | boolean | Show conversation history hints | `kiro-cli settings chat.enableHistoryHints true`  
`chat.uiMode` | string | UI variant to use | `kiro-cli settings chat.uiMode "compact"`  
`chat.enableContextUsageIndicator` | boolean | Show context usage percentage in prompt | `kiro-cli settings chat.enableContextUsageIndicator true`  
### Knowledge base[](https://kiro.dev/docs/cli/reference/settings/#knowledge-base)
Setting | Type | Description | Example  
---|---|---|---  
`chat.enableKnowledge` | boolean | Enable knowledge base functionality | `kiro-cli settings chat.enableKnowledge true`  
`knowledge.defaultIncludePatterns` | array | Default file patterns to include | `kiro-cli settings knowledge.defaultIncludePatterns '["*.py", "*.js"]'`  
`knowledge.defaultExcludePatterns` | array | Default file patterns to exclude | `kiro-cli settings knowledge.defaultExcludePatterns '["*.log", "node_modules"]'`  
`knowledge.maxFiles` | number | Maximum files for indexing | `kiro-cli settings knowledge.maxFiles 1000`  
`knowledge.chunkSize` | number | Text chunk size for processing | `kiro-cli settings knowledge.chunkSize 512`  
`knowledge.chunkOverlap` | number | Overlap between text chunks | `kiro-cli settings knowledge.chunkOverlap 50`  
`knowledge.indexType` | string | Type of knowledge index | `kiro-cli settings knowledge.indexType "fast"`  
### Key bindings[](https://kiro.dev/docs/cli/reference/settings/#key-bindings)
Setting | Type | Description | Example  
---|---|---|---  
`chat.skimCommandKey` | char | Key for fuzzy search command | `kiro-cli settings chat.skimCommandKey "f"`  
`chat.autocompletionKey` | char | Key for autocompletion hint acceptance | `kiro-cli settings chat.autocompletionKey "Tab"`  
`chat.tangentModeKey` | char | Key for tangent mode toggle | `kiro-cli settings chat.tangentModeKey "t"`  
`chat.delegateModeKey` | char | Key for delegate command | `kiro-cli settings chat.delegateModeKey "d"`  
### Feature toggles[](https://kiro.dev/docs/cli/reference/settings/#feature-toggles)
Setting | Type | Description | Example  
---|---|---|---  
`chat.enableThinking` | boolean | Enable thinking tool for complex reasoning | `kiro-cli settings chat.enableThinking true`  
`chat.enableTangentMode` | boolean | Enable tangent mode feature | `kiro-cli settings chat.enableTangentMode true`  
`introspect.tangentMode` | boolean | Auto-enter tangent mode for introspect | `kiro-cli settings introspect.tangentMode true`  
`chat.enableTodoList` | boolean | Enable todo list feature | `kiro-cli settings chat.enableTodoList true`  
`chat.enableCheckpoint` | boolean | Enable checkpoint feature | `kiro-cli settings chat.enableCheckpoint true`  
`chat.enableDelegate` | boolean | Enable delegate tool | `kiro-cli settings chat.enableDelegate true`  
### API and service[](https://kiro.dev/docs/cli/reference/settings/#api-and-service)
Setting | Type | Description | Example  
---|---|---|---  
`api.timeout` | number | API request timeout in seconds | `kiro-cli settings api.timeout 30`  
### Model context protocol (MCP)[](https://kiro.dev/docs/cli/reference/settings/#model-context-protocol-mcp)
Setting | Type | Description | Example  
---|---|---|---  
`mcp.initTimeout` | number | MCP server initialization timeout | `kiro-cli settings mcp.initTimeout 10`  
`mcp.noInteractiveTimeout` | number | Non-interactive MCP timeout | `kiro-cli settings mcp.noInteractiveTimeout 5`  
`mcp.loadedBefore` | boolean | Track previously loaded MCP servers | `kiro-cli settings mcp.loadedBefore true`  
## Common configuration examples[](https://kiro.dev/docs/cli/reference/settings/#common-configuration-examples)
### Basic setup[](https://kiro.dev/docs/cli/reference/settings/#basic-setup)
bash
```

# Enable telemetry
kiro-cli settings telemetry.enabled true

# Set default chat model
kiro-cli settings chat.defaultModel "claude-3-sonnet"

# Disable greeting message
kiro-cli settings chat.greeting.enabled false


```

### Knowledge base configuration[](https://kiro.dev/docs/cli/reference/settings/#knowledge-base-configuration)
bash
```

# Enable knowledge base
kiro-cli settings chat.enableKnowledge true

# Set file patterns to include
kiro-cli settings knowledge.defaultIncludePatterns '["*.py", "*.js", "*.md", "*.txt"]'

# Set file patterns to exclude
kiro-cli settings knowledge.defaultExcludePatterns '["*.log", "node_modules", ".git", "*.pyc"]'

# Set maximum files to index
kiro-cli settings knowledge.maxFiles 2000


```

### Enable experimental features[](https://kiro.dev/docs/cli/reference/settings/#enable-experimental-features)
bash
```

# Enable thinking tool
kiro-cli settings chat.enableThinking true

# Enable tangent mode
kiro-cli settings chat.enableTangentMode true

# Enable todo lists
kiro-cli settings chat.enableTodoList true

# Enable checkpoints
kiro-cli settings chat.enableCheckpoint true

# Configure key bindings
kiro-cli settings chat.tangentModeKey "t"
kiro-cli settings chat.delegateModeKey "d"


```

### Performance tuning[](https://kiro.dev/docs/cli/reference/settings/#performance-tuning)
bash
```

# Increase API timeout for slow connections
kiro-cli settings api.timeout 60

# Adjust knowledge base chunk size
kiro-cli settings knowledge.chunkSize 1024

# Disable auto-compaction for long conversations
kiro-cli settings chat.disableAutoCompaction true


```

## Troubleshooting settings[](https://kiro.dev/docs/cli/reference/settings/#troubleshooting-settings)
### Invalid setting values[](https://kiro.dev/docs/cli/reference/settings/#invalid-setting-values)
**Boolean values:** Use `true` or `false` (lowercase)
bash
```

kiro-cli settings telemetry.enabled true  # ✓ Correct
kiro-cli settings telemetry.enabled True  # ✗ Wrong


```

**Array values:** Use JSON format with single quotes
bash
```

kiro-cli settings knowledge.defaultIncludePatterns '["*.py", "*.js"]'  # ✓ Correct


```

**String values:** Use quotes for strings with spaces
bash
```

kiro-cli settings chat.defaultModel "claude-3-sonnet"  # ✓ Correct


```

### Resetting settings[](https://kiro.dev/docs/cli/reference/settings/#resetting-settings)
Delete individual settings:
bash
```

kiro-cli settings --delete setting.name


```

Open settings file for manual editing:
bash
```

kiro-cli settings open


```

View current settings to identify issues:
bash
```

kiro-cli settings list --all


```

### Settings file issues[](https://kiro.dev/docs/cli/reference/settings/#settings-file-issues)
If the settings file becomes corrupted:
  1. **Back up current settings:**
bash
```

kiro-cli settings list --format json > backup.json


```

  2. **Open the settings file:**
bash
```

kiro-cli settings open


```

  3. **Verify JSON syntax or restore from backup**


## Settings file location[](https://kiro.dev/docs/cli/reference/settings/#settings-file-location)
Settings are stored in:
  * **macOS** : `~/.kiro/settings.json`
  * **Linux** : `~/.config/kiro/settings.json`


You can edit this file directly, but using `kiro-cli settings` commands is recommended for validation.
## Next steps[](https://kiro.dev/docs/cli/reference/settings/#next-steps)
  * [Configure custom agents](https://kiro.dev/docs/cli/custom-agents/configuration-reference)
  * [Set up MCP servers](https://kiro.dev/docs/cli/mcp)
  * [Enable experimental features](https://kiro.dev/docs/cli/experimental)
  * [CLI Commands Reference](https://kiro.dev/docs/cli/reference/cli-commands)


Page updated: November 18, 2025
[Built-in tools](https://kiro.dev/docs/cli/reference/built-in-tools/)
[Upgrading from Q CLI](https://kiro.dev/docs/cli/migrating-from-q/)
On this page
  * [Accessing settings](https://kiro.dev/docs/cli/reference/settings/#accessing-settings)
  * [Output formats](https://kiro.dev/docs/cli/reference/settings/#output-formats)
  * [Settings reference](https://kiro.dev/docs/cli/reference/settings/#settings-reference)
  * [Telemetry and privacy](https://kiro.dev/docs/cli/reference/settings/#telemetry-and-privacy)
  * [Chat interface](https://kiro.dev/docs/cli/reference/settings/#chat-interface)
  * [Knowledge base](https://kiro.dev/docs/cli/reference/settings/#knowledge-base)
  * [Key bindings](https://kiro.dev/docs/cli/reference/settings/#key-bindings)
  * [Feature toggles](https://kiro.dev/docs/cli/reference/settings/#feature-toggles)
  * [API and service](https://kiro.dev/docs/cli/reference/settings/#api-and-service)
  * [Model context protocol (MCP)](https://kiro.dev/docs/cli/reference/settings/#model-context-protocol-mcp)
  * [Common configuration examples](https://kiro.dev/docs/cli/reference/settings/#common-configuration-examples)
  * [Basic setup](https://kiro.dev/docs/cli/reference/settings/#basic-setup)
  * [Knowledge base configuration](https://kiro.dev/docs/cli/reference/settings/#knowledge-base-configuration)
  * [Enable experimental features](https://kiro.dev/docs/cli/reference/settings/#enable-experimental-features)
  * [Performance tuning](https://kiro.dev/docs/cli/reference/settings/#performance-tuning)
  * [Troubleshooting settings](https://kiro.dev/docs/cli/reference/settings/#troubleshooting-settings)
  * [Invalid setting values](https://kiro.dev/docs/cli/reference/settings/#invalid-setting-values)
  * [Resetting settings](https://kiro.dev/docs/cli/reference/settings/#resetting-settings)
  * [Settings file issues](https://kiro.dev/docs/cli/reference/settings/#settings-file-issues)
  * [Settings file location](https://kiro.dev/docs/cli/reference/settings/#settings-file-location)
  * [Next steps](https://kiro.dev/docs/cli/reference/settings/#next-steps)