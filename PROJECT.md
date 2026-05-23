# De Leather Craft — Homepage Rebuild

## Project Overview

A complete redesign of the **De Leather Craft** homepage — a premium leather
restoration and repair service based in India. The goal: replace the existing
site with a modern, luxury-brand-feeling single page that converts visitors
into free-estimate enquiries.

The deliverable is a self-contained static site: one HTML file, one
stylesheet, one inline script, plus media assets. No build step, no
framework, no runtime dependencies — ready to drop on any static host.

---

## Client & References

| Role | Link |
|------|------|
| Client business | **De Leather Craft** |
| Client Instagram | <https://www.instagram.com/deleathercraft> |
| Client's current live site | _to fill in by client — likely deleathercraft.com_ |
| Reference / inspiration site (what the client wants to look like) | <https://www.theleatherlaundry.com> |

The client explicitly pointed at **theleatherlaundry.com** as the visual /
editorial direction they admire: video hero, elegant brand-name wordmark in
the header, clean luxury-jewellery typography, big before/after proof,
trusted-brand strip.

---

## Tech Stack

Deliberately minimal — picked so any developer (or the client themselves)
can edit it without tooling.

- **HTML5** — semantic single page (`delivery/index.html`)
- **CSS3** — handwritten, mobile-first, custom-properties for theming
  (`delivery/style.css`)
- **Vanilla JavaScript** — inline `<script>` block at end of `index.html`
  (mobile nav, before/after slider drag, header scroll-state observer,
  hero video keep-alive)
- **Google Fonts** — Cormorant Garamond (display serif) + Inter Tight (sans)
- **Static assets** — `Promo-2.mp4` (hero video), `before-bag.jpg`
  (before/after worn photo)
- **No framework, no bundler, no package.json.** Just open `index.html`.

### Deployment

- **Repo:** <https://github.com/goktugzaaa/leather-draft>
- **Host (planned):** Vercel — Framework Preset _Other_, no build command,
  root = repo root.

---

## What the Client Wanted

1. Full-screen video hero with a short, luxury-brand-style headline.
2. A header that sits transparent over the hero and only turns solid when
   the user scrolls past — like a real luxury site, not a generic web app.
3. Logo wordmark in a refined serif (jewellery-house feeling), not the
   default bold sans-serif.
4. A real, hero-scale **Before / After** comparison with a draggable
   handle — using a real worn-piece photo, not a desaturated/filtered
   fake.
5. Mobile-first: every breakpoint between 320 px (small Android) and 430 px
   (Pro Max) has to feel _designed_, not just shrunk.
6. SEO content woven into the page naturally — keywords like _"leather
   laundry near me"_, _"luxury handbag restoration"_, _"trusted leather
   care specialists"_ + the names of the luxury houses they service.
7. No fake numbers ("4.9 / 5 from 2,140 reviews"), no fake media badges
   ("As featured in Vogue") — just honest, defensible social proof.

---

## UI / Page Architecture (what we shipped)

Single-page, top-to-bottom narrative:

1. **Fixed-overlay header**
   - Transparent over the hero, scroll past hero → solid cream with backdrop
     blur. Smooth `0.35s` transition.
   - Logo: serif **Cormorant Garamond** wordmark — jewellery-house weight.
   - Desktop nav full edge-to-edge, CTA flush right.
   - `≤1200 px`: nav collapses to hamburger drawer. (Old breakpoint of
     1080 px was too tight for the long nav and left it overflowing on
     small laptops — raised to 1200.)
   - Mobile drawer open ⇒ header forced opaque so cream drawer doesn't
     clash with transparent header.

2. **Hero (video)**
   - Full-bleed background `Promo-2.mp4`, `object-fit: cover`, `100dvh`
     height (full screen on every device, dynamic viewport for mobile
     address bars).
   - Mobile / tablet: content **vertically centred** — balanced, never
     glued to the bottom edge.
   - Desktop (≥1024 px): content anchored bottom-left, editorial style.
   - Headline: `Luxury Leather Restoration Experts` (italic _Experts_).
   - Subtext minimal: `By master hands. Since 2001.`
   - CTA: **Get In Touch** — `.btn--hero.btn--hero-xl` — outlined,
     uppercase, wide letter-spacing, sweeping cream fill on hover.

3. **Intro / "Who we are"**
   - Adapted from the client's real website copy.
   - Headline: _"Leather laundry & repair service, near you."_ (SEO).
   - Body lede: who they are + what they restore.
   - Bottom of the section: **SEO paragraph** mentioning trusted-specialist
     phrasing + luxury brand names (Louis Vuitton, Hermès, Chanel, Gucci,
     Dior, Bottega Veneta, Prada, Saint Laurent) + "leather laundry near
     me" / "mobile leather furniture repair near me" search phrases.
   - Followed by an **infinite scrolling city marquee** — 13 pickup cities
     in Cormorant italic, copper-dot separators, fade mask at edges,
     hover-pauses, `prefers-reduced-motion` respected, listed twice in DOM
     for a seamless loop.

4. **Services (4 columns)** — Restoration / Cleaning / Repair / Alteration.

5. **Category grid** — Handbags, Shoes, Jackets, Sneakers, Wallets &
   Belts, Sofas & Upholstery. Fake "24K+ restored" counters removed.

6. **Before / After — feature section** (replaces the old weak
   "Complete index" service-list dump)
   - Full-width 16/10 slider on desktop, 4/5 (vertical) on mobile.
   - Real worn-bag photo as the "before" (`before-bag.jpg`) — no CSS
     desaturation, no fake SVG scratches.
   - Draggable handle, "Before" / "After" tags.
   - Story panel below: **Salvatore Ferragamo Boxyz**, 12 years carried
     daily, master-technician narrative + cognac _Get free quote_ CTA.

7. **Process (4 steps, dark)** — WhatsApp → free pickup → hand-restoration
   → returned with care + 6-month warranty.

8. **CTA banner (cream)** — _Bring it back. Today._

9. **Our promise** — 4 cards (doorstep pickup, ethical materials, tailored
   service, 6-month workmanship warranty).

10. **Brands we restore** — 22 luxury houses, full-bleed grid edge-to-edge,
    elegant cognac hover (text turns cognac, hairline cognac underline
    scales in from centre). Disabled on `@media (hover: none)` so touch
    devices don't get stuck in the hover state.

11. **Reviews** — 3 honest testimonials with Indian names (Priya Nair,
    Vikram Suri, Rahul Mehta). Fake "4.9 / 5 from 2,140 reviews" replaced
    with _"Trusted by customers across India."_

12. **Social proof (video)** — featured customer-story videos.

13. **Sustainability** — repair / re-wear / repeat narrative + stats.

14. **FAQ** (newly added) — 6 native `<details>` accordion items (how long
    restoration takes, non-luxury brands, free pickup, cities, cost,
    workmanship warranty). Animated `+ → ×` icon, cognac hover. SEO-relevant.

15. **CTA banner (dark)** — second push to action.

16. **Instagram strip** — 6 tiles linking out to
    [@deleathercraft](https://www.instagram.com/deleathercraft).

17. **Quote / Contact** — left: 9 pickup cities; right: sticky free-estimate
    form (item type, service type, city, name, phone, optional message).

18. **Footer** — brand info, services, categories, company, WhatsApp + email,
    pan-India city list, legal links. Real WhatsApp number wired:
    **+91 95607 35941** ⇒ `wa.me/919560735941`.

---

## What We Killed (because it was either fake or weak)

- "4.9 / 5 from 2,140 reviews" + 5-star bar.
- All "24K+ / 18K+ / 11K+ restored" category counters.
- "Anaïs Dorégan" testimonial (didn't fit an Indian leather atelier).
- "As featured in Vogue / Harper's Bazaar / ELLE" media strip (unverifiable).
- The whole **Complete Index** service-list dump — replaced by the
  before/after feature section.
- The static image hero (kept commented out in source for rollback).
- The old multi-case before/after picker — collapsed to one focused case.

---

## Design / Brand Tokens

| Token | Value | Use |
|-------|-------|-----|
| `--bg` | `#f7efe1` | Page background |
| `--bg-2` | `#efe3cd` | Section alternate |
| `--paper` | `#fdf8eb` | Cards / panels |
| `--ink` | `#221610` | Primary text / dark surfaces |
| `--ink-2` | `#5a4536` | Secondary text |
| `--muted` | `#8a7560` | Captions |
| `--line` | `#e2d4b8` | Hairlines |
| `--cognac` | `#a8623a` | Primary brand accent |
| `--cognac-2` | `#8a4d2c` | Cognac shadow / pressed |
| `--copper` | `#c97a4a` | Highlight |
| `--rose` | `#e6c2b3` | Secondary accent (used sparingly) |

Type: **Cormorant Garamond** for headings, hero title, brand wordmark and
the logo. **Inter Tight** for body, nav and form fields.

---

## File Layout

```
delivery/
├─ index.html        # single-page markup + inline JS
├─ style.css         # all styles, organised in numbered sections
├─ Promo-2.mp4       # hero background video
├─ before-bag.jpg    # before/after worn photo (Salvatore Ferragamo Boxyz)
├─ .gitignore
└─ PROJECT.md        # this file
```

---

## Where to Edit What

- **Hero copy / CTA text** → `index.html`, search `class="hero-video__title"`.
- **Intro headline, lede, SEO paragraph** → `index.html`, search `class="intro"`.
- **City marquee list** → `index.html`, search `class="city-marquee__track"`.
- **Before / After story** → `index.html`, search `class="ba-story"`.
- **FAQ questions / answers** → `index.html`, search `class="faq-list"`.
- **WhatsApp number** → `index.html`, search `wa.me/919560735941`.
- **Brand tokens / colours** → `style.css` section _01. Design tokens_.
- **Header behaviour (transparency / scroll state)** → `index.html`, inline
  script section _5. Transparent header_.

---

## Open Items / Things the Client Still Needs to Decide

- Replace placeholder customer-story YouTube embeds with real
  De Leather Craft reels (or self-hosted MP4s — `delivery/`).
- Decide if the "Since 2001" copy stays — some legacy copy still references
  _"four decades"_ — that copy lives in commented-out original hero and in
  the intro note; if Since 2001 is the line, the "four decades" claim is
  wrong and should be removed wherever it surfaces.
- Real product photography for category cards (currently Unsplash) and the
  before/after _after_ photo (currently an Unsplash bag image).
- Sustainability stats (48 t / 92 % / 2027) — verify or replace.
