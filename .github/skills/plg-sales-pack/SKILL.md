---
name: plg-sales-pack
description: 'Create Gumroad/Payhip digital product structure and sales page copy from factory assets. Use for product packs, sales pages, launch emails, pricing, bonuses.'
argument-hint: '[product name] [price]'
---

# PLG Sales Pack

## When to use
Gumroad, Payhip, digital product, sales page, launch, pricing, bonuses.

## Procedure
1. List what the buyer actually receives (files that already exist or will be created in this PR).
2. Write sales page: headline, pain, mechanism, what's inside, who it's for, price, FAQ, CTA.
3. No invented testimonials. Use NEEDS_REVIEW for proof slots.
4. Default stack: core pack + implementation checklist + 7-day calendar slice.
5. Pricing default if unspecified: $17 core / $27 with calendar + prompt pack.
6. Put deliverables under `offers/{slug}/` unless the issue names another path.

## Brand
Load plg-brand-voice. Grateful, urgent, clean. Mechanism over vibes.
