# Tangent mode
Tangent mode creates conversation checkpoints, allowing you to explore side topics without disrupting your main conversation flow. Enter tangent mode, ask questions or explore ideas, then return to your original conversation exactly where you left off.
## Enabling tangent mode[](https://kiro.dev/docs/cli/experimental/tangent-mode/#enabling-tangent-mode)
Tangent mode is experimental and must be enabled:
**Via Experiment Command:**
bash
```

/experiment
# Select tangent mode from the list


```

**Via Settings:**
bash
```

kiro-cli settings chat.enableTangentMode true


```

## Basic usage[](https://kiro.dev/docs/cli/experimental/tangent-mode/#basic-usage)
### Enter tangent mode[](https://kiro.dev/docs/cli/experimental/tangent-mode/#enter-tangent-mode)
Use `/tangent` or **Ctrl+T** :
```

> /tangent
Created a conversation checkpoint (↯). Use ctrl + t or /tangent to restore the conversation later.


```

### In tangent mode[](https://kiro.dev/docs/cli/experimental/tangent-mode/#in-tangent-mode)
You'll see a yellow `↯` symbol in your prompt:
```

↯ > What is the difference between async and sync functions?


```

### Exit tangent mode[](https://kiro.dev/docs/cli/experimental/tangent-mode/#exit-tangent-mode)
Use `/tangent` or **Ctrl+T** again:
```

↯ > /tangent
Restored conversation from checkpoint (↯). - Returned to main conversation.


```

### Exit with tail[](https://kiro.dev/docs/cli/experimental/tangent-mode/#exit-with-tail)
Use `/tangent tail` to preserve the last conversation entry (question + answer):
```

↯ > /tangent tail
Restored conversation from checkpoint (↯) with last conversation entry preserved.


```

## Usage examples[](https://kiro.dev/docs/cli/experimental/tangent-mode/#usage-examples)
### Example 1: Exploring alternatives[](https://kiro.dev/docs/cli/experimental/tangent-mode/#example-1-exploring-alternatives)
```

> I need to process a large CSV file in Python. What's the best approach?

I recommend using pandas for CSV processing...

> /tangent
Created a conversation checkpoint (↯).

↯ > What about using the csv module instead of pandas?

The csv module is lighter weight...

↯ > /tangent
Restored conversation from checkpoint (↯).

> Thanks! I'll go with pandas. Can you show me error handling?


```

### Example 2: Getting Kiro CLI help[](https://kiro.dev/docs/cli/experimental/tangent-mode/#example-2-getting-kiro-cli-help)
```

> Help me write a deployment script

I can help you create a deployment script...

> /tangent
Created a conversation checkpoint (↯).

↯ > What Kiro CLI commands are available for file operations?

Kiro CLI provides read, write, shell...

↯ > /tangent
Restored conversation from checkpoint (↯).

> It's a Node.js application for AWS


```

### Example 3: Clarifying requirements[](https://kiro.dev/docs/cli/experimental/tangent-mode/#example-3-clarifying-requirements)
```

> I need to optimize this SQL query

Could you share the query you'd like to optimize?

> /tangent
Created a conversation checkpoint (↯).

↯ > What information do you need to help optimize a query?

To optimize SQL queries effectively, I need:
1. The current query
2. Table schemas and indexes...

↯ > /tangent
Restored conversation from checkpoint (↯).

> Here's my query: SELECT * FROM orders...


```

### Example 4: Keeping useful information[](https://kiro.dev/docs/cli/experimental/tangent-mode/#example-4-keeping-useful-information)
```

> Help me debug this Python error

I can help you debug that. Could you share the error message?

> /tangent
Created a conversation checkpoint (↯).

↯ > What are the most common Python debugging techniques?

Here are the most effective Python debugging techniques:
1. Use print statements strategically
2. Leverage the Python debugger (pdb)...

↯ > /tangent tail
Restored conversation from checkpoint (↯) with last conversation entry preserved.

> Here's my error: TypeError: unsupported operand type(s)...

# The preserved entry about debugging techniques is now part of main conversation


```

## Configuration[](https://kiro.dev/docs/cli/experimental/tangent-mode/#configuration)
### Keyboard shortcut[](https://kiro.dev/docs/cli/experimental/tangent-mode/#keyboard-shortcut)
Change the shortcut key (default: t):
bash
```

kiro-cli settings chat.tangentModeKey y


```

### Auto-tangent for introspect[](https://kiro.dev/docs/cli/experimental/tangent-mode/#auto-tangent-for-introspect)
Automatically enter tangent mode for Kiro CLI help questions:
bash
```

kiro-cli settings introspect.tangentMode true


```

## Visual indicators[](https://kiro.dev/docs/cli/experimental/tangent-mode/#visual-indicators)
  * **Normal mode** : `> ` (magenta)
  * **Tangent mode** : `↯ > ` (yellow ↯ + magenta)
  * **With agent** : `[dev] ↯ > ` (cyan + yellow ↯ + magenta)


## When to use tangent mode[](https://kiro.dev/docs/cli/experimental/tangent-mode/#when-to-use-tangent-mode)
### Good use cases[](https://kiro.dev/docs/cli/experimental/tangent-mode/#good-use-cases)
  * **Asking clarifying questions** about the current topic
  * **Exploring alternative approaches** before deciding
  * **Getting help** with Kiro CLI commands or features
  * **Testing understanding** of concepts
  * **Quick side questions** that don't need to be in main context


### When not to use[](https://kiro.dev/docs/cli/experimental/tangent-mode/#when-not-to-use)
  * **Completely unrelated topics** - Start a new conversation instead
  * **Long, complex discussions** - Use regular conversation flow
  * **When you want the side discussion in main context** - Don't use tangent mode


## Tips[](https://kiro.dev/docs/cli/experimental/tangent-mode/#tips)
  1. **Keep tangents focused** : Brief explorations, not extended discussions
  2. **Return promptly** : Don't forget you're in tangent mode
  3. **Use for clarification** : Perfect for "wait, what does X mean?" questions
  4. **Experiment safely** : Test ideas without affecting main conversation
  5. **Use`/tangent tail`** : When both the tangent question and answer are useful for main conversation


## How it works[](https://kiro.dev/docs/cli/experimental/tangent-mode/#how-it-works)
### Checkpoint creation[](https://kiro.dev/docs/cli/experimental/tangent-mode/#checkpoint-creation)
When you enter tangent mode:
  1. Current conversation state is saved as a checkpoint
  2. You can continue the conversation in tangent mode
  3. All tangent conversation is separate from main thread


### Restoration[](https://kiro.dev/docs/cli/experimental/tangent-mode/#restoration)
When you exit tangent mode:
  1. Conversation returns to the checkpoint state
  2. Tangent conversation is discarded (unless using `tail`)
  3. Main conversation continues as if tangent never happened


### Tail mode[](https://kiro.dev/docs/cli/experimental/tangent-mode/#tail-mode)
Using `/tangent tail`:
  1. Returns to checkpoint like normal exit
  2. Preserves the last Q&A pair from tangent
  3. Adds that Q&A to main conversation context
  4. Useful when tangent provided valuable information


## Limitations[](https://kiro.dev/docs/cli/experimental/tangent-mode/#limitations)
  * **Tangent conversations are discarded** when you exit (unless using tail)
  * **Only one level of tangent** supported (no nested tangents)
  * **Experimental feature** that may change or be removed
  * **Must be explicitly enabled** before use


## Troubleshooting[](https://kiro.dev/docs/cli/experimental/tangent-mode/#troubleshooting)
### Tangent mode not working[](https://kiro.dev/docs/cli/experimental/tangent-mode/#tangent-mode-not-working)
Enable via experiment:
bash
```

/experiment
# Select tangent mode from the list


```

Or enable via settings:
bash
```

kiro-cli settings chat.enableTangentMode true


```

### Keyboard shortcut not working[](https://kiro.dev/docs/cli/experimental/tangent-mode/#keyboard-shortcut-not-working)
Check or reset the shortcut key:
bash
```

kiro-cli settings chat.tangentModeKey t


```

Ensure you're using Ctrl+T (not just T).
### Lost in tangent mode[](https://kiro.dev/docs/cli/experimental/tangent-mode/#lost-in-tangent-mode)
Look for the `↯` symbol in your prompt. Use `/tangent` to exit and return to main conversation.
### Accidentally discarded important information[](https://kiro.dev/docs/cli/experimental/tangent-mode/#accidentally-discarded-important-information)
If you exit tangent mode without using `tail` and lose important information:
  1. Unfortunately, tangent conversations are not recoverable
  2. You'll need to ask the question again in the main conversation
  3. Consider using `/tangent tail` in the future to preserve important Q&A pairs


## Related features[](https://kiro.dev/docs/cli/experimental/tangent-mode/#related-features)
  * **Introspect** : Kiro CLI help (auto-enters tangent if configured)
  * **Experiments** : Manage experimental features with `/experiment`
  * **Checkpointing** : Similar concept but for file changes


## Best practices[](https://kiro.dev/docs/cli/experimental/tangent-mode/#best-practices)
### Workflow integration[](https://kiro.dev/docs/cli/experimental/tangent-mode/#workflow-integration)
  1. **Start main task** : Begin your primary conversation
  2. **Hit tangent** : When a side question arises, use `/tangent`
  3. **Explore freely** : Ask clarifying questions without worry
  4. **Decide on tail** : If the tangent was useful, use `/tangent tail`
  5. **Continue main** : Return to your primary task


### Example workflow[](https://kiro.dev/docs/cli/experimental/tangent-mode/#example-workflow)
```

> Help me refactor this React component

# Main conversation starts...

> /tangent
↯ > What's the difference between useMemo and useCallback?

# Get clarification...

↯ > /tangent tail  # This was useful, keep it

> Now I understand. Let's use useMemo for the expensive calculation...


```

## Next steps[](https://kiro.dev/docs/cli/experimental/tangent-mode/#next-steps)
  * [Experimental Features Overview](https://kiro.dev/docs/cli/experimental)
  * [Checkpointing](https://kiro.dev/docs/cli/experimental/checkpointing)
  * [Settings Configuration](https://kiro.dev/docs/cli/settings)


Page updated: November 18, 2025
[Knowledge management](https://kiro.dev/docs/cli/experimental/knowledge-management/)
[TODO lists](https://kiro.dev/docs/cli/experimental/todo-lists/)
On this page
  * [Enabling tangent mode](https://kiro.dev/docs/cli/experimental/tangent-mode/#enabling-tangent-mode)
  * [Basic usage](https://kiro.dev/docs/cli/experimental/tangent-mode/#basic-usage)
  * [Enter tangent mode](https://kiro.dev/docs/cli/experimental/tangent-mode/#enter-tangent-mode)
  * [In tangent mode](https://kiro.dev/docs/cli/experimental/tangent-mode/#in-tangent-mode)
  * [Exit tangent mode](https://kiro.dev/docs/cli/experimental/tangent-mode/#exit-tangent-mode)
  * [Exit with tail](https://kiro.dev/docs/cli/experimental/tangent-mode/#exit-with-tail)
  * [Usage examples](https://kiro.dev/docs/cli/experimental/tangent-mode/#usage-examples)
  * [Example 1: Exploring alternatives](https://kiro.dev/docs/cli/experimental/tangent-mode/#example-1-exploring-alternatives)
  * [Example 2: Getting Kiro CLI help](https://kiro.dev/docs/cli/experimental/tangent-mode/#example-2-getting-kiro-cli-help)
  * [Example 3: Clarifying requirements](https://kiro.dev/docs/cli/experimental/tangent-mode/#example-3-clarifying-requirements)
  * [Example 4: Keeping useful information](https://kiro.dev/docs/cli/experimental/tangent-mode/#example-4-keeping-useful-information)
  * [Configuration](https://kiro.dev/docs/cli/experimental/tangent-mode/#configuration)
  * [Keyboard shortcut](https://kiro.dev/docs/cli/experimental/tangent-mode/#keyboard-shortcut)
  * [Auto-tangent for introspect](https://kiro.dev/docs/cli/experimental/tangent-mode/#auto-tangent-for-introspect)
  * [Visual indicators](https://kiro.dev/docs/cli/experimental/tangent-mode/#visual-indicators)
  * [When to use tangent mode](https://kiro.dev/docs/cli/experimental/tangent-mode/#when-to-use-tangent-mode)
  * [Good use cases](https://kiro.dev/docs/cli/experimental/tangent-mode/#good-use-cases)
  * [When not to use](https://kiro.dev/docs/cli/experimental/tangent-mode/#when-not-to-use)
  * [Tips](https://kiro.dev/docs/cli/experimental/tangent-mode/#tips)
  * [How it works](https://kiro.dev/docs/cli/experimental/tangent-mode/#how-it-works)
  * [Checkpoint creation](https://kiro.dev/docs/cli/experimental/tangent-mode/#checkpoint-creation)
  * [Restoration](https://kiro.dev/docs/cli/experimental/tangent-mode/#restoration)
  * [Tail mode](https://kiro.dev/docs/cli/experimental/tangent-mode/#tail-mode)
  * [Limitations](https://kiro.dev/docs/cli/experimental/tangent-mode/#limitations)
  * [Troubleshooting](https://kiro.dev/docs/cli/experimental/tangent-mode/#troubleshooting)
  * [Tangent mode not working](https://kiro.dev/docs/cli/experimental/tangent-mode/#tangent-mode-not-working)
  * [Keyboard shortcut not working](https://kiro.dev/docs/cli/experimental/tangent-mode/#keyboard-shortcut-not-working)
  * [Lost in tangent mode](https://kiro.dev/docs/cli/experimental/tangent-mode/#lost-in-tangent-mode)
  * [Accidentally discarded important information](https://kiro.dev/docs/cli/experimental/tangent-mode/#accidentally-discarded-important-information)
  * [Related features](https://kiro.dev/docs/cli/experimental/tangent-mode/#related-features)
  * [Best practices](https://kiro.dev/docs/cli/experimental/tangent-mode/#best-practices)
  * [Workflow integration](https://kiro.dev/docs/cli/experimental/tangent-mode/#workflow-integration)
  * [Example workflow](https://kiro.dev/docs/cli/experimental/tangent-mode/#example-workflow)
  * [Next steps](https://kiro.dev/docs/cli/experimental/tangent-mode/#next-steps)