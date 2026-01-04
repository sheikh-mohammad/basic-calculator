---
name: frontend-design
description: This skill should be used when creating modern, aesthetically pleasing frontend components using HTML, CSS, JS, and Tailwind CSS with contemporary design principles inspired by clean SaaS and AI product interfaces.
---

# Modern Frontend Design Builder

Creates contemporary frontend components and interfaces using HTML, CSS, JS, and Tailwind CSS with modern aesthetic principles.

## Core Design Principles

### Visual Aesthetics
- **Clean Layouts**: Ample white space with clear visual hierarchy
- **Card-Based Organization**: Content organized in distinct, separated containers
- **Professional Typography**: Modern sans-serif fonts with varied weights and sizes
- **Sophisticated Color Palette**: Professional blues and grays with strategic accent colors
- **Depth Effects**: Multi-layered shadows creating premium feel (macOS window effect)
- **Subtle Animations**: Entrance animations, hover effects, and typing indicators
- **Visual Elements**: Strategic icons, tables, and progressive disclosure

### Technical Implementation
- HTML5 semantic structure
- Tailwind CSS for styling with custom configuration
- Vanilla JavaScript for interactivity
- Responsive design principles
- Accessibility best practices

## Before Implementation

Gather context to ensure successful implementation:

| Source | Gather |
|--------|--------|
| **Codebase** | Existing structure, patterns, conventions to integrate with |
| **Conversation** | User's specific requirements, constraints, preferences |
| **Skill References** | Modern design patterns, Tailwind utilities, accessibility standards |
| **User Guidelines** | Project-specific conventions, team standards |

Ensure all required context is gathered before implementing.

## Implementation Standards

### HTML Structure
- Semantic HTML5 elements
- Proper heading hierarchy (h1 → h6)
- Accessible ARIA attributes where needed
- Proper form structure with labels

### CSS/Tailwind Guidelines
- Use Tailwind utility classes primarily
- Custom components in separate CSS files when needed
- Responsive breakpoints: sm, md, lg, xl, 2xl
- Consistent spacing with Tailwind scale
- Z-index management for depth effects

### JavaScript Patterns
- Event delegation for dynamic content
- Progressive enhancement approach
- Performance-conscious animations
- Clean, readable code with comments for complex logic

### Modern Design Elements
- Card-based layouts with subtle shadows
- Gradient backgrounds (subtle)
- Hover animations and transitions
- Clean typography with proper hierarchy
- Consistent spacing and alignment
- Mobile-first responsive design

## Output Specifications

### Component Structure
```
component/
├── index.html
├── style.css (or tailwind.config.js)
├── script.js
└── README.md
```

### Quality Checklist
- [ ] Responsive on all device sizes
- [ ] Accessible to screen readers
- [ ] Performance optimized
- [ ] Cross-browser compatible
- [ ] Modern aesthetic consistent
- [ ] Clean, maintainable code

## Implementation Workflow

1. **Analyze Requirements**
   - Determine component type needed
   - Identify specific functionality
   - Consider responsive behavior

2. **Design Structure**
   - Plan HTML semantic structure
   - Map out visual hierarchy
   - Plan responsive breakpoints

3. **Implement Design**
   - Create HTML structure
   - Apply Tailwind styling
   - Add JavaScript interactivity

4. **Refine Aesthetics**
   - Apply modern design principles
   - Add subtle animations
   - Ensure visual consistency

5. **Test & Validate**
   - Check responsiveness
   - Verify accessibility
   - Optimize performance

## Common Component Patterns

### Card Component
- Clean container with subtle shadow
- Consistent padding and spacing
- Hover effects for interactivity
- Proper content hierarchy

### Button Component
- Clear visual states (default, hover, active)
- Consistent sizing and spacing
- Appropriate feedback on interaction
- Accessible focus states

### Form Component
- Clear labeling and instructions
- Proper validation feedback
- Consistent styling
- Accessible interactions

### Navigation Component
- Clear visual hierarchy
- Responsive behavior
- Consistent styling
- Accessible menu patterns

## Tailwind Configuration

Use these recommended Tailwind configurations for modern aesthetics:

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      boxShadow: {
        'modern': '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)',
        'elevated': '0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)',
      },
      colors: {
        'modern-blue': {
          50: '#eff6ff',
          100: '#dbeafe',
          200: '#bfdbfe',
          300: '#93c5fd',
          400: '#60a5fa',
          500: '#3b82f6',
          600: '#2563eb',
          700: '#1d4ed8',
          800: '#1e40af',
          900: '#1e3a8a',
        }
      }
    }
  }
}
```

## Accessibility Guidelines

- Proper semantic HTML structure
- Sufficient color contrast
- Keyboard navigation support
- ARIA attributes for complex components
- Focus management for interactive elements