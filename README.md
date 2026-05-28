# De Leather Craft — Luxury Leather Restoration Website

A premium, modern, and mobile-first single-page web experience for **De Leather Craft** — an independent luxury leather restoration, cleaning, and repair atelier founded in Mumbai since 2005.

This project is built using semantic HTML5, Vanilla CSS, and modern JavaScript, designed with a focus on luxury aesthetics (featuring curated color palettes, elegant typography, before/after visual storytelling, and micro-interactions). It is fully optimized for performance, accessibility, SEO, and structured data, and is designed to plug smoothly into a React/Next.js setup.

---

## 🌟 Key Features

- **Luxury Visual Identity**: Bespoke color palettes (warm charcoal `#221610`, cognac `#a46839`, paper `#f7f4f0`) and typography (`Cormorant Garamond` serif and `Inter Tight` sans-serif).
- **Responsive & Mobile-First**: Built from the ground up to offer an exceptional UX on mobile devices, tablets, and desktops.
- **Before/After Slider**: Interactive visual storytelling components that let users drag to reveal the transformation of premium leather items.
- **SEO & Structure Optimized**: Ships with complete JSON-LD structured schemas (`Organization`, `LocalBusiness`, `Service`, `BreadcrumbList`, and `FAQPage`) to maximize search engine discoverability.
- **Atelier Video Showcase**: Fluid infinite loop video headers and image layouts representing the craftsmanship.
- **Vercel Ready**: Pre-configured `vercel.json` with clean URL routing and asset caching configurations.

---

## 📂 Project Structure

```
delivery/
├── public/                 # Static assets (images, logos, videos)
│   ├── before-after/       # Transformation comparison images (Fendi, etc.)
│   ├── branding/           # SVG and raster logo versions
│   ├── services-photos/    # High-quality service landing images
│   └── video/              # Promo videos
├── services/
│   ├── service-template/
│   │   └── index.html      # Service Detail MASTER TEMPLATE ({{placeholder}} tokens)
│   ├── leather-bag-restoration/
│   │   └── index.html      # Example service page (template filled with real data)
│   └── generate_example.py # Helper: fills the master template into a service page
├── index.html              # Main Landing page / Home
├── style.css               # Core design system and main styles
├── service.css             # Service detail page-specific styles
├── sitemap.xml             # Search engine sitemap
├── robots.txt              # Crawler instructions
└── vercel.json             # Vercel deployment configuration
```

---

## 🛠️ Tech Stack

- **Core**: Semantic HTML5, Vanilla CSS3 (CSS Variables, Flexbox, CSS Grid)
- **Logic**: Vanilla ES6+ JavaScript (Intersection Observer API for transparent headers, custom slider logic, mobile drawer navigation)
- **Deployment**: Optimized for Vercel (Supports clean URLs `/services/leather-bag-restoration`)

---

## 🚀 Development & Deployment

### Run Locally
Simply open `index.html` in any browser or run a local server:
```bash
# Using Python
python -m http.server 8000

# Using Node (live-server or serve)
npx serve .
```

### Deploy to Vercel
You can deploy this repository directly to Vercel. The `vercel.json` configuration will automatically configure clean URL paths (e.g., `/services/leather-bag-restoration` instead of `/services/leather-bag-restoration/index.html`).

---

## 📐 Next.js Integration Plan

The service template (`services/service-template/index.html`) contains detailed comments outlining a 1:1 integration path into a Next.js setup:
- **Route**: `app/services/[slug]/page.tsx`
- **TypeScript Data Model**: Outlined inside the template for easy data schema modeling.
- **Component Map**: 1:1 component breakdown (`<Header />`, `<ServiceHero />`, `<Transformation />`, etc.).
