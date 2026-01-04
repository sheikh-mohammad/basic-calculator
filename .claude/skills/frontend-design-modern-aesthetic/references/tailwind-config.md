# Tailwind CSS Configuration for Modern Design

## Recommended Tailwind Configuration

```js
// tailwind.config.js
module.exports = {
  content: [
    "./src/**/*.{html,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      boxShadow: {
        'modern': '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)',
        'elevated': '0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)',
        'floating': '0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)',
        'mac-window': '0 12px 28px 0 rgba(0, 0, 0, 0.2), 0 2px 4px 0 rgba(0, 0, 0, 0.1), inset 0 0 0 1px rgba(255, 255, 255, 0.5)',
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
        },
        'neutral': {
          50: '#f9fafb',
          100: '#f3f4f6',
          200: '#e5e7eb',
          300: '#d1d5db',
          400: '#9ca3af',
          500: '#6b7280',
          600: '#4b5563',
          700: '#374151',
          800: '#1f2937',
          900: '#111827',
        }
      },
      animation: {
        'fade-in': 'fadeIn 0.5s ease-in forwards',
        'slide-up': 'slideUp 0.3s ease-out forwards',
        'pulse-slow': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { transform: 'translateY(10px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        }
      },
      transitionProperty: {
        'height': 'height',
        'spacing': 'margin, padding',
      }
    },
  },
  plugins: [
    // Add any custom plugins here
  ],
}
```

## Common Tailwind Component Patterns

### Modern Card Component
```html
<div class="bg-white rounded-xl shadow-modern p-6 hover:shadow-elevated transition-shadow duration-300">
  <div class="flex items-start space-x-4">
    <div class="flex-shrink-0">
      <!-- Content -->
    </div>
    <div class="flex-1 min-w-0">
      <!-- Content -->
    </div>
  </div>
</div>
```

### Button with Modern Styling
```html
<!-- Primary Button -->
<button class="px-4 py-2 bg-modern-blue-600 text-white rounded-lg hover:bg-modern-blue-700 transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-modern-blue-500 focus:ring-offset-2">
  Button Text
</button>

<!-- Secondary Button -->
<button class="px-4 py-2 border border-neutral-300 text-neutral-700 rounded-lg hover:bg-neutral-50 transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-modern-blue-500 focus:ring-offset-2">
  Button Text
</button>
```

### Responsive Grid
```html
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
  <!-- Grid items -->
</div>
```

## Utility Classes for Modern Aesthetics

### Spacing
- `space-x-*` and `space-y-*` for consistent spacing between elements
- `divide-x-*` and `divide-y-*` for dividers between elements
- `p-*`, `m-*` using the 8-point grid system

### Shadows
- `shadow-modern` for subtle depth
- `shadow-elevated` for interactive elements
- `shadow-floating` for important elements
- `shadow-mac-window` for special containers

### Animations
- `animate-fade-in` for content appearing
- `animate-slide-up` for dropdowns and modals
- `animate-pulse-slow` for subtle loading indicators

### Responsive Breakpoints
- `sm:` (640px) - Small screens
- `md:` (768px) - Medium screens
- `lg:` (1024px) - Large screens
- `xl:` (1280px) - Extra large screens
- `2xl:` (1536px) - 2x extra large screens

## Typography Utilities

### Headings
- `text-2xl`, `text-3xl`, `text-4xl` for heading sizes
- `font-bold`, `font-semibold` for heading weights
- `leading-tight`, `leading-snug` for line heights

### Body Text
- `text-base`, `text-sm` for body sizes
- `font-normal`, `font-medium` for weights
- `text-neutral-700`, `text-neutral-800` for text colors