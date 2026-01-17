# TODO lists
The TODO list feature enables Kiro to automatically create and modify task lists, while providing you with commands to view and manage existing TODO lists.
## Getting started[](https://kiro.dev/docs/cli/experimental/todo-lists/#getting-started)
TODO lists are automatically created when Kiro breaks down complex tasks. You can then manage these lists using the `/todo` command.
### Enable TODO lists[](https://kiro.dev/docs/cli/experimental/todo-lists/#enable-todo-lists)
bash
```

kiro-cli settings chat.enableTodoList true


```

### Basic usage[](https://kiro.dev/docs/cli/experimental/todo-lists/#basic-usage)
bash
```

/todo view      # View existing TODO lists
/todo resume    # Resume a TODO list


```

## How it works[](https://kiro.dev/docs/cli/experimental/todo-lists/#how-it-works)
### Automatic creation[](https://kiro.dev/docs/cli/experimental/todo-lists/#automatic-creation)
Kiro automatically creates TODO lists when:
  * You ask for help with multi-step tasks
  * A complex problem needs to be broken down
  * You explicitly request a TODO list


**Example:**
```

> Make a todo list with 3 read-only tasks.

I'll create a todo list with 3 read-only tasks for you.

🛠️  Using tool: todo_list (trusted)
 ⋮ 
 ● TODO:
[ ] Review project documentation
[ ] Check system status
[ ] Read latest updates
 ⋮ 
 ● Completed in 0.4s


```

### Task management[](https://kiro.dev/docs/cli/experimental/todo-lists/#task-management)
Kiro can:
  * Create TODO lists
  * Mark tasks as complete
  * Add/remove tasks
  * Load TODO lists by ID
  * Search for existing TODO lists


You can:
  * View TODO lists
  * Resume TODO lists
  * Delete TODO lists


## Commands[](https://kiro.dev/docs/cli/experimental/todo-lists/#commands)
### /todo view[](https://kiro.dev/docs/cli/experimental/todo-lists/#todo-view)
Display and select a TODO list to view its contents, showing task descriptions and completion status.
bash
```

/todo view


```

**Interactive selection shows:**
  * ✓ Completed lists (green checkmark)
  * ✗ In-progress lists with completion count (red X with progress)


**Example:**
```

> /todo view

? Select a to-do list to view: ›
❯ ✗ Unfinished todo list (0/3)
  ✔ Completed todo list (3/3)


```

### /todo resume[](https://kiro.dev/docs/cli/experimental/todo-lists/#todo-resume)
Show an interactive menu of available TODO lists with their current progress status. Selecting a list loads it back into your chat session, allowing Kiro to continue where it left off.
bash
```

/todo resume


```

**Example:**
```

> /todo resume

⟳ Resuming: Read-only tasks for information gathering

🛠️  Using tool: todo (trusted)
 ⋮ 
 ● TODO:
[x] Review project documentation
[ ] Check system status
[ ] Read latest updates
 ⋮ 
 ● Completed in 0.1s


```

### /todo clear-finished[](https://kiro.dev/docs/cli/experimental/todo-lists/#todo-clear-finished)
Remove all completed TODO lists from storage. This helps clean up your workspace by removing lists where all tasks have been completed.
bash
```

/todo clear-finished


```

### /todo delete[](https://kiro.dev/docs/cli/experimental/todo-lists/#todo-delete)
Delete specific TODO lists or all lists at once.
bash
```

/todo delete           # Interactive selection to delete one list
/todo delete --all     # Delete all TODO lists


```

**Options:**
  * `--all` - Delete all TODO lists without interactive selection


## Storage[](https://kiro.dev/docs/cli/experimental/todo-lists/#storage)
TODO lists are persisted across sessions
Each list is saved as a JSON file with:
  * Unique timestamp-based ID
  * Task descriptions and completion status
  * Context updates from completed tasks
  * Modified file paths
  * Overall list description


### Directory structure[](https://kiro.dev/docs/cli/experimental/todo-lists/#directory-structure)
```

my-project/
├── .kiro/
│   └── cli-todo-lists/
│       ├── 1234567890-task-list.json
│       └── 1234567891-another-list.json
└── src/
    └── main.py


```

## Interactive selection[](https://kiro.dev/docs/cli/experimental/todo-lists/#interactive-selection)
All commands use interactive selection allowing you to:
  * Navigate with arrow keys
  * Press Enter to select
  * Press Esc to cancel


## Use cases[](https://kiro.dev/docs/cli/experimental/todo-lists/#use-cases)
### Breaking down complex tasks[](https://kiro.dev/docs/cli/experimental/todo-lists/#breaking-down-complex-tasks)
```

> I need to migrate our database from MySQL to PostgreSQL

Let me create a TODO list for this migration:

🛠️  Using tool: todo
 ● TODO: Database Migration
[ ] Backup current MySQL database
[ ] Set up PostgreSQL instance
[ ] Create schema migration scripts
[ ] Test migration on staging
[ ] Perform production migration
[ ] Verify data integrity


```

### Tracking multi-step implementations[](https://kiro.dev/docs/cli/experimental/todo-lists/#tracking-multi-step-implementations)
```

> Help me implement user authentication

I'll break this down into manageable steps:

🛠️  Using tool: todo
 ● TODO: User Authentication Implementation
[ ] Set up authentication library
[ ] Create user model and database schema
[ ] Implement registration endpoint
[ ] Implement login endpoint
[ ] Add password hashing
[ ] Create JWT token generation
[ ] Add authentication middleware
[ ] Write tests for auth flow


```

### Resuming previous work[](https://kiro.dev/docs/cli/experimental/todo-lists/#resuming-previous-work)
```

> /todo resume

? Select a to-do list to resume: ›
❯ ✗ User Authentication Implementation (3/8)
  ✗ Database Migration (1/6)
  ✔ Code Refactoring (5/5)

# Select "User Authentication Implementation"

⟳ Resuming: User Authentication Implementation

Let's continue with the authentication implementation. 
We've completed the first 3 tasks. Next up is implementing the login endpoint...


```

## Best practices[](https://kiro.dev/docs/cli/experimental/todo-lists/#best-practices)
### Managing lists[](https://kiro.dev/docs/cli/experimental/todo-lists/#managing-lists)
  * **Use`clear-finished` regularly** to remove completed lists
  * **Resume lists** to continue complex multi-step tasks
  * **Check`view`** to see progress without resuming


### Workflow integration[](https://kiro.dev/docs/cli/experimental/todo-lists/#workflow-integration)
  * **Let Kiro create TODO lists** for complex tasks automatically
  * **Use`resume`** to pick up where you left off in previous sessions
  * **Check`view`** to see what tasks remain before resuming work


### Organization[](https://kiro.dev/docs/cli/experimental/todo-lists/#organization)
  * **Work in project directories** where TODO lists are relevant
  * **Complete tasks in order** for better context
  * **Delete old lists** when no longer needed


## Limitations[](https://kiro.dev/docs/cli/experimental/todo-lists/#limitations)
### Functionality[](https://kiro.dev/docs/cli/experimental/todo-lists/#functionality)
  * Cannot manually edit TODO list files
  * Cannot merge or split TODO lists
  * Cannot reorder tasks after creation


## Troubleshooting[](https://kiro.dev/docs/cli/experimental/todo-lists/#troubleshooting)
### Tasks not updating[](https://kiro.dev/docs/cli/experimental/todo-lists/#tasks-not-updating)
If task completion isn't being tracked:
  1. **Ensure TODO list is active** : Resume the list first
  2. **Let Kiro mark tasks** : Don't manually edit JSON files
  3. **Check for errors** : Look for error messages in chat


## Tool vs command[](https://kiro.dev/docs/cli/experimental/todo-lists/#tool-vs-command)
###  `todo` tool[](https://kiro.dev/docs/cli/experimental/todo-lists/#todo-tool)
The `todo` tool is for Kiro to call. Kiro can:
  * Create TODO lists
  * Mark tasks as complete
  * Add/remove tasks
  * Load TODO lists with given ID
  * Search for existing TODO lists


###  `/todo` command[](https://kiro.dev/docs/cli/experimental/todo-lists/#todo-command)
The `/todo` command is for you to manage existing TODO lists. You can:
  * View TODO lists
  * Resume TODO lists
  * Delete TODO lists
  * Clear finished lists


## Example workflow[](https://kiro.dev/docs/cli/experimental/todo-lists/#example-workflow)
### 1. Start complex task[](https://kiro.dev/docs/cli/experimental/todo-lists/#1-start-complex-task)
```

> I need to set up CI/CD for our project


```

### 2. Kiro creates TODO list[](https://kiro.dev/docs/cli/experimental/todo-lists/#2-kiro-creates-todo-list)
```

🛠️  Using tool: todo_list
 ● TODO: CI/CD Setup
[ ] Choose CI/CD platform
[ ] Create pipeline configuration
[ ] Set up build stage
[ ] Add test stage
[ ] Configure deployment stage
[ ] Set up environment variables
[ ] Test pipeline


```

### 3. Work through tasks[](https://kiro.dev/docs/cli/experimental/todo-lists/#3-work-through-tasks)
Kiro works through tasks, marking them complete as you go.
### 4. Resume later[](https://kiro.dev/docs/cli/experimental/todo-lists/#4-resume-later)
```

> /todo resume

? Select a to-do list to resume: ›
❯ ✗ CI/CD Setup (4/7)

# Continue where you left off


```

### 5. Clean up when done[](https://kiro.dev/docs/cli/experimental/todo-lists/#5-clean-up-when-done)
```

> /todo clear-finished


```

## Next steps[](https://kiro.dev/docs/cli/experimental/todo-lists/#next-steps)
  * [Experimental Features Overview](https://kiro.dev/docs/cli/experimental)
  * [Checkpointing](https://kiro.dev/docs/cli/experimental/checkpointing)
  * [Custom Agents](https://kiro.dev/docs/cli/custom-agents)


Page updated: November 18, 2025
[Tangent mode](https://kiro.dev/docs/cli/experimental/tangent-mode/)
[Thinking tool](https://kiro.dev/docs/cli/experimental/thinking/)
On this page
  * [Getting started](https://kiro.dev/docs/cli/experimental/todo-lists/#getting-started)
  * [Enable TODO lists](https://kiro.dev/docs/cli/experimental/todo-lists/#enable-todo-lists)
  * [Basic usage](https://kiro.dev/docs/cli/experimental/todo-lists/#basic-usage)
  * [How it works](https://kiro.dev/docs/cli/experimental/todo-lists/#how-it-works)
  * [Automatic creation](https://kiro.dev/docs/cli/experimental/todo-lists/#automatic-creation)
  * [Task management](https://kiro.dev/docs/cli/experimental/todo-lists/#task-management)
  * [Commands](https://kiro.dev/docs/cli/experimental/todo-lists/#commands)
  * [/todo view](https://kiro.dev/docs/cli/experimental/todo-lists/#todo-view)
  * [/todo resume](https://kiro.dev/docs/cli/experimental/todo-lists/#todo-resume)
  * [/todo clear-finished](https://kiro.dev/docs/cli/experimental/todo-lists/#todo-clear-finished)
  * [/todo delete](https://kiro.dev/docs/cli/experimental/todo-lists/#todo-delete)
  * [Storage](https://kiro.dev/docs/cli/experimental/todo-lists/#storage)
  * [Directory structure](https://kiro.dev/docs/cli/experimental/todo-lists/#directory-structure)
  * [Interactive selection](https://kiro.dev/docs/cli/experimental/todo-lists/#interactive-selection)
  * [Use cases](https://kiro.dev/docs/cli/experimental/todo-lists/#use-cases)
  * [Breaking down complex tasks](https://kiro.dev/docs/cli/experimental/todo-lists/#breaking-down-complex-tasks)
  * [Tracking multi-step implementations](https://kiro.dev/docs/cli/experimental/todo-lists/#tracking-multi-step-implementations)
  * [Resuming previous work](https://kiro.dev/docs/cli/experimental/todo-lists/#resuming-previous-work)
  * [Best practices](https://kiro.dev/docs/cli/experimental/todo-lists/#best-practices)
  * [Managing lists](https://kiro.dev/docs/cli/experimental/todo-lists/#managing-lists)
  * [Workflow integration](https://kiro.dev/docs/cli/experimental/todo-lists/#workflow-integration)
  * [Organization](https://kiro.dev/docs/cli/experimental/todo-lists/#organization)
  * [Limitations](https://kiro.dev/docs/cli/experimental/todo-lists/#limitations)
  * [Functionality](https://kiro.dev/docs/cli/experimental/todo-lists/#functionality)
  * [Troubleshooting](https://kiro.dev/docs/cli/experimental/todo-lists/#troubleshooting)
  * [Tasks not updating](https://kiro.dev/docs/cli/experimental/todo-lists/#tasks-not-updating)
  * [Tool vs command](https://kiro.dev/docs/cli/experimental/todo-lists/#tool-vs-command)
  * [`todo` tool](https://kiro.dev/docs/cli/experimental/todo-lists/#todo-tool)
  * [`/todo` command](https://kiro.dev/docs/cli/experimental/todo-lists/#todo-command)
  * [Example workflow](https://kiro.dev/docs/cli/experimental/todo-lists/#example-workflow)
  * [1. Start complex task](https://kiro.dev/docs/cli/experimental/todo-lists/#1-start-complex-task)
  * [2. Kiro creates TODO list](https://kiro.dev/docs/cli/experimental/todo-lists/#2-kiro-creates-todo-list)
  * [3. Work through tasks](https://kiro.dev/docs/cli/experimental/todo-lists/#3-work-through-tasks)
  * [4. Resume later](https://kiro.dev/docs/cli/experimental/todo-lists/#4-resume-later)
  * [5. Clean up when done](https://kiro.dev/docs/cli/experimental/todo-lists/#5-clean-up-when-done)
  * [Next steps](https://kiro.dev/docs/cli/experimental/todo-lists/#next-steps)