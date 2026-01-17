---
inclusion: always
---

# Browser Automation - Agent Browser

**IMPORTANT:** When browser automation, web testing, or web interaction tasks are needed, load the Agent Browser skill.

**Read now:** `.kiro/skills/agent-browser-skill/SKILL.md`

## What is Agent Browser?

Agent Browser is a powerful CLI tool for browser automation built on Playwright. It provides a simple command-line interface for navigating websites, interacting with elements, taking screenshots, filling forms, and extracting data from web pages.

## When to Use

Load this skill when the user needs to:
- Navigate and interact with websites
- Test web applications or pages
- Fill out forms automatically
- Take screenshots or generate PDFs
- Extract information from web pages
- Validate web UI/UX
- Test authentication flows
- Check responsive design
- Record browser interactions as video
- Automate any browser-based task

## Quick Reference (Core Commands)

### Navigation
```bash
agent-browser open <url>      # Navigate to URL
agent-browser snapshot -i     # Get interactive elements with refs
agent-browser click @e1       # Click element by ref
agent-browser fill @e2 "text" # Fill input by ref
agent-browser close           # Close browser
```

### Key Workflow
1. **Open** a page: `agent-browser open https://example.com`
2. **Snapshot** to get element refs: `agent-browser snapshot -i`
3. **Interact** using refs: `agent-browser click @e1`, `agent-browser fill @e2 "text"`
4. **Re-snapshot** after navigation or DOM changes

### Common Tasks
- **Screenshots**: `agent-browser screenshot` or `agent-browser screenshot path.png`
- **Form filling**: Use `snapshot -i` to get refs, then `fill @ref "value"`
- **Wait for elements**: `agent-browser wait @e1` or `agent-browser wait --text "Success"`
- **Get information**: `agent-browser get text @e1`, `agent-browser get url`
- **Video recording**: `agent-browser record start ./demo.webm`, perform actions, `agent-browser record stop`

## Progressive Disclosure

The SKILL.md file contains:
- Complete command reference
- All interaction methods (click, fill, type, hover, drag, etc.)
- Advanced features (network interception, cookies, storage, tabs)
- Authentication and state management
- Debugging techniques
- JSON output for parsing

**Only read the full SKILL.md when you need detailed command syntax or advanced features.**

## Key Capabilities

- **Element references**: Snapshot returns `@e1`, `@e2` refs for reliable interaction
- **Multiple interaction modes**: Click, fill, type, hover, drag, scroll, keyboard
- **State management**: Save/load authentication state for reuse
- **Network control**: Intercept, mock, or block requests
- **Multi-session**: Run parallel browsers with `--session` flag
- **Video recording**: Record interactions for demos or debugging
- **Debugging**: Headed mode, console logs, error tracking, element highlighting

**For complete command reference and advanced usage:** Read `.kiro/skills/agent-browser-skill/SKILL.md`
