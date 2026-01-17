---
name: frontend-design-skill
description: Create production-grade frontend interfaces following the Dynamous brand system. Use when building web components, pages, or applications for Dynamous. Implements a sophisticated dark-mode-first design language with glass morphism, signature blue accents, and technical-but-approachable aesthetics.
---

# Dynamous Frontend Design

**Skill Location:** `.kiro/skills/frontend-design-skill`

This skill guides creation of frontend interfaces that embody the **Dynamous brand identity**. Every interface should feel technical yet approachable, sophisticated yet accessible.

**Required reading for implementation details:**
- **Brand philosophy & complete specifications**: See `.kiro/skills/frontend-design-skill/resources/brand-system.md`
- **Live CSS reference & component examples**: See `.kiro/skills/frontend-design-skill/resources/design-system.html`

---

## Brand Philosophy

Before coding, internalize these core principles:

### 1. Technical but Approachable
Complex AI topics made accessible without dumbing them down. Show sophistication, explain it clearly. The interface should feel like it was built by engineers who care about craft.

### 2. Clean over Flashy
No unnecessary decoration. Every visual element has a purpose. Elegance through restraint. One well-placed glow effect beats ten scattered animations.

### 3. Dark Mode by Default
Modern, developer-focused aesthetic. Easy on the eyes for people who stare at screens all day. The dark canvas makes the content shine.

### 4. Intentional Design Choices
Bold decisions executed with precision. If something glows, it should glow for a reason. If something moves, it should move purposefully.

---

## Essential Design Tokens

### Colors — Dynamous Blue is the Hero

```css
/* Primary — Use sparingly for maximum impact */
--dynamous-blue: #3B82F6;      /* Primary buttons, links, hero accents */
--dynamous-dark: #2563EB;      /* Hover states, outlines */
--dynamous-light: #60A5FA;     /* Secondary accents, highlights */

/* Dark Theme (Default) */
--background: #07090F;         /* Near-black with subtle blue tint */
--background-alt: #080A13;     /* Slightly warmer alternative */
--surface: rgba(0, 0, 0, 0.4); /* Glass card backgrounds */
--border: rgba(255, 255, 255, 0.1);

/* Text Hierarchy */
--text-primary: rgba(255, 255, 255, 0.98);   /* Headings */
--text-secondary: rgba(255, 255, 255, 0.8);  /* Body text */
--text-muted: rgba(255, 255, 255, 0.7);      /* Meta, labels */

/* Semantic (use only for meaning, not decoration) */
--success: #047857;  --success-bg: #A7F3D0;
--warning: #B45309;  --warning-bg: #FEF3C7;
--error: #B91C1C;    --error-bg: #FECACA;
--ai-purple: #6D28D9; --ai-purple-bg: #DDD6FE;  /* AI/LLM elements */
```

**Rule**: Dynamous Blue is the hero. Use it for actions and emphasis. Don't dilute by overusing.

### Typography — The Dynamous Stack

```css
--font-sans: 'Inter', ui-sans-serif, system-ui, sans-serif;
--font-mono: 'JetBrains Mono', ui-monospace, monospace;
--font-display: 'Montserrat', var(--font-sans);  /* Thumbnails, bold headlines */
```

| Element | Font | Weight | Notes |
|---------|------|--------|-------|
| Hero/Display | Inter | 700 | Large, impactful headings |
| H1 | Inter | 700 | Page titles |
| H2-H3 | Inter | 600 | Section headers |
| Body | Inter | 400 | Readable paragraphs |
| Buttons | Inter | 500 | Clear CTAs |
| Code | JetBrains Mono | 400 | Developer-friendly |
| Thumbnails | Montserrat | 800 | Maximum impact only |

### Spacing — Multiples of 8px

```css
--space-xs: 4px;   --space-sm: 8px;   --space-md: 12px;
--space-base: 16px; --space-lg: 24px;  --space-xl: 32px;
--space-2xl: 48px;  --space-3xl: 64px;
```

### Border Radius

```css
--radius-sm: 4px;   --radius-md: 8px;   --radius-lg: 12px;
--radius-xl: 16px;  --radius-full: 9999px;
```

---

## Signature Elements

These define the Dynamous visual identity. Use them consistently.

### Glass Card — The Defining Pattern

Frosted glass over dark backgrounds. The signature container for content.

```css
.glass-card {
  background: rgba(0, 0, 0, 0.4);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 12px;
}
```

**Use for**: Content cards, video containers, feature highlights, testimonials.
**Do NOT use for**: Buttons, navigation, form inputs (these need clarity).

### Blue Glow — Signature Emphasis

Creates a soft halo around important elements.

```css
.blue-glow {
  box-shadow: 0 0 15px rgba(59, 130, 246, 0.5),
              0 0 30px rgba(59, 130, 246, 0.3);
}

.text-glow {
  text-shadow: 0 0 10px rgba(59, 130, 246, 0.5),
               0 0 20px rgba(59, 130, 246, 0.3);
}
```

**Use for**: Hero text highlights, primary buttons, featured content, logo in hero sections.
**Rule**: Use sparingly. If everything glows, nothing does.

### Primary Button

```css
.btn-primary {
  background: var(--dynamous-blue);
  color: white;
  font-weight: 500;
  padding: 8px 16px;
  border-radius: 8px;
  box-shadow: 0 4px 14px -4px rgba(59, 130, 246, 0.4);
  transition: all 200ms cubic-bezier(0, 0, 0.2, 1);
}

.btn-primary:hover {
  background: var(--dynamous-dark);
  transform: translateY(-1px);
  box-shadow: 0 6px 20px -4px rgba(59, 130, 246, 0.5);
}
```

### Hero Gradient Background

```css
background: linear-gradient(to bottom, #07090f, rgba(30, 58, 138, 0.9), #080a13);
background-attachment: fixed;
```

### Grid Pattern (Subtle Background Texture)

```css
.grid-pattern {
  background-image:
    linear-gradient(to right, rgba(99, 102, 241, 0.05) 1px, transparent 1px),
    linear-gradient(to bottom, rgba(99, 102, 241, 0.05) 1px, transparent 1px);
  background-size: 40px 40px;
}
```

---

## Motion Guidelines

Nothing should take longer than 600ms. Snappy > smooth.

```css
--duration-micro: 150ms;  /* Button states, toggles */
--duration-fast: 200ms;   /* Dropdowns, small transitions */
--duration-normal: 300ms; /* Cards, modals */
--duration-slow: 600ms;   /* Page transitions, fade-ins */

--ease-out: cubic-bezier(0, 0, 0.2, 1);  /* Entrances */
--ease-in: cubic-bezier(0.4, 0, 1, 1);   /* Exits */
/* Never use linear for UI — feels robotic */
```

### Signature Animations

```css
/* Float — decorative elements */
@keyframes float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}
animation: float 6s ease-in-out infinite;

/* Fade-in — content entrance */
@keyframes fade-in {
  0% { opacity: 0; transform: translateY(10px); }
  100% { opacity: 1; transform: translateY(0); }
}
animation: fade-in 0.6s ease-out forwards;

/* Shimmer — button hover effect */
.btn::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
  transform: translateX(-100%);
  transition: transform 0.5s ease;
}
.btn:hover::before { transform: translateX(100%); }
```

### What Moves vs. What Doesn't

**Moves**: Buttons, cards on hover, decorative logos, page sections on scroll, modals.
**Stays grounded**: Body text, navigation, form inputs, critical UI.

---

## Anti-Patterns — What to Avoid

### Generic AI Aesthetics (AI Slop)
- Cliched purple gradients on white backgrounds
- Overused generic illustrations
- Cookie-cutter layouts without context
- Random floating geometric shapes
- Excessive glossy 3D elements

### Breaking Brand Consistency
- Using colors outside the Dynamous palette
- Light mode as default (always dark-first)
- Fonts other than Inter/Montserrat/JetBrains Mono
- Rounded corners that don't match the system (8px, 12px, 16px)
- Borders thicker than 1px for subtle elements

### Motion Mistakes
- Animations longer than 600ms
- Linear easing for UI transitions
- Animating body text
- Everything moving at once (use stagger delays)

### Glow Overuse
- Glowing everything (dilutes impact)
- Glow on non-interactive elements
- Multiple glow colors competing

---

## Implementation Workflow

1. **Start with the dark canvas**: `background: #07090F`
2. **Establish text hierarchy**: Primary (98%), secondary (80%), muted (70%)
3. **Add glass cards for containers**: The signature frosted effect
4. **Use Dynamous Blue for actions**: Buttons, links, highlights only
5. **Apply glow effects sparingly**: Hero elements, primary CTAs
6. **Add motion last**: Entrance animations, hover states

---

## When to Consult Reference Files

**Read `.kiro/skills/frontend-design-skill/resources/brand-system.md` when you need:**
- Complete color specifications with HSL values
- Full typography rules and line heights
- Icon specifications (Lucide React, sizes)
- YouTube thumbnail specifications
- Diagram colors for Excalidraw
- Image treatment guidelines
- Complete CSS variables reference

**Read `.kiro/skills/frontend-design-skill/resources/design-system.html` when you need:**
- Live component examples to reference
- Exact CSS implementations
- Interactive demos of animations
- Color swatches you can inspect
- Complete button/input/card variants

---

## Quick Reference

| Element | Implementation |
|---------|----------------|
| Background | `#07090F` or hero gradient |
| Card | Glass morphism with `rgba(0,0,0,0.4)` + blur |
| Primary action | Dynamous Blue `#3B82F6` |
| Text | 98%/80%/70% white opacity hierarchy |
| Borders | `rgba(255,255,255,0.1)` always |
| Corners | 8px buttons, 12px cards |
| Emphasis | Blue glow, use once per viewport |
| Motion | ≤600ms, ease-out for entrances |

---

Remember: Dynamous interfaces should feel like they were crafted by engineers who deeply care about both technical excellence and visual design. Every pixel has purpose. Every animation has intent. Every glow creates focus.
