# De Leather Craft — Site Audit

_Comprehensive review of the homepage as deployed. Focuses on: section
order/flow, realism, image/brand consistency, mobile-first quality,
copy hygiene, and what is missing vs over-served._

---

## 1. Current section order

1. Header (fixed, transparent over hero)
2. **Hero** — full-screen Promo-2.mp4 video, "Leather Restoration & Repair."
3. **Intro** — "Leather laundry & repair service, near you." + SEO paragraph + city marquee
4. **Services** — 4 photo-led cards (Restore / Clean / Repair / Alter) on dark luxe background
5. **Category grid** — 6 cards (Handbags / Shoes / Jackets / Sneakers / Wallets / Sofas) with blur-hover
6. **Before / After + Process (merged)** — Fendi slider on left, vertical process timeline on right
7. **Brands** — 22-name single-row auto-scrolling marquee
8. **Reviews** — 3 customer testimonials
9. **Atelier (Rishi)** — founder Q&A slider, 5 YouTube Shorts
10. **Sustainability** — "Repair. Re-wear. Repeat."
11. **FAQ** — 6 native `<details>` accordion
12. **CTA banner (dark)** — "Bring it back. Today."
13. **Instagram** — auto-marquee + prev/next slider with 17 real public/ images
14. **Quote / Contact form** — pickup cities + free-estimate form
15. **Footer** — wordmark, contact, social, legal

---

## 2. Flow analysis

### What works
- **Hero → Intro → Services** opens with show (video) → tell (who) → what (services). Classic.
- **Before/After + Process merge** is now ONE coherent story: see the
  result, see the steps. Strong.
- **FAQ → CTA → Instagram → Contact form** end is a clean conversion funnel:
  answer doubts → push action → social proof → form.
- **Atelier (Rishi)** breaks the page mid-scroll with founder presence
  before the closing trust signals (FAQ, contact). Strong.

### Friction / drift in the flow
- **Reviews (8) → Atelier (9) → Sustainability (10) → FAQ (11)** is the
  weakest stretch. Three trust/voice sections back-to-back with no visual
  variation. Reviews + Atelier in particular both lean on customer/founder
  voice and feel repetitive in sequence.
  - **Suggestion**: move **Reviews** up — between Brands and Atelier, so
    Reviews (customer voice) → Atelier (founder voice) reads as a single
    dialogue, then Sustainability cleans the palate with a different topic.
  - Alternative: drop Reviews to 2 cards (currently 3) — already restrained,
    one less tile reduces the lull.
- **Sustainability** sits between Atelier and FAQ. Could move up to
  between Brands and Reviews; it would slot in as a quiet pause before
  the customer/founder voices kick in.

### Section count
15 sections is on the heavy side. Two could plausibly be merged or cut:
- **Sustainability** is short. Could be condensed into a single rotating
  manifesto line in the Intro or near the dark CTA banner.
- **Brands** is currently a thin one-line marquee — the lightest possible
  brand statement. Acceptable. Keep.

---

## 3. Realism / honesty audit

| Item | Status |
|---|---|
| `4.9 / 5 from 2,140 reviews` (fake) | ✅ Removed |
| `24K+ restored` category counters (fake) | ✅ Removed |
| `Vogue / Harper's / ELLE` media badges (fake) | ✅ Removed |
| `Anaïs Dorégan` non-Indian name (off-brand) | ✅ Replaced with Indian names |
| `48 t / 92% / 2027` sustainability stats (fake) | ✅ Removed |
| `carbon-neutral by 2027` claim | ✅ Removed |
| `Four decades / 40+` (incompatible with 2001) | ✅ Removed |
| WhatsApp number — placeholder `9999999999` | ✅ Real number `9560735941` wired |
| Email `hello@deleathercraft.com` (placeholder) | ✅ Real `deleathercraft@gmail.com` wired |
| Real founder content (Rishi) | ✅ All 5 Q&A captions from real video transcripts |
| Real city/address list | ✅ Matches client contact info |

### Still standing — flag these
- **Hero CTA `Get In Touch`** scrolls to `#contact` form. Works ✓
- **2001 vs 2005**: hero/intro/footer say _Since 2001_, but the Rishi
  intro video transcript said _"the journey started in 2005"_. Conflict
  unresolved. Client must confirm the authentic year.
- **Number-of-cities messaging is mixed:**
  - Hero eyebrow + intro lede + quote section: **9 cities** doorstep
  - City marquee: **14 cities** listed
  - Footer pan-India list: **12 cities**
  - Atelier Q·04: _"collection points in cities across India"_ (vague)
  - Probably should pick one canonical number — _12 cities_ is closest to
    real list. _"Free pickup in nine cities"_ contradicts what's actually shown.
- **Reviews testimonials** are still written-style ("looking older, in the
  right way" etc). Pulled from Google reviews would be even more honest;
  current ones are stylised paraphrases.

---

## 4. Mobile-first quality

### Working well
- Hero is **100dvh full-screen**, content vertically centred, dynamic
  viewport (mobile address-bar safe), title clamps elegantly across
  320 / 360 / 390 / 430 viewports.
- Header collapses to hamburger at ≤1200px (raised from 1080 because the
  desktop nav was overflowing). Drawer opens to full-list + opaque header.
- Services cards: photo-led, single column on mobile, stacked with
  generous padding.
- Category grid: 1 column on mobile, blur+text-rise hover (auto-disabled
  on touch devices).
- Before/After: slider full-width on mobile, **process timeline
  stacks vertically below** the slider — no side-by-side cram.
- Brands marquee, IG marquee, City marquee: all motion-friendly on mobile
  (pure CSS / rAF + hover/tap pause).
- Atelier slider: stacked column on mobile, video above text, dot
  navigator instead of the desktop side list.

### Mobile issues
- **Atelier section** desktop has the side question list (3rd col). On
  mobile that column is hidden and dots take over — but the desktop is
  noticeably richer. Mobile feels lighter, almost too light. Could show
  one or two upcoming question titles under the dots on mobile as a
  preview hint.
- **IG marquee buttons** — at mobile width (390 → tile 220px) the prev/next
  44px buttons partially overlap the first/last tile photos. Not broken
  but visually crowded. Either shrink buttons further or fade them out
  on mobile and rely on swipe.
- **City marquee** on tiny phones (≤360px) — uppercase tracked names
  (`AHMEDABAD`, `CHANDIGARH`) get long; diamond-separated row reads ok
  but could be a touch smaller.
- **Hero CTA button** on mobile is fine but the dense letter-spacing
  `0.2em` on the uppercase `GET IN TOUCH` makes touch-targets feel slim
  for chunky thumbs.
- **Quote form** at the bottom — segmented option buttons (Handbag /
  Shoes / Jacket / ...) wrap to 2-3 rows on phones. Functional but the
  wrap is a tight squeeze.

### Mobile recommendations
- Reduce IG marquee buttons to ~36px on mobile (currently 40px,
  defined for `≤520px`). Move them slightly inside or fade them out.
- Add `scroll-margin-top: 80px` to anchor sections so jump links don't
  hide content under the fixed header on mobile.
- Test hero on 320 × 568 (iPhone SE original) — currently the smallest
  breakpoint targets aren't covered.

---

## 5. Image / brand consistency

### Image inventory
- **Hero video**: `Promo-2.mp4` ✓ real client content
- **Before/After**: `before-fendi.jpg` / `after-fendi.jpg` ✓ real Fendi
  Mamma Baguette photos
- **Atelier**: 5 YouTube Shorts ✓ real Rishi videos
- **Instagram marquee**: 17 images in `public/` ✓ all real client work
- **Services cards**: 4 Unsplash images (tools / craft photos) ⚠️
  generic stock, not real DLC atelier
- **Category grid**: 6 Unsplash images (handbag / shoes / etc) ⚠️
  generic stock
- **Sustainability**: 1 Unsplash leather-care image ⚠️ generic stock
- **Footer / header logo**: real client SVG wordmark ✓

### Image issue
The **Instagram marquee + Before/After + hero video** are all real
client work, but the **services / category / sustainability** images
are still Unsplash stock. The visual jump between "real DLC photo" and
"stock photo" is visible if a viewer scrolls slowly. Replacing those
with even one real atelier photo per category would tighten the brand.

### Brand consistency
- Cormorant Garamond serif used in: hero title, section titles, brand
  marquee, atelier text, story captions, Instagram captions, FAQ
  questions, city marquee. Consistent.
- Inter Tight used in: nav, body, mono labels. Consistent.
- Cognac accent: hero CTA, eyebrow text, accent dots in marquees,
  underline reveals, founder slider active dot. Consistent.
- Logo SVG: header + footer use the same wordmark with state-driven
  fills (light over hero, dark over scroll, etc). Consistent.

---

## 6. Copy hygiene

### What's tight
- Hero: 4 words title, 3-word sub, 1 CTA. Restrained.
- Intro lede: 1 short paragraph, no adjective stew.
- Services: numbered prefix + serif title + 5-bullet list. No
  descriptor paragraphs.
- Before/After story: "By hand. Four weeks." — minimal.
- Atelier captions: real founder quotes condensed to 1-2 sentences.
- FAQ answers: factual, ~2-3 sentences each.

### What still bloats
- **`<title>` tag**: _"De Leather Craft — Premium Leather Repair,
  Cleaning & Restoration"_ — still has _Premium_. Meta description also
  has _Premium_ + _luxury_. These are SEO keywords (intentional). Keep,
  but flag.
- **Logo SVG tagline**: `luxury care for your luxury leather...` —
  baked into the logo image, can't strip without editing the SVG.
  Says _luxury_ twice. Could be edited to e.g.
  _"by-hand care for your leather goods..."_
- **Sustainability lede**: _"Every piece we restore is a piece that stays
  out of landfill."_ — single line, good but feels orphaned without the
  removed stats. Either lean it into 2-3 short lines or merge with
  another section.

---

## 7. Header nav — 67 placeholder `href="#"` links

The desktop nav and mobile drawer have **67 placeholder links** going
to `#`. Most are unbuilt routes (Home / About / Blog / Products /
We Service ▾ / Restoration / Cleaning / Repair / Alteration / sub-items …
Sneakers / Trolley / Sofas / Testimonials / Terms / Contact …).

This is the biggest unfinished thing on the homepage. Either:

1. **Trim the nav** to the routes that actually exist (currently:
   `#services`, `#categories`, `#before-after`, `#brands`, `#reviews`,
   `#atelier`, `#faq`, `#contact`, `#locations`). Most should be
   anchor-scroll links into existing sections, not multi-page routes.
2. **Build the missing pages.** That's a bigger project. For a single
   homepage launch, option 1 is the right call.

Recommended single-page nav:
- _What we do_ → `#services`
- _What we restore_ → `#categories`
- _The transformation_ → `#before-after`
- _Brands_ → `#brands`
- _From the atelier_ → `#atelier`
- _FAQ_ → `#faq`
- _Contact_ → `#contact`

Mobile drawer same list — 7 items, all working.

---

## 8. Design — visual rhythm

- Section background rhythm (cream → cream → dark → cream → cream → dark
  → cream …): generally good. The dark Services + dark Process →
  merged-into Before/After … wait, Process is dark in old layout, but
  the merged Before/After is cream. So the merged section lost the dark
  "process" beat. The page now goes:
  - Hero (dark video) → Intro (cream) → Services (**dark**) →
    Categories (cream) → Before/After+Process (**cream**) → Brands (cream)
    → Reviews (paper) → Atelier (cream-2) → Sustainability (rose) →
    FAQ (paper) → CTA dark → IG cream → Form cream → Footer dark.
  - **The middle stretch (Categories → Before/After → Brands → Reviews
    → Atelier) is all cream-ish.** Five cream sections in a row.
- **Suggestion**: paint the **Brands** marquee section dark (ink with
  the brand names in cream/cognac) — instant rhythm break, gives the
  brand strip more presence, and breaks the long cream stretch.

### Typography
- Cormorant Garamond at 5+ different sizes (hero / section-title /
  card title / lede / quote-form title etc). Consistent feel.
- Inter Tight at body 16 / mono 10-13 / nav 12. Restrained scale.

### Spacing
- Section padding `120 → 144` (Phase 3) gave breathing room. Now
  consistent across sections.

---

## 9. Performance + tech

### What's right
- All images use `loading="lazy"` except the hero video poster.
- Single CSS file, single inline `<script>`, no framework, no build.
- `vercel.json` caches assets 7 days immutable.
- Real responsive `dvh` for mobile viewports.

### What could be improved
- **No `prefers-reduced-motion`** on the IG rAF auto-scroll. Brand
  marquee and city marquee respect it; IG marquee does not. Should
  pause auto-scroll for those users.
- **Hero video** auto-plays muted — no `preload="metadata"` thrift; loads
  the whole 4.2MB on first paint. For mobile data plans, consider
  `preload="none"` + a poster image fallback, then start on `loadeddata`.
- **Atelier YouTube iframes** all lazy-loaded; only 1 plays at a time
  via the slider mechanism. Good.

---

## 10. Excesses to consider trimming

- **2 CTA banners** were already cut to 1 (dark). Good.
- **3 separate marquees** on the page (city / brands / IG) is a lot.
  Consider: city marquee + IG marquee both feature horizontal scroll.
  Could the city marquee become a static line ("Mumbai · Delhi · …")
  to reduce motion repetition? Brands already feels different (italic
  serif), city + IG feel similar in cadence.
- **Sustainability section** is short and sits between dense sections —
  could be folded into Atelier or Intro as a one-line manifesto.

---

## 11. Deficiencies — what's missing

- **No real "About" page link** — the founder story is reduced to the
  Atelier slider. Could merit a longer story page eventually.
- **Pricing transparency** — FAQ says "every estimate hand-priced" but
  no ballpark. A "starting from ₹X" indicator on services or a sample
  price table for the most common items (shoe re-sole, handbag re-dye)
  would reduce friction.
- **Trust badges that are real** — Google Reviews count (live), or a
  link to the GMB profile, would be stronger than the (removed) fake
  star rating.
- **Service guarantee wording** — only mentioned in FAQ. Could be a
  one-line manifesto somewhere visible: _"6-month workmanship warranty
  on every restoration."_
- **Schema.org JSON-LD** (LocalBusiness, FAQ, Service) — discussed
  earlier; not yet added. Would meaningfully improve search/AI visibility.
- **No `og:image` / Twitter card** — site shares as a blank rectangle
  on WhatsApp / LinkedIn / Twitter. Earlier audit flagged this; still
  not added.
- **Sitemap.xml / robots.txt** — missing.
- **Header anchor scroll** doesn't account for fixed header (72px).
  Add `html { scroll-padding-top: 80px; }` so anchor jumps land below
  the header.

---

## 12. Priority punch list (top 10)

In recommended order:

1. **Reconcile 2001 vs 2005** — confirm authentic year, fix everywhere.
2. **Pick one canonical city count** (e.g. "12 cities") and propagate.
3. **Replace 67 placeholder `href="#"` links** with real anchor links
   or trim the nav to what works.
4. **Add `og:image`, Twitter card, canonical URL, sitemap.xml, robots.txt**.
5. **Add JSON-LD schema** (Organization + LocalBusiness + FAQ + Service).
6. **Move Reviews up to between Brands and Atelier** (flow tightener).
7. **Paint Brands marquee dark** (visual rhythm break).
8. **Replace at least 1 stock image per section** (services + categories +
   sustainability) with real DLC atelier photos.
9. **Add `prefers-reduced-motion` guard** to IG rAF marquee.
10. **Strip _luxury_ from logo SVG tagline** OR keep it but make sure no
    other section adds another _luxury_ on top of it.

---

## Summary

The site has come a long way from the original template. The big
foundations are right: real client content (videos, photos, address,
contact), restrained copy, mobile-first hero, motion-rich brand strip,
honest sustainability, founder slider with real Rishi quotes, real
Instagram photos in an interactive slider.

What's left is mostly **last-mile polish**: nav links that go nowhere,
two stats (2001 vs 2005 and "9 vs 12 cities") that contradict each
other, a long cream-on-cream visual stretch in the middle that wants
one dark beat, and the absence of social-share metadata / structured
data which keeps AI visibility lower than it should be.

Nothing in the current site is broken or off-brand. The recommendations
above are tightening moves, not rebuilds.
