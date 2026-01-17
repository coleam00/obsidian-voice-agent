# Knowledge management
The `/knowledge` command provides persistent knowledge base functionality for Kiro CLI, allowing you to store, search, and manage contextual information that persists across chat sessions.
## Getting started[](https://kiro.dev/docs/cli/experimental/knowledge-management/#getting-started)
### Enable knowledge feature[](https://kiro.dev/docs/cli/experimental/knowledge-management/#enable-knowledge-feature)
Knowledge management is experimental and must be enabled before use:
bash
```

kiro-cli settings chat.enableKnowledge true


```

### Basic usage[](https://kiro.dev/docs/cli/experimental/knowledge-management/#basic-usage)
Once enabled, use `/knowledge` commands within your chat session:
bash
```

/knowledge add --name myproject --path /path/to/project
/knowledge show


```

## Commands[](https://kiro.dev/docs/cli/experimental/knowledge-management/#commands)
### /knowledge show[](https://kiro.dev/docs/cli/experimental/knowledge-management/#knowledge-show)
Display all entries in your knowledge base with detailed information including creation dates, item counts, and persistence status. Also shows any active background indexing operations with progress and ETA.
This unified command provides a complete view of both your stored knowledge and ongoing operations.
bash
```

/knowledge show


```

### /knowledge add[](https://kiro.dev/docs/cli/experimental/knowledge-management/#knowledge-add)
Add files or directories to your knowledge base. The system recursively indexes all supported files in directories.
**Syntax:**
bash
```

/knowledge add --name <name> --path <path> [--include pattern] [--exclude pattern] [--index-type Fast|Best]


```

**Required Parameters:**
  * `--name` or `-n`: Descriptive name for the knowledge entry
  * `--path` or `-p`: Path to file or directory to index


**Examples:**
bash
```

/knowledge add --name "project-docs" --path /path/to/documentation
/knowledge add -n "config-files" -p /path/to/config.json
/knowledge add --name "fast-search" --path /path/to/logs --index-type Fast
/knowledge add -n "semantic-search" -p /path/to/docs --index-type Best


```

### Index types[](https://kiro.dev/docs/cli/experimental/knowledge-management/#index-types)
Choose the indexing approach that best fits your needs:
#### Fast (Lexical - bm25)[](https://kiro.dev/docs/cli/experimental/knowledge-management/#fast-lexical---bm25)
**Advantages:**
  * ✅ Lightning-fast indexing - processes files quickly
  * ✅ Instant search - keyword-based with immediate results
  * ✅ Low resource usage - minimal CPU and memory
  * ✅ Perfect for logs, configs, and large codebases


**Disadvantages:**
  * ❌ Less intelligent - requires exact keyword matches


#### Best (Semantic - all-minilm-l6-v2)[](https://kiro.dev/docs/cli/experimental/knowledge-management/#best-semantic---all-minilm-l6-v2)
**Advantages:**
  * ✅ Intelligent search - understands context and meaning
  * ✅ Natural language queries - search with full sentences
  * ✅ Finds related concepts - even without exact keywords
  * ✅ Perfect for documentation and research


**Disadvantages:**
  * ❌ Slower indexing - requires AI model processing
  * ❌ Higher resource usage - more CPU and memory intensive


### When to use each type[](https://kiro.dev/docs/cli/experimental/knowledge-management/#when-to-use-each-type)
Use Case | Recommended Type | Why  
---|---|---  
Log files, error messages | Fast | Quick keyword searches, large volumes  
Configuration files | Fast | Exact parameter/value lookups  
Large codebases | Fast | Fast symbol and function searches  
Documentation | Best | Natural language understanding  
Research papers | Best | Concept-based searching  
Mixed content | Best | Better overall search experience  
### Default behavior[](https://kiro.dev/docs/cli/experimental/knowledge-management/#default-behavior)
If you don't specify `--index-type`, the system uses your configured default:
bash
```

# Set your preferred default
kiro-cli settings knowledge.indexType Fast   # or Best

# This will use your default setting
/knowledge add "my-project" /path/to/project


```

### Pattern filtering[](https://kiro.dev/docs/cli/experimental/knowledge-management/#pattern-filtering)
Control which files are indexed using include and exclude patterns:
bash
```

/knowledge add "rust-code" /path/to/project --include "*.rs" --exclude "target/**"
/knowledge add "docs" /path/to/project --include "**/*.md" --include "**/*.txt" --exclude "node_modules/**"


```

**Pattern Examples:**
  * `*.rs` - All Rust files recursively (equivalent to `**/*.rs`)
  * `**/*.py` - All Python files recursively
  * `target/**` - Everything in target directory
  * `node_modules/**` - Everything in node_modules


**Default Pattern Behavior:**
When you don't specify patterns, the system uses configured defaults:
bash
```

kiro-cli settings knowledge.defaultIncludePatterns '["**/*.rs", "**/*.py"]'
kiro-cli settings knowledge.defaultExcludePatterns '["target/**", "__pycache__/**"]'

# Uses default patterns
/knowledge add "my-project" /path/to/project

# Overrides defaults
/knowledge add "docs-only" /path/to/project --include "**/*.md"


```

### Supported file types[](https://kiro.dev/docs/cli/experimental/knowledge-management/#supported-file-types)
**Text files:** .txt, .log, .rtf, .tex, .rst
**Markdown:** .md, .markdown, .mdx
**JSON:** .json (treated as text for searchability)
**Configuration:** .ini, .conf, .cfg, .properties, .env
**Data files:** .csv, .tsv
**Web formats:** .svg (text-based)
**Code files:** .rs, .py, .js, .jsx, .ts, .tsx, .java, .c, .cpp, .h, .hpp, .go, .rb, .php, .swift, .kt, .kts, .cs, .sh, .bash, .zsh, .html, .htm, .xml, .css, .scss, .sass, .less, .sql, .yaml, .yml, .toml
**Special files:** Dockerfile, Makefile, LICENSE, CHANGELOG, README (files without extensions)
**Note:** Unsupported files are indexed without text content extraction.
### /knowledge remove[](https://kiro.dev/docs/cli/experimental/knowledge-management/#knowledge-remove)
Remove entries from your knowledge base by name, path, or context ID.
bash
```

/knowledge remove "project-docs"  # Remove by name
/knowledge remove /path/to/old/project  # Remove by path


```

### /knowledge update[](https://kiro.dev/docs/cli/experimental/knowledge-management/#knowledge-update)
Update an existing knowledge base entry with new content. Original include/exclude patterns are preserved.
bash
```

/knowledge update /path/to/updated/project


```

### /knowledge clear[](https://kiro.dev/docs/cli/experimental/knowledge-management/#knowledge-clear)
Remove all entries from your knowledge base. Requires confirmation and cannot be undone.
bash
```

/knowledge clear


```

You'll be prompted:
```

⚠️ This will remove ALL knowledge base entries. Are you sure? (y/N):


```

### /knowledge cancel[](https://kiro.dev/docs/cli/experimental/knowledge-management/#knowledge-cancel)
Cancel background operations. Cancel specific operation by ID or all operations.
bash
```

/knowledge cancel abc12345  # Cancel specific operation
/knowledge cancel all       # Cancel all operations


```

## Configuration[](https://kiro.dev/docs/cli/experimental/knowledge-management/#configuration)
Configure knowledge base behavior:
bash
```

# Maximum files per knowledge base
kiro-cli settings knowledge.maxFiles 10000

# Text chunk size for processing
kiro-cli settings knowledge.chunkSize 1024

# Overlap between chunks
kiro-cli settings knowledge.chunkOverlap 256

# Default index type
kiro-cli settings knowledge.indexType Fast

# Default include patterns
kiro-cli settings knowledge.defaultIncludePatterns '["**/*.rs", "**/*.md"]'

# Default exclude patterns
kiro-cli settings knowledge.defaultExcludePatterns '["target/**", "node_modules/**"]'


```

## Agent-specific knowledge bases[](https://kiro.dev/docs/cli/experimental/knowledge-management/#agent-specific-knowledge-bases)
### Isolated knowledge storage[](https://kiro.dev/docs/cli/experimental/knowledge-management/#isolated-knowledge-storage)
Each agent maintains its own isolated knowledge base, ensuring knowledge contexts are scoped to the specific agent you're working with. This provides better organization and prevents knowledge conflicts.
### Folder structure[](https://kiro.dev/docs/cli/experimental/knowledge-management/#folder-structure)
Knowledge bases are stored in:
```

~/.kiro/knowledge_bases/
├── kiro_cli_default/          # Default agent
│   ├── contexts.json
│   ├── context-id-1/
│   │   ├── data.json
│   │   └── bm25_data.json
│   └── context-id-2/
│       └── data.json
├── my-custom-agent_<code>/    # Custom agent
│   ├── contexts.json
│   └── context-id-3/
│       └── data.json
└── another-agent_<code>/      # Another agent
    ├── contexts.json
    └── context-id-4/
        └── data.json


```

### How agent isolation works[](https://kiro.dev/docs/cli/experimental/knowledge-management/#how-agent-isolation-works)
  * **Automatic Scoping** : `/knowledge` commands operate on current agent's knowledge base
  * **No Cross-Agent Access** : Agent A cannot access Agent B's knowledge
  * **Independent Configuration** : Each agent has different settings and contexts
  * **Migration Support** : Legacy knowledge bases migrate to default agent


### Agent switching[](https://kiro.dev/docs/cli/experimental/knowledge-management/#agent-switching)
When you switch agents, knowledge commands automatically work with that agent's knowledge base:
bash
```

# Working with default agent
/knowledge add /path/to/docs

# Switch to custom agent
kiro chat --agent my-custom-agent

# Creates separate knowledge base for my-custom-agent
/knowledge add /path/to/agent/docs

# Switch back to default
kiro chat

# Only sees original docs, not agent-specific docs
/knowledge show


```

## How it works[](https://kiro.dev/docs/cli/experimental/knowledge-management/#how-it-works)
### Indexing process[](https://kiro.dev/docs/cli/experimental/knowledge-management/#indexing-process)
  1. **Pattern Filtering** : Files filtered by include/exclude patterns
  2. **File Discovery** : Recursive scan for supported file types
  3. **Content Extraction** : Text extracted from each file
  4. **Chunking** : Large files split into searchable chunks
  5. **Background Processing** : Asynchronous indexing
  6. **Semantic Embedding** : Content processed for semantic search


### Search capabilities[](https://kiro.dev/docs/cli/experimental/knowledge-management/#search-capabilities)
Knowledge bases use semantic search:
  * Natural language queries
  * Results ranked by relevance, not just keywords
  * Related concepts found even without exact word matches


### Persistence[](https://kiro.dev/docs/cli/experimental/knowledge-management/#persistence)
  * Contexts survive across chat sessions and CLI restarts
  * Persistence determined automatically by usage patterns
  * Include/exclude patterns stored and reused during updates


## Best practices[](https://kiro.dev/docs/cli/experimental/knowledge-management/#best-practices)
### Organizing your knowledge base[](https://kiro.dev/docs/cli/experimental/knowledge-management/#organizing-your-knowledge-base)
  * Use descriptive names: "api-documentation" not "docs"
  * Group related files in directories before adding
  * Use include/exclude patterns to focus on relevant files
  * Regularly review and update outdated contexts


### Effective searching[](https://kiro.dev/docs/cli/experimental/knowledge-management/#effective-searching)
  * Use natural language: "how to handle authentication errors using the knowledge tool"
  * Be specific: "database connection configuration"
  * Try different phrasings if initial searches don't work
  * Prompt Kiro to use the tool: "find database connection configuration using your knowledge bases"


### Managing large projects[](https://kiro.dev/docs/cli/experimental/knowledge-management/#managing-large-projects)
  * Add project directories rather than individual files
  * Use patterns to avoid build artifacts: `--exclude "target/**" --exclude "node_modules/**"`
  * Use `/knowledge show` to monitor indexing progress
  * Consider breaking large projects into logical sub-directories


### Pattern filtering best practices[](https://kiro.dev/docs/cli/experimental/knowledge-management/#pattern-filtering-best-practices)
  * **Be specific** : Use precise patterns to avoid over-inclusion
  * **Exclude build artifacts** : Always exclude `target/**`, `node_modules/**`, `.git/**`
  * **Include relevant extensions** : Focus on file types you need
  * **Test patterns** : Verify patterns match expected files before large operations


## Limitations[](https://kiro.dev/docs/cli/experimental/knowledge-management/#limitations)
### File type support[](https://kiro.dev/docs/cli/experimental/knowledge-management/#file-type-support)
  * Binary files ignored during indexing
  * Very large files may be chunked, potentially splitting related content
  * Some specialized formats may not extract content optimally


### Performance considerations[](https://kiro.dev/docs/cli/experimental/knowledge-management/#performance-considerations)
  * Large directories may take significant time to index
  * Background operations limited by concurrent processing
  * Search performance varies by knowledge base size
  * Pattern filtering improves performance for large directories


### Storage and persistence[](https://kiro.dev/docs/cli/experimental/knowledge-management/#storage-and-persistence)
  * No explicit storage size limits, but practical limits apply
  * No automatic cleanup of old or unused contexts
  * Clear operations are irreversible with no backup


## Troubleshooting[](https://kiro.dev/docs/cli/experimental/knowledge-management/#troubleshooting)
### Files not being indexed[](https://kiro.dev/docs/cli/experimental/knowledge-management/#files-not-being-indexed)
  1. **Check patterns** : Ensure include patterns match your files
  2. **Verify exclude patterns** : Make sure they're not filtering desired files
  3. **Check file types** : Ensure files have supported extensions
  4. **Monitor progress** : Use `/knowledge show` to check indexing status
  5. **Verify paths** : Ensure paths exist and are accessible
  6. **Check for errors** : Look for error messages in CLI output


### Search not finding expected results[](https://kiro.dev/docs/cli/experimental/knowledge-management/#search-not-finding-expected-results)
  1. **Wait for indexing** : Use `/knowledge show` to ensure completion
  2. **Try different queries** : Use various phrasings and keywords
  3. **Verify content** : Confirm content was added with `/knowledge show`
  4. **Check file types** : Unsupported types won't have searchable content


### Performance issues[](https://kiro.dev/docs/cli/experimental/knowledge-management/#performance-issues)
  1. **Check operations** : Use `/knowledge show` for progress
  2. **Cancel if needed** : Use `/knowledge cancel` for problematic operations
  3. **Add smaller chunks** : Consider subdirectories instead of entire projects
  4. **Use better patterns** : Exclude unnecessary files
  5. **Adjust settings** : Lower `maxFiles` or `chunkSize` for better performance


### Pattern issues[](https://kiro.dev/docs/cli/experimental/knowledge-management/#pattern-issues)
  1. **Test patterns** : Start simple, then add complexity
  2. **Check syntax** : Ensure glob patterns use correct syntax (`**` for recursive)
  3. **Verify paths** : Make sure patterns match actual file paths
  4. **Use absolute patterns** : Consider full paths for precision


## Next steps[](https://kiro.dev/docs/cli/experimental/knowledge-management/#next-steps)
  * [Context Management](https://kiro.dev/docs/cli/chat/context/)
  * [Custom Agents](https://kiro.dev/docs/cli/custom-agents)
  * [Settings Configuration](https://kiro.dev/docs/cli/reference/settings)
  * [Experimental Features](https://kiro.dev/docs/cli/experimental)


Page updated: December 8, 2025
[Experimental](https://kiro.dev/docs/cli/experimental/)
[Tangent mode](https://kiro.dev/docs/cli/experimental/tangent-mode/)
On this page
  * [Getting started](https://kiro.dev/docs/cli/experimental/knowledge-management/#getting-started)
  * [Enable knowledge feature](https://kiro.dev/docs/cli/experimental/knowledge-management/#enable-knowledge-feature)
  * [Basic usage](https://kiro.dev/docs/cli/experimental/knowledge-management/#basic-usage)
  * [Commands](https://kiro.dev/docs/cli/experimental/knowledge-management/#commands)
  * [/knowledge show](https://kiro.dev/docs/cli/experimental/knowledge-management/#knowledge-show)
  * [/knowledge add](https://kiro.dev/docs/cli/experimental/knowledge-management/#knowledge-add)
  * [Index types](https://kiro.dev/docs/cli/experimental/knowledge-management/#index-types)
  * [Fast (Lexical - bm25)](https://kiro.dev/docs/cli/experimental/knowledge-management/#fast-lexical---bm25)
  * [Best (Semantic - all-minilm-l6-v2)](https://kiro.dev/docs/cli/experimental/knowledge-management/#best-semantic---all-minilm-l6-v2)
  * [When to use each type](https://kiro.dev/docs/cli/experimental/knowledge-management/#when-to-use-each-type)
  * [Default behavior](https://kiro.dev/docs/cli/experimental/knowledge-management/#default-behavior)
  * [Pattern filtering](https://kiro.dev/docs/cli/experimental/knowledge-management/#pattern-filtering)
  * [Supported file types](https://kiro.dev/docs/cli/experimental/knowledge-management/#supported-file-types)
  * [/knowledge remove](https://kiro.dev/docs/cli/experimental/knowledge-management/#knowledge-remove)
  * [/knowledge update](https://kiro.dev/docs/cli/experimental/knowledge-management/#knowledge-update)
  * [/knowledge clear](https://kiro.dev/docs/cli/experimental/knowledge-management/#knowledge-clear)
  * [/knowledge cancel](https://kiro.dev/docs/cli/experimental/knowledge-management/#knowledge-cancel)
  * [Configuration](https://kiro.dev/docs/cli/experimental/knowledge-management/#configuration)
  * [Agent-specific knowledge bases](https://kiro.dev/docs/cli/experimental/knowledge-management/#agent-specific-knowledge-bases)
  * [Isolated knowledge storage](https://kiro.dev/docs/cli/experimental/knowledge-management/#isolated-knowledge-storage)
  * [Folder structure](https://kiro.dev/docs/cli/experimental/knowledge-management/#folder-structure)
  * [How agent isolation works](https://kiro.dev/docs/cli/experimental/knowledge-management/#how-agent-isolation-works)
  * [Agent switching](https://kiro.dev/docs/cli/experimental/knowledge-management/#agent-switching)
  * [How it works](https://kiro.dev/docs/cli/experimental/knowledge-management/#how-it-works)
  * [Indexing process](https://kiro.dev/docs/cli/experimental/knowledge-management/#indexing-process)
  * [Search capabilities](https://kiro.dev/docs/cli/experimental/knowledge-management/#search-capabilities)
  * [Persistence](https://kiro.dev/docs/cli/experimental/knowledge-management/#persistence)
  * [Best practices](https://kiro.dev/docs/cli/experimental/knowledge-management/#best-practices)
  * [Organizing your knowledge base](https://kiro.dev/docs/cli/experimental/knowledge-management/#organizing-your-knowledge-base)
  * [Effective searching](https://kiro.dev/docs/cli/experimental/knowledge-management/#effective-searching)
  * [Managing large projects](https://kiro.dev/docs/cli/experimental/knowledge-management/#managing-large-projects)
  * [Pattern filtering best practices](https://kiro.dev/docs/cli/experimental/knowledge-management/#pattern-filtering-best-practices)
  * [Limitations](https://kiro.dev/docs/cli/experimental/knowledge-management/#limitations)
  * [File type support](https://kiro.dev/docs/cli/experimental/knowledge-management/#file-type-support)
  * [Performance considerations](https://kiro.dev/docs/cli/experimental/knowledge-management/#performance-considerations)
  * [Storage and persistence](https://kiro.dev/docs/cli/experimental/knowledge-management/#storage-and-persistence)
  * [Troubleshooting](https://kiro.dev/docs/cli/experimental/knowledge-management/#troubleshooting)
  * [Files not being indexed](https://kiro.dev/docs/cli/experimental/knowledge-management/#files-not-being-indexed)
  * [Search not finding expected results](https://kiro.dev/docs/cli/experimental/knowledge-management/#search-not-finding-expected-results)
  * [Performance issues](https://kiro.dev/docs/cli/experimental/knowledge-management/#performance-issues)
  * [Pattern issues](https://kiro.dev/docs/cli/experimental/knowledge-management/#pattern-issues)
  * [Next steps](https://kiro.dev/docs/cli/experimental/knowledge-management/#next-steps)