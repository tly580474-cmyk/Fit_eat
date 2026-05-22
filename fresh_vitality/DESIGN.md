---
name: Fresh & Vitality
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f3'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#3f4a3c'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#6f7a6b'
  outline-variant: '#becab9'
  surface-tint: '#006e1c'
  primary: '#006e1c'
  on-primary: '#ffffff'
  primary-container: '#4caf50'
  on-primary-container: '#003c0b'
  inverse-primary: '#78dc77'
  secondary: '#8b5000'
  on-secondary: '#ffffff'
  secondary-container: '#ff9800'
  on-secondary-container: '#653900'
  tertiary: '#556158'
  on-tertiary: '#ffffff'
  tertiary-container: '#929e94'
  on-tertiary-container: '#2a352d'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#94f990'
  primary-fixed-dim: '#78dc77'
  on-primary-fixed: '#002204'
  on-primary-fixed-variant: '#005313'
  secondary-fixed: '#ffdcbe'
  secondary-fixed-dim: '#ffb870'
  on-secondary-fixed: '#2c1600'
  on-secondary-fixed-variant: '#693c00'
  tertiary-fixed: '#d9e6da'
  tertiary-fixed-dim: '#bdcabe'
  on-tertiary-fixed: '#131e17'
  on-tertiary-fixed-variant: '#3e4a41'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 30px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.5px
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
  headline-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
  headline-lg-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 26px
    fontWeight: '700'
    lineHeight: 34px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  container-margin: 1.25rem
  gutter-base: 1rem
  stack-sm: 0.5rem
  stack-md: 1rem
  stack-lg: 1.5rem
  card-padding: 1rem
---

## Brand & Style

The design system is centered on a "Fresh & Vitality" narrative, specifically tailored for health-conscious users seeking clarity and motivation in their wellness journey. The personality is approachable, optimistic, and clean, bridging the gap between a clinical nutrition tool and a vibrant lifestyle magazine.

The aesthetic blends **Modern Minimalism** with **Soft Tactile** elements. It prioritizes high-quality food photography and generous whitespace to reduce cognitive load during meal planning. The emotional response should be one of "effortless health"—where tracking feels like a natural extension of a balanced life rather than a chore. Visual weight is carried by cards and vibrant data visualizations, ensuring that Chinese typography remains legible and prominent within the interface.

## Colors

The palette is rooted in nature and energy. 
- **Primary Green (#4CAF50):** Represents growth, health, and fresh ingredients. Used for primary actions, progress indicators, and "success" states.
- **Secondary Orange (#FF9800):** Symbolizes metabolic energy and appetite. Used sparingly for highlights, warnings, or "active" states like workout buttons to provide a warm contrast to the green.
- **Neutral Cream (#FAFAFA):** The primary background color. It provides a softer, more organic feel than pure white, reducing eye strain during night-time meal logging.
- **Tertiary Mint (#E8F5E9):** Used for large surface areas like card backgrounds or chip containers to create a layered, "tonal" look without high contrast.

## Typography

This design system utilizes **Plus Jakarta Sans** for its friendly, rounded terminals which complement the soft UI shapes. For Chinese characters, the system defaults to high-quality system sans-serif fonts (PingFang SC or Noto Sans SC) to maintain maximum legibility at all weights.

Typography is treated with a clear hierarchy:
- **Headlines:** Bold and expressive, used for recipe names and daily summaries.
- **Body:** Ample line height (1.5x) is applied to Chinese text to prevent density issues, ensuring that ingredient lists and instructions are easy to scan while cooking.
- **Data Labels:** Used for nutritional facts (calories, macros); these often use a slightly heavier weight to ensure numbers stand out.

## Layout & Spacing

The design system follows a **Mobile-First Fixed-Fluid** hybrid model. On mobile, it uses a 1.25rem (20px) side margin to provide breathing room for the card-based layout. 

Layout logic:
- **Vertical Rhythm:** Content follows a strict 4px/8px baseline grid to keep elements aligned.
- **Card Spacing:** Elements within cards use a 1rem (16px) gutter.
- **Sectioning:** Distinct blocks of content (e.g., "Breakfast" vs "Lunch") are separated by 1.5rem (24px) to indicate clear transitions in the daily timeline.
- **Safe Areas:** Bottom navigation and floating action buttons (FAB) for "Log Food" must account for device-specific home indicators.

## Elevation & Depth

Depth in the design system is achieved through **Tonal Layering** and **Ambient Shadows**. Instead of harsh black shadows, this system uses "soft-focus" shadows tinted with the primary color to maintain a "fresh" appearance.

- **Level 0 (Background):** The soft cream (#FAFAFA) base.
- **Level 1 (Cards):** Elevated via a subtle 10% opacity primary-green shadow (0px 4px 20px) to make recipe cards feel "lifted" from the background.
- **Level 2 (Interactive):** Floating buttons or active selection states use a more pronounced shadow to invite interaction.
- **Overlays:** Use a 40% backdrop blur (Glassmorphism effect) for modal backgrounds to maintain context while focusing the user on a specific task, like adding an ingredient.

## Shapes

The shape language is overtly **Rounded and Organic**.
- **Standard Cards:** Use a 1rem (16px) corner radius to evoke a friendly, modern feel.
- **Feature Cards:** Large hero cards (e.g., "Daily Goal") can go up to 1.5rem (24px) to soften the visual impact.
- **Buttons & Chips:** Follow a "Semi-Pill" style with a minimum of 0.5rem (8px) radius, ensuring they feel tactile and "squishy" without being fully circular unless they are icon-only FABs.
- **Images:** Food photography should always have rounded corners matching the container card to maintain a cohesive, integrated look.

## Components

- **Recipe Cards:** Full-width images with a text overlay at the bottom. Use a subtle dark-to-transparent gradient behind text to ensure legibility over bright food photos.
- **Nutritional Gauges:** Use circular progress bars for Macros (Protein, Carbs, Fats) with high-contrast colors against the primary cream background.
- **Buttons:**
  - *Primary:* Solid #4CAF50 with white text, 16px corner radius.
  - *Secondary:* Outlined #4CAF50 or solid #FF9800 for "Burn" or "Energy" actions.
- **Input Fields:** Clean, minimal fields with a 1px border that thickens and changes to Green on focus. Labels should remain visible above the input.
- **Timeline Lists:** Used for daily weight tracking or food logs. Use a vertical "stem" with dot indicators to show progress through the day.
- **Chips:** Small, rounded indicators for dietary tags (e.g., "Vegan," "High Protein"). Use the tertiary green background with primary green text.