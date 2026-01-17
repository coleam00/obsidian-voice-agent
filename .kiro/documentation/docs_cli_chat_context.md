# Context management
## Choosing the right context approach[](https://kiro.dev/docs/cli/chat/context/#choosing-the-right-context-approach)
Kiro offers three ways to provide context, each optimized for different use cases:
Approach | Context Window Impact | Persistence | Best For  
---|---|---|---  
Agent Resources | Always active (consumes tokens) | Persistent across sessions | Essential project files, standards, configs  
Session Context | Always active (consumes tokens) | Current session only | Temporary files, quick experiments  
Knowledge Bases | Only when searched | Persistent across sessions | Large codebases, extensive documentation  
## Decision flowchart[](https://kiro.dev/docs/cli/chat/context/#decision-flowchart)
  1. Use this decision tree to choose the appropriate context approach:
     * Is your content larger than 10MB or contains thousands of files? 
       * Yes → Use Knowledge Bases
       * No → Continue to step 2
  2. Do you need this context in every conversation?
     * Yes → Use Agent Resources
     * No → Use Session Context


### Quick reference[](https://kiro.dev/docs/cli/chat/context/#quick-reference)
  * Essential project files (README, configs, standards) → Agent Resources
  * Large codebases or documentation sets → Knowledge Bases
  * Temporary files for current task → Session Context


## Understanding context window impact[](https://kiro.dev/docs/cli/chat/context/#understanding-context-window-impact)
  * Context files and agent resources consume tokens from your context window on every request, whether referenced or not.


bash
```

> /context show

Agent 
  - .kiro/steering/**/*.md  <project-root>/.kiro/steering/product.md
<project-root>/.kiro/steering/structure.md
<project-root>/.kiro/steering/tech.md
<project-root>/.kiro/steering/testing.md
  - README.md <project-root>/snake/README.md
  - ~/.kiro/steering/**/*.md (no matches)

Session (temporary)
  <none>

5 matched files in use
- <project-root>/.kiro/steering/testing.md (0.1% of context window)
- <project-root>/snake/.kiro/steering/tech.md (0.1% of context window)
- <project-root>/snake/README.md (0.1% of context window)
- <project-root>/snake/.kiro/steering/structure.md (0.2% of context window)
- <project-root>/snake/.kiro/steering/product.md (0.1% of context window)

Context files total: 0.5% of context window


```

  * The output shows:
    * **Agent** : Persistent context from your agent's resources field
    * **Session** : Temporary context added during the current session
  * Context files are limited to 75% of your model's context window. Files exceeding this limit are automatically dropped.
  * Knowledge bases don't consume context window space until searched, making them ideal for large reference materials. For more information, see Knowledge base context (for large datasets).


## Managing context[](https://kiro.dev/docs/cli/chat/context/#managing-context)
Context files contain information you want Kiro to consider during your conversations. These can include project requirements, coding standards, development rules, or any other information that helps Kiro provide more relevant responses.
### Configuring persistent context with agent resources[](https://kiro.dev/docs/cli/chat/context/#configuring-persistent-context-with-agent-resources)
The recommended way to configure context is through the resources field in your agent configuration file. This creates persistent context that is available every time you use the agent.
Add file paths or glob patterns to the resources array in your agent config:
json
```

{
  "name": "my-agent",
  "description": "My development agent",
  "resources": [
    "file://README.md",
    "file://docs/**/*.md",
    "file://src/config.py"
  ]
}


```

Resources must be prefixed with file:// to be included as context files. These files will be automatically available in all chat sessions using this agent.
### Adding temporary session context[](https://kiro.dev/docs/cli/chat/context/#adding-temporary-session-context)
You can temporarily add files to your current chat session using the /context add command. These additions are only available for the current session and will not persist when you start a new chat session.
bash
```

> /context add README.md
Added 1 path(s) to context.


```

**Note** : Context modifications via slash command is temporary.
You can also add multiple files at once using glob patterns:
bash
```

> /context add docs/*.md
Added 3 path(s) to context.



```

To make context changes permanent, add the files to your agent's resources field instead. For more information, see Configuring persistent context with agent resources.
### Knowledge base context (for large datasets)[](https://kiro.dev/docs/cli/chat/context/#knowledge-base-context-for-large-datasets)
For large codebases, documentation sets, or reference materials that would exceed context window limits, use knowledge bases. Knowledge bases provide semantic search capabilities without consuming context window space until searched.
Enable knowledge bases:
kiro-cli settings chat.enableKnowledge true
Add content to a knowledge base:
kiro-cli chat
> /knowledge add /path/to/large-codebase --include "**/*.py" --exclude "node_modules/** "
Knowledge bases are searched on-demand by Kiro when relevant information is needed, making them ideal for large reference materials.
### Viewing context usage[](https://kiro.dev/docs/cli/chat/context/#viewing-context-usage)
To view your current context, use the /context show command:
bash
```

> /context show

Current context window (5.9% used)
|||████████████████████████████████████████████████████████████████ 5.9%

█ Context files 0.9%
█ Tools 0.5%
█ Kiro responses 0.7%
█ Your prompts 3.8%


```

### Removing context[](https://kiro.dev/docs/cli/chat/context/#removing-context)
To remove files from your current session context:
bash
```

> /context remove src/temp-file.py
Removed 1 path(s) from context.


```

To clear all session context, use the /context clear command:
bash
```

> /context clear
Cleared context
Note: Context modifications via slash command is temporary.


```

Note: You cannot remove agent-defined context using /context commands. To permanently remove context, edit your agent's resources field.
## Context management actions[](https://kiro.dev/docs/cli/chat/context/#context-management-actions)
Here are some common reasons for actively managing your context window:
  1. If you find yourself repeatedly adding the same context files using `/context add` commands, consider moving them to your agent's resources field for persistence:


bash
```

# Instead of running these commands every session:
> /context add README.md
> /context add docs/*.md

# Add them to your agent config once:
{
  "resources": [
    "file://README.md",
    "file://docs/**/*.md"
  ]
}


```

You can configure a default agent that includes your preferred context files. This ensures your context is automatically available in new chat sessions without needing to specify the agent each time.
bash
```

   >kiro-cli settings chat.defaultAgent my-project-agent


```

  1. If you have large context files (consume significant part of context window) consider using knowledge base instead of including those files as is. Use cases to consider knowledge: 
     * You have large codebases or documentation sets
     * You need semantic search across extensive materials
     * You want to avoid constant context window consumption
     * Example: Instead of adding a large codebase as context files:


bash
```

# This would consume too many tokens:
> /context add src/**/*.py

# Use knowledge base instead:
> /knowledge add src/ --include "**/*.py" --exclude "__pycache__/**"


```

## Best practices[](https://kiro.dev/docs/cli/chat/context/#best-practices)
### Context file organization[](https://kiro.dev/docs/cli/chat/context/#context-file-organization)
  1. Keep context files focused and relevant to avoid token limits
  2. Use descriptive filenames that indicate their purpose
  3. Organize rules and documentation in logical directory structures
  4. Consider file size - very large files may consume significant tokens


### Performance considerations[](https://kiro.dev/docs/cli/chat/context/#performance-considerations)
  1. Monitor token usage with /context show to stay within limits
  2. Use specific glob patterns rather than overly broad ones
  3. Remove unused context files from agent configurations
  4. Consider splitting large context files into smaller, focused files
  5. Use knowledge bases for large datasets to avoid context window consumption


### Security considerations[](https://kiro.dev/docs/cli/chat/context/#security-considerations)
  1. Avoid including sensitive information in context files
  2. Use `.gitignore` to prevent accidental commits of sensitive context
  3. Review context files regularly to ensure they don't contain outdated information
  4. Be mindful of what information is shared when using context in conversations


## Related documentation[](https://kiro.dev/docs/cli/chat/context/#related-documentation)
  * [Slash Commands](https://kiro.dev/docs/cli/reference/slash-commands) - In-chat context commands
  * [CLI Commands](https://kiro.dev/docs/cli/reference/cli-commands) - Terminal context commands
  * [Interactive Chat Mode](https://kiro.dev/docs/cli/chat/interactive-mode) - Using context in chat


Page updated: November 21, 2025
[Prompts](https://kiro.dev/docs/cli/chat/manage-prompts/)
[Responding to messages](https://kiro.dev/docs/cli/chat/responding/)
On this page
  * [Choosing the right context approach](https://kiro.dev/docs/cli/chat/context/#choosing-the-right-context-approach)
  * [Decision flowchart](https://kiro.dev/docs/cli/chat/context/#decision-flowchart)
  * [Quick reference](https://kiro.dev/docs/cli/chat/context/#quick-reference)
  * [Understanding context window impact](https://kiro.dev/docs/cli/chat/context/#understanding-context-window-impact)
  * [Managing context](https://kiro.dev/docs/cli/chat/context/#managing-context)
  * [Configuring persistent context with agent resources](https://kiro.dev/docs/cli/chat/context/#configuring-persistent-context-with-agent-resources)
  * [Adding temporary session context](https://kiro.dev/docs/cli/chat/context/#adding-temporary-session-context)
  * [Knowledge base context (for large datasets)](https://kiro.dev/docs/cli/chat/context/#knowledge-base-context-for-large-datasets)
  * [Viewing context usage](https://kiro.dev/docs/cli/chat/context/#viewing-context-usage)
  * [Removing context](https://kiro.dev/docs/cli/chat/context/#removing-context)
  * [Context management actions](https://kiro.dev/docs/cli/chat/context/#context-management-actions)
  * [Best practices](https://kiro.dev/docs/cli/chat/context/#best-practices)
  * [Context file organization](https://kiro.dev/docs/cli/chat/context/#context-file-organization)
  * [Performance considerations](https://kiro.dev/docs/cli/chat/context/#performance-considerations)
  * [Security considerations](https://kiro.dev/docs/cli/chat/context/#security-considerations)
  * [Related documentation](https://kiro.dev/docs/cli/chat/context/#related-documentation)