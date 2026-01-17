# Steering
## What is steering?[](https://kiro.dev/docs/cli/steering/#what-is-steering)
Steering gives Kiro persistent knowledge about your project through markdown files in `.kiro/steering/`. Instead of explaining your conventions in every chat, steering files ensure Kiro consistently follows your established patterns, libraries, and standards.
## Key benefits[](https://kiro.dev/docs/cli/steering/#key-benefits)
**Consistent Code Generation** - Every component, API endpoint, or test follows your team's established patterns and conventions.
**Reduced Repetition** - No need to explain project standards in each conversation. Kiro remembers your preferences.
**Team Alignment** - All developers work with the same standards, whether they're new to the project or seasoned contributors.
**Scalable Project Knowledge** - Documentation that grows with your codebase, capturing decisions and patterns as your project evolves.
## Steering file scope[](https://kiro.dev/docs/cli/steering/#steering-file-scope)
Steering files can be created with a workspace scope or a global scope.
### Workspace steering[](https://kiro.dev/docs/cli/steering/#workspace-steering)
Workspace steering files reside in your workspace root folder under `.kiro/steering/`, and apply only to that specific workspace. Workspace steering files can be used to inform Kiro of patterns, libraries, and standards that apply to an individual workspace.
### Global steering[](https://kiro.dev/docs/cli/steering/#global-steering)
Global steering files reside in your home directory under `~/.kiro/steering/`, and apply to all workspaces. Global steering files can be used to inform Kiro of conventions that apply to _all_ your workspaces.
In case of conflicting instructions between global and workspace steering, Kiro will prioritize the workspace steering instructions. This allows you to specify global directives that generally apply to all your workspaces, while preserving the ability to override those directives for specific workspaces.
### Team steering[](https://kiro.dev/docs/cli/steering/#team-steering)
The global steering feature can be used to define centralized steering files that apply to entire teams. Team steering files can be pushed to user's PCs via MDM solutions or Group Policies, or downloaded by users to their PCs from a central repository, and placed into the `~/.kiro/steering` folder.
## Foundational steering files[](https://kiro.dev/docs/cli/steering/#foundational-steering-files)
Create foundational steering files to establish core project context.
  1. Create a `.kiro/steering/` folder in your project root for workspace scope or `~/.kiro/steering` folder for global scope.
  2. Add markdown files for your project standards
  3. Kiro will automatically load these files in chat sessions


Foundational steering files are:
**Product Overview** (`product.md`) - Defines your product's purpose, target users, key features, and business objectives. This helps Kiro understand the "why" behind technical decisions and suggest solutions aligned with your product goals.
**Technology Stack** (`tech.md`) - Documents your chosen frameworks, libraries, development tools, and technical constraints. When Kiro suggests implementations, it will prefer your established stack over alternatives.
**Project Structure** (`structure.md`) - Outlines file organization, naming conventions, import patterns, and architectural decisions. This ensures generated code fits seamlessly into your existing codebase.
These foundation files are included in every interaction by default, forming the baseline of Kiro's project understanding.
## Creating custom steering files[](https://kiro.dev/docs/cli/steering/#creating-custom-steering-files)
Extend Kiro's understanding with specialized guidance tailored to your project's unique needs:
  1. Create a new `.md` file in `.kiro/steering/`
  2. Choose a descriptive filename (e.g., `api-standards.md`)
  3. Write your guidance using standard markdown syntax
  4. Use natural language to describe your requirements


Examples:
  * API specs: `#[[file:api/openapi.yaml]]`
  * Component patterns: `#[[file:components/ui/button.tsx]]`
  * Config templates: `#[[file:.env.example]]`


##Agents.md
Kiro supports providing steering directives via the [AGENTS.md](https://agents.md/) standard. AGENTS.md files are in markdown format, similar to Kiro steering files; however, AGENTS.md files are always included.
You can add AGENTS.md files to the global steering file location (`~/.kiro/steering/`), or to the root folder of your workspace, and they will get picked up by Kiro automatically.
## Best practices[](https://kiro.dev/docs/cli/steering/#best-practices)
**Keep Files Focused** One domain per file - API design, testing, or deployment procedures.
**Use Clear Names**
  * `api-rest-conventions.md` - REST API standards
  * `testing-unit-patterns.md` - Unit testing approaches
  * `components-form-validation.md` - Form component standards


**Include Context** Explain why decisions were made, not just what the standards are.
**Provide Examples** Use code snippets and before/after comparisons to demonstrate standards.
**Security First** Never include API keys, passwords, or sensitive data. Steering files are part of your codebase.
**Maintain Regularly**
  * Review during sprint planning and architecture changes
  * Test file references after restructuring
  * Treat steering changes like code changes - require reviews


## Common steering file strategies[](https://kiro.dev/docs/cli/steering/#common-steering-file-strategies)
**API Standards** (`api-standards.md`) - Define REST conventions, error response formats, authentication flows, and versioning strategies. Include endpoint naming patterns, HTTP status code usage, and request/response examples.
**Testing Approach** (`testing-standards.md`) - Establish unit test patterns, integration test strategies, mocking approaches, and coverage expectations. Document preferred testing libraries, assertion styles, and test file organization.
**Code Style** (`code-conventions.md`) - Specify naming patterns, file organization, import ordering, and architectural decisions. Include examples of preferred code structures, component patterns, and anti-patterns to avoid.
**Security Guidelines** (`security-policies.md`) - Document authentication requirements, data validation rules, input sanitization standards, and vulnerability prevention measures. Include secure coding practices specific to your application.
**Deployment Process** (`deployment-workflow.md`) - Outline build procedures, environment configurations, deployment steps, and rollback strategies. Include CI/CD pipeline details and environment-specific requirements.
Custom steering files are stored in `.kiro/steering/` and become immediately available across all Kiro CLI chat sessions.
Page updated: November 21, 2025
[Governance](https://kiro.dev/docs/cli/mcp/governance/)
[Experimental](https://kiro.dev/docs/cli/experimental/)
On this page
  * [What is steering?](https://kiro.dev/docs/cli/steering/#what-is-steering)
  * [Key benefits](https://kiro.dev/docs/cli/steering/#key-benefits)
  * [Steering file scope](https://kiro.dev/docs/cli/steering/#steering-file-scope)
  * [Workspace steering](https://kiro.dev/docs/cli/steering/#workspace-steering)
  * [Global steering](https://kiro.dev/docs/cli/steering/#global-steering)
  * [Team steering](https://kiro.dev/docs/cli/steering/#team-steering)
  * [Foundational steering files](https://kiro.dev/docs/cli/steering/#foundational-steering-files)
  * [Creating custom steering files](https://kiro.dev/docs/cli/steering/#creating-custom-steering-files)
  * [Best practices](https://kiro.dev/docs/cli/steering/#best-practices)
  * [Common steering file strategies](https://kiro.dev/docs/cli/steering/#common-steering-file-strategies)