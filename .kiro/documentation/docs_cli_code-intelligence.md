# Code Intelligence
## Overview[](https://kiro.dev/docs/cli/code-intelligence/#overview)
Code Intelligence integrates Language Server Protocol (LSP) into Kiro CLI to enable semantic understanding of your codebase for the Kiro agent, similar to how extensions provide capabilities in your IDE. It comes pre-configured with 7 languages (TypeScript, Rust, Python, Go, Java, Ruby, C/C++) but can be expanded to any language by adding custom LSP configurations to `.kiro/settings/lsp.json` in your project root. After running `/code init`, you can search symbols, find references, navigate definitions, rename across files, and get diagnostics through natural language queries.
### How it works[](https://kiro.dev/docs/cli/code-intelligence/#how-it-works)
Kiro CLI spawns LSP server processes in the background that communicate via JSON-RPC over stdio. When you initialize a workspace, it detects languages from project markers (like `package.json`, `Cargo.toml`) and file extensions, then starts the appropriate language servers. These servers continuously analyze your code and maintain an index of symbols, types, and references. When you make queries, Kiro translates your natural language into LSP protocol requests, sends them to the relevant server, and formats the responses back into readable output.
Here's how you can enable Kiro CLI to use LSP servers:
  1. Install language servers
  2. Enable the LSP integration
  3. Ask code related questions to use language servers


## Installing language servers[](https://kiro.dev/docs/cli/code-intelligence/#installing-language-servers)
**Supported Languages**
Language | Extensions | Server | Install Command  
---|---|---|---  
TypeScript/JavaScript | .ts, .js, .tsx, .jsx | typescript-language-server | `npm install -g typescript-language-server typescript`  
Rust | .rs | rust-analyzer | `rustup component add rust-analyzer`  
Python | .py | jedi-language-server | `npm install -g pyright or pip install pyright`  
Go | .go | gopls | `go install golang.org/x/tools/gopls@latest`  
Java | .java | jdtls | `brew install jdtls (macOS)`  
Ruby | .rb | solargraph | `gem install solargraph`  
C/C++ | .c, .cpp, .h, .hpp | clangd | `brew install llvm (macOS) or apt install clangd (Linux)`  
## Initialize Code Intelligence[](https://kiro.dev/docs/cli/code-intelligence/#initialize-code-intelligence)
**Workspace-scoped configuration**
Code intelligence is configured per workspace, not globally. Each project maintains its own LSP settings independently.
Run this slash command in your project root:
```

/code init


```

This creates `.kiro/settings/lsp.json` configuration and starts language servers.
What you'll see:
```

✓ Workspace initialization started

Workspace: /path/to/your/project
Detected Languages: ["python", "rust", "typescript"]
Project Markers: ["Cargo.toml", "package.json"]

Available LSPs:
○ clangd (cpp) - available
○ gopls (go) - not installed
◐ jdtls (java) - initializing...
✓ jedi-language-server (python) - initialized (687ms)
✓ rust-analyzer (rust) - initialized (488ms)
○ solargraph (ruby) - not installed
✓ typescript-language-server (typescript) - initialized (214ms)


```

**Status indicators:**
  * ✓ - Initialized and ready
  * ◐ - Currently initializing
  * ○ available - Installed but not needed for detected languages
  * ○ not installed - Not installed on your system


**Restart LSP servers:** If language servers shut down or become unresponsive, use `/code init -f`.
**Auto-initialization:** After the first `/code init`, Kiro CLI automatically initializes code intelligence on startup when `.kiro/settings/lsp.json` exists in the workspace.
**Disabling code intelligence:** Delete `.kiro/settings/lsp.json` from your project to disable. You must restart your session for this change to take effect. Re-enable anytime with `/code init`.
## Using Language Servers[](https://kiro.dev/docs/cli/code-intelligence/#using-language-servers)
Language servers provide semantic code intelligence through natural language queries. You can search symbols, navigate definitions, find references, rename across files, get diagnostics, view method documentation, and discover available APIs on classes and objects.
### Example 1: Find a Symbol[](https://kiro.dev/docs/cli/code-intelligence/#example-1-find-a-symbol)
```

> Find the UserRepository class

Searching for symbols matching: "UserRepository"

  1. Class UserRepository at src/repositories/user.repository.ts:15:1


```

### Example 2: Find All References[](https://kiro.dev/docs/cli/code-intelligence/#example-2-find-all-references)
```

> Find references of Person class

Finding all references at: auth.ts:42:10

  1. src/auth.ts:42:10 - export function authenticate(...)
  2. src/handlers/login.ts:15:5 - authenticate(credentials)
  3. src/handlers/api.ts:89:12 - await authenticate(token)
  (3 more items found)


```

### Example 3: Go to Definition[](https://kiro.dev/docs/cli/code-intelligence/#example-3-go-to-definition)
```

> Find the definition of UserService

src/services/user.service.ts:42:1: export class UserService { ...


```

### Example 4: Get File Symbols[](https://kiro.dev/docs/cli/code-intelligence/#example-4-get-file-symbols)
```

> What symbols are in auth.service.ts?

Getting symbols from: auth.service.ts

  1. Class AuthService at auth.service.ts:12:1
  2. Function login at auth.service.ts:25:3
  3. Function logout at auth.service.ts:45:3
  4. Function validateToken at auth.service.ts:62:3


```

### Example 5: Rename with Dry Run[](https://kiro.dev/docs/cli/code-intelligence/#example-5-rename-with-dry-run)
```

> Dry run: rename the method "FetchUser" to "fetchUserData"

Dry run: Would rename 12 occurrences in 5 files


```

### Example 6: Get Diagnostics[](https://kiro.dev/docs/cli/code-intelligence/#example-6-get-diagnostics)
```

> Get diagnostics for main.ts

  1. Error line 15:10: Cannot find name 'undefined_var'
  2. Warning line 42:5: 'result' is declared but never used


```

### Example 7: Get Hover Information[](https://kiro.dev/docs/cli/code-intelligence/#example-7-get-hover-information)
```

> What's the documentation for the authenticate method in AuthService?

Type: (credentials: Credentials) => Promise<AuthResult>

Documentation: Authenticates a user with the provided credentials.
Returns an AuthResult containing the user token and profile.

@param credentials - User login credentials
@throws AuthenticationError if credentials are invalid


```

### Example 8: Get Code Completions[](https://kiro.dev/docs/cli/code-intelligence/#example-8-get-code-completions)
```

> What methods are available on the s3Client instance?

Available completions:

  1. putObject - Function: (params: PutObjectRequest) => Promise<PutObjectOutput>
  2. getObject - Function: (params: GetObjectRequest) => Promise<GetObjectOutput>
  3. deleteObject - Function: (params: DeleteObjectRequest) => Promise<DeleteObjectOutput>
  4. listObjects - Function: (params: ListObjectsRequest) => Promise<ListObjectsOutput>
  5. headObject - Function: (params: HeadObjectRequest) => Promise<HeadObjectOutput>


```

## Custom Language Servers[](https://kiro.dev/docs/cli/code-intelligence/#custom-language-servers)
Add custom language servers by editing `.kiro/settings/lsp.json` in your project:
json
```

{ 
  "languages": { 
    "mylang": { 
      "name": "my-language-server", 
      "command": "my-lsp-binary", 
      "args": ["--stdio"], 
      "file_extensions": ["mylang", "ml"], 
      "project_patterns": ["mylang.config"], 
      "exclude_patterns": ["**/build/**"], 
      "multi_workspace": false, 
      "initialization_options": { "custom": "options" } 
    } 
  } 
}


```

**Fields:**
  * **name** : Display name for the language server
  * **command** : Binary/command to execute
  * **args** : Command line arguments (usually ["--stdio"])
  * **file_extensions** : File extensions this server handles
  * **project_patterns** : Files that indicate a project root (e.g., package.json)
  * **exclude_patterns** : Glob patterns to exclude from analysis
  * **multi_workspace** : Set to true if the LSP supports multiple workspace folders (default: false)
  * **initialization_options** : LSP-specific configuration passed during initialization
  * **request_timeout_secs** : Timeout in seconds for LSP requests. Default is 60.


After editing, restart KIRO CLI to load the new configuration.
## Troubleshooting[](https://kiro.dev/docs/cli/code-intelligence/#troubleshooting)
Issue | Cause(s) | Solution  
---|---|---  
Workspace is still initializing | LSP servers are starting up | Wait and try again. If servers crashed, use `/code init -f` to restart.  
LSP initialization failed |  | Check logs for details: `/code logs -l`  
No symbols found | Language server is still indexing or File has syntax errors or Symbol name doesn't match | Check file for errors, try broader search terms.  
No definition found | Position doesn't point to a symbol. Solution: Verify the row and column numbers point to a symbol name. |   
## Best Practices[](https://kiro.dev/docs/cli/code-intelligence/#best-practices)
  1. Initialize once per project - Run `/code init` in project root
  2. Use exact positions - Row and column must point to the symbol
  3. Use dry_run for renames - Preview changes before applying
  4. Check diagnostics first - Syntax errors can prevent analysis
  5. Be specific in searches - "UserService" > "user"
  6. Ask for documentation naturally - "What does the login method do?" instead of specifying coordinates
  7. Discover APIs conversationally - "What methods does s3Client have?" to explore external library functionality


## Limitations[](https://kiro.dev/docs/cli/code-intelligence/#limitations)
  1. LSP feature support varies by language server - not all servers support every operation (e.g., some may not support rename or formatting)
  2. Large codebases may have slow initial indexing


Page updated: December 18, 2025
[Auto complete](https://kiro.dev/docs/cli/autocomplete/)
[Billing for individuals](https://kiro.dev/docs/cli/billing/)
On this page
  * [Overview](https://kiro.dev/docs/cli/code-intelligence/#overview)
  * [How it works](https://kiro.dev/docs/cli/code-intelligence/#how-it-works)
  * [Installing language servers](https://kiro.dev/docs/cli/code-intelligence/#installing-language-servers)
  * [Initialize Code Intelligence](https://kiro.dev/docs/cli/code-intelligence/#initialize-code-intelligence)
  * [Using Language Servers](https://kiro.dev/docs/cli/code-intelligence/#using-language-servers)
  * [Example 1: Find a Symbol](https://kiro.dev/docs/cli/code-intelligence/#example-1-find-a-symbol)
  * [Example 2: Find All References](https://kiro.dev/docs/cli/code-intelligence/#example-2-find-all-references)
  * [Example 3: Go to Definition](https://kiro.dev/docs/cli/code-intelligence/#example-3-go-to-definition)
  * [Example 4: Get File Symbols](https://kiro.dev/docs/cli/code-intelligence/#example-4-get-file-symbols)
  * [Example 5: Rename with Dry Run](https://kiro.dev/docs/cli/code-intelligence/#example-5-rename-with-dry-run)
  * [Example 6: Get Diagnostics](https://kiro.dev/docs/cli/code-intelligence/#example-6-get-diagnostics)
  * [Example 7: Get Hover Information](https://kiro.dev/docs/cli/code-intelligence/#example-7-get-hover-information)
  * [Example 8: Get Code Completions](https://kiro.dev/docs/cli/code-intelligence/#example-8-get-code-completions)
  * [Custom Language Servers](https://kiro.dev/docs/cli/code-intelligence/#custom-language-servers)
  * [Troubleshooting](https://kiro.dev/docs/cli/code-intelligence/#troubleshooting)
  * [Best Practices](https://kiro.dev/docs/cli/code-intelligence/#best-practices)
  * [Limitations](https://kiro.dev/docs/cli/code-intelligence/#limitations)