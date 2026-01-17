# Delegate
**Deprecation notice**
The experimental delegate tool will be replaced by the official [subagents](https://kiro.dev/docs/cli/chat/subagents) tool in a future release. We recommend using subagents for new workflows.
Delegate enables launching and managing asynchronous task processes, allowing you to run Kiro chat sessions with specific agents in parallel to your main conversation. Subagents extend this capability by providing specialized agents that can autonomously handle complex tasks with real-time progress tracking.
## Overview[](https://kiro.dev/docs/cli/experimental/delegate/#overview)
The delegate feature allows you to:
  * Launch background tasks using natural language
  * Run parallel Kiro chat sessions with specific agents
  * Monitor task progress independently
  * Continue your main conversation while tasks run


## Enabling delegate[](https://kiro.dev/docs/cli/experimental/delegate/#enabling-delegate)
bash
```

kiro-cli settings chat.enableDelegate true


```

Or use the experiment command:
bash
```

/experiment
# Select "Delegate" from the list


```

## How it works[](https://kiro.dev/docs/cli/experimental/delegate/#how-it-works)
### Task creation[](https://kiro.dev/docs/cli/experimental/delegate/#task-creation)
Use natural language to ask Kiro to launch a background task:
```

> Can you create a background task to analyze the performance of our API endpoints?


```

Kiro will:
  1. Understand the task requirements
  2. Determine if an agent is needed
  3. Request approval if using an agent
  4. Launch the task in the background
  5. Return control to your main conversation


### Agent approval flow[](https://kiro.dev/docs/cli/experimental/delegate/#agent-approval-flow)
**Tasks with agents:**
  * Require explicit approval
  * Show agent details before execution
  * Display agent configuration and permissions


**Tasks without agents:**
  * Run with a warning about trust-all permissions
  * May have broader access to tools


### Task management[](https://kiro.dev/docs/cli/experimental/delegate/#task-management)
Once delegated, tasks work independently. You can:
  * Check progress at any time
  * Read results when complete
  * Delete tasks when no longer needed


## Usage examples[](https://kiro.dev/docs/cli/experimental/delegate/#usage-examples)
### Example 1: Code analysis[](https://kiro.dev/docs/cli/experimental/delegate/#example-1-code-analysis)
```

> Can you create a background task to analyze the performance of our API endpoints?

I'll create a background task to analyze your API performance.

Agent: performance-analyzer
Tools: read, shell, aws
Resources: api-docs, performance-metrics

Approve this agent? (y/n): y

✓ Task created: api-performance-analysis
  Task ID: task-abc123
  Status: Running

You can continue working while the analysis runs in the background.

> Great! Now help me with the frontend code...

# Continue main conversation

> Check the status of my API analysis task

Let me check on that task...

Task: api-performance-analysis (task-abc123)
Status: Complete
Duration: 2m 34s

Results:
- Analyzed 15 API endpoints
- Found 3 performance bottlenecks
- Generated optimization recommendations

Would you like me to show you the detailed results?


```

### Example 2: Test suite execution[](https://kiro.dev/docs/cli/experimental/delegate/#example-2-test-suite-execution)
```

> Run our test suite in the background while I work on the new feature

I'll start the test suite in a background task.

✓ Task created: test-suite-run
  Task ID: task-def456
  Status: Running

# Continue working on feature

> How's the test suite doing?

Let me check...

Task: test-suite-run (task-def456)
Status: Running (45% complete)
Progress: 127/283 tests passed

Still running. I'll let you know when it's complete.


```

### Example 3: Documentation generation[](https://kiro.dev/docs/cli/experimental/delegate/#example-3-documentation-generation)
```

> Generate API documentation in the background

I'll create a task to generate your API documentation.

✓ Task created: api-docs-generation
  Task ID: task-ghi789
  Status: Running

# Work on other things

> Show me the results from the documentation task

Task: api-docs-generation (task-ghi789)
Status: Complete

Generated documentation for:
- 23 API endpoints
- 15 data models
- 8 authentication methods

Documentation saved to: docs/api/


```

## Task lifecycle[](https://kiro.dev/docs/cli/experimental/delegate/#task-lifecycle)
### 1. Creation[](https://kiro.dev/docs/cli/experimental/delegate/#1-creation)
```

> Create a background task to [description]


```

Kiro analyzes the request and determines:
  * What agent (if any) is needed
  * What tools are required
  * What resources to access


### 2. Approval (if needed)[](https://kiro.dev/docs/cli/experimental/delegate/#2-approval-if-needed)
If an agent is required, you'll see:
```

Agent: task-agent-name
Description: What this agent does
Tools: List of tools it can use
Resources: Files it can access

Approve this agent? (y/n):


```

### 3. Execution[](https://kiro.dev/docs/cli/experimental/delegate/#3-execution)
Task runs in the background while you continue your main conversation.
### 4. Monitoring[](https://kiro.dev/docs/cli/experimental/delegate/#4-monitoring)
Check status anytime:
```

> Check on [task name]
> What's the status of my background task?
> Show me task progress


```

### 5. Completion[](https://kiro.dev/docs/cli/experimental/delegate/#5-completion)
When complete, you can:
```

> Show me the results from [task name]
> What did the background task find?


```

### 6. Cleanup[](https://kiro.dev/docs/cli/experimental/delegate/#6-cleanup)
Delete tasks when done:
```

> Delete the [task name] task
> Clean up completed tasks


```

## Best practices[](https://kiro.dev/docs/cli/experimental/delegate/#best-practices)
### When to use delegate[](https://kiro.dev/docs/cli/experimental/delegate/#when-to-use-delegate)
  * **Long-running operations** : Test suites, builds, analysis
  * **Independent tasks** : Work that doesn't need your input
  * **Parallel work** : Multiple tasks that can run simultaneously
  * **Background monitoring** : Continuous checks or watches


### When not to use[](https://kiro.dev/docs/cli/experimental/delegate/#when-not-to-use)
  * **Interactive tasks** : Work requiring your input
  * **Quick operations** : Tasks that complete in seconds
  * **Dependent work** : Tasks that need results from main conversation
  * **Simple commands** : Direct execution is faster


### Task organization[](https://kiro.dev/docs/cli/experimental/delegate/#task-organization)
  * **Use descriptive names** : Make tasks easy to identify
  * **Monitor progress** : Check on long-running tasks periodically
  * **Clean up completed tasks** : Delete when no longer needed
  * **Limit concurrent tasks** : Too many may slow down system


## Security considerations[](https://kiro.dev/docs/cli/experimental/delegate/#security-considerations)
### Agent approval[](https://kiro.dev/docs/cli/experimental/delegate/#agent-approval)
Always review agent details before approval:
  * **Tools** : What can the agent do?
  * **Resources** : What files can it access?
  * **Permissions** : What operations are allowed?


### Trust-all warning[](https://kiro.dev/docs/cli/experimental/delegate/#trust-all-warning)
Tasks without agents run with elevated permissions:
  * Can access all tools
  * May have broader file access
  * Should be used carefully


### Best practices[](https://kiro.dev/docs/cli/experimental/delegate/#best-practices-1)
  1. **Review agent configurations** : Understand what you're approving
  2. **Use specific agents** : Create agents with minimal required permissions
  3. **Monitor task activity** : Check what tasks are doing
  4. **Delete sensitive results** : Clean up tasks with sensitive data


## Limitations[](https://kiro.dev/docs/cli/experimental/delegate/#limitations)
### Concurrency[](https://kiro.dev/docs/cli/experimental/delegate/#concurrency)
  * Limited number of concurrent tasks
  * System resources shared between tasks
  * May impact performance with many tasks


### Task isolation[](https://kiro.dev/docs/cli/experimental/delegate/#task-isolation)
  * Tasks run independently
  * Cannot directly communicate with main conversation
  * Results must be explicitly retrieved


### Persistence[](https://kiro.dev/docs/cli/experimental/delegate/#persistence)
  * Tasks are session-scoped
  * May not survive session restarts
  * Results should be saved if needed long-term


## Troubleshooting[](https://kiro.dev/docs/cli/experimental/delegate/#troubleshooting)
### Task not starting[](https://kiro.dev/docs/cli/experimental/delegate/#task-not-starting)
  1. **Verify delegate is enabled** :
bash
```

kiro-cli settings chat.enableDelegate


```

  2. **Check for errors** : Look for error messages in chat
  3. **Try simpler task** : Test with a basic task first


### Cannot check task status[](https://kiro.dev/docs/cli/experimental/delegate/#cannot-check-task-status)
  1. **Verify task ID** : Ensure you're using correct task name/ID
  2. **Check if task completed** : Completed tasks may be cleaned up
  3. **List all tasks** : Ask Kiro to show all active tasks


### Agent approval issues[](https://kiro.dev/docs/cli/experimental/delegate/#agent-approval-issues)
  1. **Review agent details carefully** : Ensure you understand permissions
  2. **Check agent exists** : Verify agent is properly configured
  3. **Try without agent** : Some tasks can run without specific agents


## Advanced usage[](https://kiro.dev/docs/cli/experimental/delegate/#advanced-usage)
### Custom agents for tasks[](https://kiro.dev/docs/cli/experimental/delegate/#custom-agents-for-tasks)
Create specialized agents for common background tasks:
json
```

{
  "name": "test-runner",
  "description": "Runs test suites in background",
  "tools": ["shell", "read"],
  "allowedTools": ["shell"],
  "toolsSettings": {
    "shell": {
      "allowedCommands": ["npm test", "pytest", "cargo test"]
    }
  }
}


```

### Task patterns[](https://kiro.dev/docs/cli/experimental/delegate/#task-patterns)
**Analysis Tasks:**
```

> Analyze code quality in the background
> Run security scan as a background task
> Generate performance report in background


```

**Build Tasks:**
```

> Build the project in the background
> Compile and run tests as a background task
> Generate production bundle in background


```

**Monitoring Tasks:**
```

> Monitor log files in the background
> Watch for file changes as a background task
> Track system metrics in background


```

## Related features[](https://kiro.dev/docs/cli/experimental/delegate/#related-features)
  * [Experimental Features](https://kiro.dev/docs/cli/experimental)
  * [Custom Agents](https://kiro.dev/docs/cli/custom-agents)
  * [TODO Lists](https://kiro.dev/docs/cli/experimental/todo-lists)


## Next steps[](https://kiro.dev/docs/cli/experimental/delegate/#next-steps)
  * [Create custom agents for tasks](https://kiro.dev/docs/cli/custom-agents/creating)
  * [Configure agents](https://kiro.dev/docs/cli/custom-agents/configuration-reference)
  * [Enable other experimental features](https://kiro.dev/docs/cli/experimental)


Page updated: December 18, 2025
[Checkpointing](https://kiro.dev/docs/cli/experimental/checkpointing/)
[Hooks](https://kiro.dev/docs/cli/hooks/)
On this page
  * [Overview](https://kiro.dev/docs/cli/experimental/delegate/#overview)
  * [Enabling delegate](https://kiro.dev/docs/cli/experimental/delegate/#enabling-delegate)
  * [How it works](https://kiro.dev/docs/cli/experimental/delegate/#how-it-works)
  * [Task creation](https://kiro.dev/docs/cli/experimental/delegate/#task-creation)
  * [Agent approval flow](https://kiro.dev/docs/cli/experimental/delegate/#agent-approval-flow)
  * [Task management](https://kiro.dev/docs/cli/experimental/delegate/#task-management)
  * [Usage examples](https://kiro.dev/docs/cli/experimental/delegate/#usage-examples)
  * [Example 1: Code analysis](https://kiro.dev/docs/cli/experimental/delegate/#example-1-code-analysis)
  * [Example 2: Test suite execution](https://kiro.dev/docs/cli/experimental/delegate/#example-2-test-suite-execution)
  * [Example 3: Documentation generation](https://kiro.dev/docs/cli/experimental/delegate/#example-3-documentation-generation)
  * [Task lifecycle](https://kiro.dev/docs/cli/experimental/delegate/#task-lifecycle)
  * [1. Creation](https://kiro.dev/docs/cli/experimental/delegate/#1-creation)
  * [2. Approval (if needed)](https://kiro.dev/docs/cli/experimental/delegate/#2-approval-if-needed)
  * [3. Execution](https://kiro.dev/docs/cli/experimental/delegate/#3-execution)
  * [4. Monitoring](https://kiro.dev/docs/cli/experimental/delegate/#4-monitoring)
  * [5. Completion](https://kiro.dev/docs/cli/experimental/delegate/#5-completion)
  * [6. Cleanup](https://kiro.dev/docs/cli/experimental/delegate/#6-cleanup)
  * [Best practices](https://kiro.dev/docs/cli/experimental/delegate/#best-practices)
  * [When to use delegate](https://kiro.dev/docs/cli/experimental/delegate/#when-to-use-delegate)
  * [When not to use](https://kiro.dev/docs/cli/experimental/delegate/#when-not-to-use)
  * [Task organization](https://kiro.dev/docs/cli/experimental/delegate/#task-organization)
  * [Security considerations](https://kiro.dev/docs/cli/experimental/delegate/#security-considerations)
  * [Agent approval](https://kiro.dev/docs/cli/experimental/delegate/#agent-approval)
  * [Trust-all warning](https://kiro.dev/docs/cli/experimental/delegate/#trust-all-warning)
  * [Best practices](https://kiro.dev/docs/cli/experimental/delegate/#best-practices-1)
  * [Limitations](https://kiro.dev/docs/cli/experimental/delegate/#limitations)
  * [Concurrency](https://kiro.dev/docs/cli/experimental/delegate/#concurrency)
  * [Task isolation](https://kiro.dev/docs/cli/experimental/delegate/#task-isolation)
  * [Persistence](https://kiro.dev/docs/cli/experimental/delegate/#persistence)
  * [Troubleshooting](https://kiro.dev/docs/cli/experimental/delegate/#troubleshooting)
  * [Task not starting](https://kiro.dev/docs/cli/experimental/delegate/#task-not-starting)
  * [Cannot check task status](https://kiro.dev/docs/cli/experimental/delegate/#cannot-check-task-status)
  * [Agent approval issues](https://kiro.dev/docs/cli/experimental/delegate/#agent-approval-issues)
  * [Advanced usage](https://kiro.dev/docs/cli/experimental/delegate/#advanced-usage)
  * [Custom agents for tasks](https://kiro.dev/docs/cli/experimental/delegate/#custom-agents-for-tasks)
  * [Task patterns](https://kiro.dev/docs/cli/experimental/delegate/#task-patterns)
  * [Related features](https://kiro.dev/docs/cli/experimental/delegate/#related-features)
  * [Next steps](https://kiro.dev/docs/cli/experimental/delegate/#next-steps)