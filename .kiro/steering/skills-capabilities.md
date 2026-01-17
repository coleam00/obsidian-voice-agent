---
inclusion: always
---

# Available Skills

This workspace has specialized skills that extend your capabilities. **Load the appropriate skill when working on relevant tasks.**

## Skill Index

### 1. Frontend Design Skill
**Location:** `.kiro/skills/frontend-design-skill/SKILL.md`
**Description:** Create production-grade frontend interfaces following the Dynamous brand system. Implements a sophisticated dark-mode-first design language with glass morphism, signature blue accents (#3B82F6), and technical-but-approachable aesthetics.

**When to use:**
- Building any web component, page, or application
- Creating HTML/CSS layouts
- Designing React, Vue, or other frontend components
- Styling user interfaces
- When the user asks for "beautiful", "production-grade", or "Dynamous-style" frontends

**How to activate:**
Read `.kiro/skills/frontend-design-skill/SKILL.md` before starting any frontend work. The skill contains:
- Complete Dynamous brand philosophy and design tokens
- Color system, typography, spacing specifications
- Signature elements (glass cards, blue glow effects)
- Anti-patterns to avoid (generic AI aesthetics)

**Key brand elements (quick reference):**
- Background: `#07090F` (dark mode default)
- Primary accent: `#3B82F6` (Dynamous Blue)
- Fonts: Inter (UI), Montserrat (display), JetBrains Mono (code)
- Glass cards: `rgba(0,0,0,0.4)` + `backdrop-filter: blur(16px)`

---

### 2. Agent Browser Skill
**Location:** `.kiro/skills/agent-browser-skill/SKILL.md`
**Description:** Browser automation with Agent Browser CLI built on Playwright. Navigate websites, interact with elements via refs, take screenshots, fill forms, extract data, test web apps, record videos, manage authentication state, and automate any browser task.

**When to use:**
- Testing websites or web applications
- Browser automation tasks
- Taking screenshots or generating PDFs
- Form filling and submission testing
- Extracting information from web pages
- Responsive design validation
- Login flow testing
- Video recording of browser interactions
- Any browser-based testing or automation

**How to activate:**
Read `.kiro/skills/agent-browser-skill/SKILL.md` before browser automation tasks. The skill contains:
- Complete command reference
- Element reference system (`@e1`, `@e2` from snapshots)
- Interaction methods (click, fill, type, hover, drag)
- Advanced features (network, cookies, storage, tabs)
- Authentication state management
- Debugging techniques

**Critical workflow:**
1. Open page: `agent-browser open <url>`
2. Get element refs: `agent-browser snapshot -i`
3. Interact: `agent-browser click @e1`, `agent-browser fill @e2 "text"`
4. Re-snapshot after navigation or DOM changes

---

## Skill Usage Instructions

When a task matches a skill's use case:

1. **Read the SKILL.md file** for that skill before starting work
2. **Follow the skill's instructions** exactly as documented
3. **Use progressive disclosure** - only read additional reference files (like `resources/brand-system.md` or `API_REFERENCE.md`) when you need deeper details
4. **Apply the skill's patterns consistently** throughout the task

**Important:** Skills contain detailed instructions that significantly improve output quality. Always load the relevant skill rather than relying on general knowledge.
