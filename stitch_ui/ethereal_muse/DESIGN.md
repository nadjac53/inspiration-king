# Design System Document: The Ethereal Atelier

## 1. Overview & Creative North Star
This design system is built upon the North Star of **"The Ethereal Atelier."** 

Inspiration is not a rigid, linear process; it is fluid, translucent, and layered. To reflect this, we are moving away from the "industrial" look of standard apps and toward a high-end editorial experience. We achieve this through **intentional asymmetry**, where elements overlap to create depth, and a **high-contrast typography scale** that demands attention. The goal is to make the user feel as though they are navigating a curated digital gallery rather than a database.

The interface breathes. It uses "White Space" as a functional component, not just a gap. By utilizing glassmorphism and soft tonal shifts, we create a sense of "Creative Energy" that feels both premium and boundless.

---

## 2. Colors & Surface Logic

### The Palette
We utilize a sophisticated earth-toned foundation punctuated by a sharp, creative teal.
- **Primary (`#8c4b22`):** Representing the "King" aspect—grounded, authoritative, and warm.
- **Secondary (`#7a5643`):** Used for supporting elements and subtle brand presence.
- **Tertiary (`#00696c`):** The "Spark." Used sparingly for highlights, secondary CTAs, or success states to inject "Creative Energy."
- **Background Gradient:** A soft transition from `surface_container_low` (`#fff1eb`) to `surface_container_lowest` (`#ffffff`) to create a natural horizon line.

### The "No-Line" Rule
**Strict Mandate:** 1px solid borders for sectioning are prohibited. 
Structure must be defined through:
1.  **Tonal Shifts:** Placing a `surface_container_high` card on a `surface` background.
2.  **Shadow Depth:** Using ambient shadows to define boundaries.
3.  **Negative Space:** Using the Spacing Scale to separate ideas.

### Surface Hierarchy & Nesting
Treat the UI as a series of physical layers.
- **Level 0 (Base):** `surface` or the background gradient.
- **Level 1 (Sections):** `surface_container_low`.
- **Level 2 (Cards/Interactive):** `surface_container_lowest` or Glassmorphism containers.
- **Level 3 (Pop-overs):** `surface_bright` with high blur shadows.

---

## 3. Typography: Editorial Authority

The typography strategy relies on the tension between the expressive **Plus Jakarta Sans** and the functional **Inter**.

- **Display & Headlines (Plus Jakarta Sans):** These are the "Voice" of the system. Use `display-lg` and `headline-lg` with Bold weights to create an editorial feel. Do not be afraid to let headlines overlap slightly with background elements or glass cards.
- **Body & Labels (Inter):** These are the "Function." Keep body text in `body-md` for legibility. Use `label-sm` for metadata, ensuring high contrast using `on_surface_variant`.
- **Hierarchy of Inspiration:** Titles should always be significantly larger than expected (e.g., 2.5x the size of body text) to guide the eye through the "Creative Energy" of the page.

---

## 4. Elevation & Depth

### The Glassmorphism Standard
To achieve a "Translucent Modernity," main UI containers should follow these specs:
- **Fill:** `rgba(255, 255, 255, 0.7)`
- **Backdrop Blur:** 10px
- **Radius:** `lg` (2rem / 32px) for large cards; `md` (1.5rem / 24px) for standard components.
- **Ghost Border:** Use `outline_variant` at **15% opacity** only if the container sits on a busy background.

### Ambient Shadows
Avoid "dirty" grey shadows. 
- **Value:** Y=6, Blur=15.
- **Color:** Use `on_surface` at **8% opacity**. This ensures the shadow feels like a natural obstruction of light within the warm environment of the app.

---

## 5. Components

### 5.1 Buttons
- **Primary:** Filled with `primary` (`#8c4b22`). Text in `on_primary`. Shape: `full` (pill-shaped). Use a subtle gradient transition to `primary_container` for a "lit from within" effect.
- **Secondary (The Glass Button):** Glassmorphism fill (blur 10px) with a `primary` text color. No border.
- **Tertiary:** Text-only using `tertiary` color, with a slight weight increase to Bold.

### 5.2 Cards & Lists
- **The "No Divider" Rule:** Never use lines to separate list items. Use 16px to 24px of vertical space (Spacing Scale `md` to `lg`) or alternate background tints between `surface_container_low` and `surface_container_highest`.
- **Interactive Cards:** On hover/tap, cards should "lift" by increasing the shadow blur and decreasing the `backdrop-blur` slightly to make the content feel "closer" to the user.

### 5.3 Input Fields
- **Style:** Background `surface_container_high`, `xl` (3rem) corner radius. 
- **States:** Active state should not use a high-contrast border; instead, use a 2px "Ghost Border" of `primary` at 40% opacity.

### 5.4 Signature Elements: Atmospheric Icons
To reinforce the "Inspiration King" identity, use faint floating icons (✨, 💡).
- **Opacity:** Fixed at 6%.
- **Placement:** Asymmetric, partially "tucked" behind glass containers or bleeding off the edge of the viewport. This creates a sense of an environment that extends beyond the screen.

---

## 6. Do’s and Don’ts

### Do:
- **Do** use intentional white space. If you think a section needs more room, double the padding.
- **Do** overlap elements. Let a glass card sit 20px over a headline to create depth.
- **Do** use the `tertiary` teal for moments of "Delight" (e.g., a successful inspiration save).

### Don’t:
- **Don’t** use 100% black (`#000000`). Always use `on_surface` or `on_background` for text to maintain the warm, premium tone.
- **Don’t** use standard 4px or 8px radiuses. This system requires "Softness"—stick to the `md`, `lg`, and `xl` roundedness scale.
- **Don’t** center-align everything. Modern editorial design thrives on left-aligned headlines with right-aligned or floating supporting imagery.

---

## 7. Interaction Design
Every transition must feel "weightless." When a glass card appears, it should fade in while scaling from 98% to 100%, mimicking the way a lens focuses. This reinforces the "Lucid" nature of the design system.