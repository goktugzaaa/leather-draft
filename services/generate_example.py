import os
import re

template_path = r"c:\Users\goktu\Desktop\client homepage-claude\delivery\services\service-template\index.html"
output_dir = r"c:\Users\goktu\Desktop\client homepage-claude\delivery\services\leather-bag-restoration"
output_path = os.path.join(output_dir, "index.html")

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Define replacements for Leather Bag Restoration
replacements = {
    # SEO / Metadata
    "{{SERVICE_TITLE}}": "Designer Leather Bag Restoration & Repair",
    "{{SERVICE_META_DESCRIPTION}}": "Expert leather handbag restoration and repair since 2005. Hand-detailed deep cleaning, custom color-matching, stitch repair, and lining replacement for Chanel, Hermès, Gucci, and Louis Vuitton.",
    "{{SERVICE_SLUG}}": "leather-bag-restoration",
    "{{SOCIAL_SHARE_IMAGE}}": "/public/before-after/after-fendi.jpg",
    "{{HERO_IMAGE_PATH}}": "https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=1600&q=80&auto=format&fit=crop",
    
    # Hero Section
    "{{SERVICE_NAME}}": "Leather Bag Restoration",
    "{{SERVICE_TAGLINE}}": "for designer handbags worth preserving.",
    "{{SERVICE_HERO_SUB}}": "Restore the structure, color, and finish of your heirloom designer pieces. Our expert artisans provide custom hand-detailing, stitching, and color-matching for Hermès, Chanel, Louis Vuitton, and luxury leather goods.",
    
    # Problem Section ("Common Issues We Fix")
    "{{PROBLEM_1_TITLE}}": "Scuffs & Abrasions",
    "{{PROBLEM_1_DESC}}": "Friction along base corners, piping, and edges strips color pigments and degrades delicate lambskin or calfskin.",
    "{{PROBLEM_2_TITLE}}": "Deep Surface Stains",
    "{{PROBLEM_2_DESC}}": "Ink spills, dye transfers from denim, watermarks, makeup, and oils penetrate raw leather grain causing permanent discoloration.",
    "{{PROBLEM_3_TITLE}}": "Color Fading",
    "{{PROBLEM_3_DESC}}": "Continuous exposure to UV rays and hand oils bleaches out original brand-specific pigments and dries out texture.",
    "{{PROBLEM_4_TITLE}}": "Torn Stitching & Piping",
    "{{PROBLEM_4_DESC}}": "Heavy load carrying pulls stress points loose, tearing seams, handles, strap loops, and exposing plastic piping cords.",
    "{{PROBLEM_5_TITLE}}": "Hardware Tarnish & Scratches",
    "{{PROBLEM_5_DESC}}": "Bespoke gold or silver brand hardware undergoes oxidizing, dulling, micro-scratching, or complete clasp failure.",
    "{{PROBLEM_6_TITLE}}": "Lining Tears & Odors",
    "{{PROBLEM_6_DESC}}": "Interior silk, suede, or canvas linings gather dirt, ink marks, structural tears, or mold odors over years of storage.",

    # Before / After Gallery (3 items)
    "{{BEFORE_AFTER_1_TAB}}": "Chanel Flap",
    "{{BEFORE_AFTER_2_TAB}}": "LV Speedy",
    "{{BEFORE_AFTER_3_TAB}}": "Hermès Birkin",
    "{{BEFORE_AFTER_1_BEFORE}}": "https://images.unsplash.com/photo-1598033129183-c4f50c736f10?w=900&q=80&auto=format&fit=crop",
    "{{BEFORE_AFTER_1_AFTER}}": "https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=900&q=80&auto=format&fit=crop",
    "{{BEFORE_AFTER_1_NAME}}": "Chanel Classic Flap",
    "{{BEFORE_AFTER_1_META}}": "Lambskin · Color Revival & Scuff Repair",
    "{{BEFORE_AFTER_1_BULLET_1}}": "Precision pigment match for deep black lacquer finish",
    "{{BEFORE_AFTER_1_BULLET_2}}": "Corner leather rebuild and structural reinforcement",
    "{{BEFORE_AFTER_1_BULLET_3}}": "24k gold plated CC turnlock polish & tarnish removal",
    
    "{{BEFORE_AFTER_2_BEFORE}}": "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?w=900&q=80&auto=format&fit=crop",
    "{{BEFORE_AFTER_2_AFTER}}": "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?w=900&q=80&auto=format&fit=crop",
    "{{BEFORE_AFTER_2_NAME}}": "Louis Vuitton Speedy 30",
    "{{BEFORE_AFTER_2_META}}": "Monogram Canvas · Vachetta Rebuild",
    "{{BEFORE_AFTER_2_BULLET_1}}": "Replacement of dried & cracked Vachetta leather trims",
    "{{BEFORE_AFTER_2_BULLET_2}}": "Hand-stitched rolled leather handles using yellow French thread",
    "{{BEFORE_AFTER_2_BULLET_3}}": "Oxidation removal and polish on brass rivets and padlocks",

    "{{BEFORE_AFTER_3_BEFORE}}": "https://images.unsplash.com/photo-1566150905458-1bf1fc15a4a0?w=900&q=80&auto=format&fit=crop",
    "{{BEFORE_AFTER_3_AFTER}}": "https://images.unsplash.com/photo-1566150905458-1bf1fc15a4a0?w=900&q=80&auto=format&fit=crop",
    "{{BEFORE_AFTER_3_NAME}}": "Hermès Birkin 35",
    "{{BEFORE_AFTER_3_META}}": "Togo Leather · Orange H Pigment Match",
    "{{BEFORE_AFTER_3_BULLET_1}}": "Extraction of grease stains from handles & base seams",
    "{{BEFORE_AFTER_3_BULLET_2}}": "Custom edge paint formulation and multi-layer hand application",
    "{{BEFORE_AFTER_3_BULLET_3}}": "Rebuilding shape using interior structural supports to fix sagging",

    # Testimonials Section (3 items)
    "{{TESTIMONIAL_1_QUOTE}}": "De Leather Craft brought my vintage Chanel bag back to life! The faded corners look brand new and the leather feels incredibly soft. The color match is exact.",
    "{{TESTIMONIAL_1_NAME}}": "Karan Johar",
    "{{TESTIMONIAL_1_META}}": "Mumbai · Chanel Lambskin",
    "{{TESTIMONIAL_2_QUOTE}}": "Outstanding work on my Hermes Birkin. The handle grease stains are completely gone and the sagging shape has been corrected. High-end craftsmanship.",
    "{{TESTIMONIAL_2_NAME}}": "Priya Sharma",
    "{{TESTIMONIAL_2_META}}": "Delhi · Hermès Birkin 35",
    "{{TESTIMONIAL_3_QUOTE}}": "Highly recommend! They replaced the cracked handles on my Louis Vuitton Speedy. The stitching is absolutely flawless and matches the original perfectly.",
    "{{TESTIMONIAL_3_NAME}}": "Ananya Iyer",
    "{{TESTIMONIAL_3_META}}": "Bangalore · LV Speedy",

    # FAQ Section (6 items)
    "{{FAQ_Q1}}": "How long does a typical bag restoration take?",
    "{{FAQ_A1}}": "Most handbag restorations take 3 to 4 weeks. If structural reconstructions (like custom strap rebuilding or interior lining replacement) are needed, it may take up to 6 weeks.",
    "{{FAQ_Q2}}": "Will restoring the color affect the bag's feel?",
    "{{FAQ_A2}}": "No. We use water-based, luxury-grade pigments and thin binding sealers that penetrate leather pores. This preserves the original grain texture and soft hand-feel of calfskin and lambskin.",
    "{{FAQ_Q3}}": "Do you repair internal linings and pockets?",
    "{{FAQ_A3}}": "Yes. We offer interior detailing including pocket re-sewing, ink extraction, zipper repairs, and complete lining replacements using premium silk, suede, or genuine leather.",
    "{{FAQ_Q4}}": "Can you fix cracked Vachetta leather on Louis Vuitton bags?",
    "{{FAQ_A4}}": "Once leather is deeply cracked and split, it cannot be safely glued. We perform panel replacements, replacing the old trim with premium untreated Vachetta leather which will patina naturally over time.",
    "{{FAQ_Q5}}": "Are my luxury bags insured during transport?",
    "{{FAQ_A5}}": "Yes, all items picked up by our doorstep couriers or sent by post are fully insured up to their current fair market valuation for complete peace of mind.",
    "{{FAQ_Q6}}": "Do you provide warranty on stitching and repairs?",
    "{{FAQ_A6}}": "We offer a 6-month warranty covering stitching, leather bonding, handle replacements, and edge paint adhesion on all bag restoration orders."
}

# Read template
with open(template_path, "r", encoding="utf-8") as f:
    template_content = f.read()

# Replace placeholders
output_content = template_content
for key, val in replacements.items():
    # Convert newlines to list items in before/after bullets if needed
    if key.endswith("_DETAILS}}"):
        bullets = val.split("\n")
        formatted_bullets = "".join([f"<li>{b.replace('• ', '')}</li>" for b in bullets if b])
        output_content = output_content.replace(key, formatted_bullets)
    else:
        output_content = output_content.replace(key, val)

# Write output
with open(output_path, "w", encoding="utf-8") as f:
    f.write(output_content)

print(f"Generated successfully at: {output_path}")

# Check if there are any remaining placeholders
remaining = re.findall(r"\{\{[A-Z0-9_]+\}\}", output_content)
if remaining:
    print(f"Warning: The following placeholders were NOT replaced: {set(remaining)}")
else:
    print("All placeholders successfully replaced!")
