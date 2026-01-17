---
inclusion: fileMatch
fileMatchPattern: "**/*.{html,css,tsx,jsx,vue,svelte,scss,sass,less}"
---

# Frontend Design - Dynamous Brand

**IMPORTANT:** You are working on frontend files. Load and follow the Dynamous frontend design skill.

**Read now:** `.kiro/skills/frontend-design-skill/SKILL.md`

## Quick Reference (Essential Tokens)

### Colors
```css
--dynamous-blue: #3B82F6;      /* Primary actions, links, hero accents */
--background: #07090F;         /* Dark mode default */
--surface: rgba(0, 0, 0, 0.4); /* Glass card backgrounds */
--border: rgba(255, 255, 255, 0.1);
--text-primary: rgba(255, 255, 255, 0.98);
--text-secondary: rgba(255, 255, 255, 0.8);
```

### Typography
- **UI text:** Inter
- **Display/Headlines:** Montserrat (weight 800)
- **Code:** JetBrains Mono

### Signature Glass Card
```css
.glass-card {
  background: rgba(0, 0, 0, 0.4);
  backdrop-filter: blur(16px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 12px;
}
```

### Blue Glow (Use Sparingly)
```css
box-shadow: 0 0 15px rgba(59, 130, 246, 0.5),
            0 0 30px rgba(59, 130, 246, 0.3);
```

## Anti-Patterns to Avoid
- Light mode as default (always dark-first)
- Purple gradients on white backgrounds
- Fonts other than Inter/Montserrat/JetBrains Mono
- Overusing glow effects
- Animations longer than 600ms

**For complete specifications:** Read `.kiro/skills/frontend-design-skill/resources/brand-system.md`
