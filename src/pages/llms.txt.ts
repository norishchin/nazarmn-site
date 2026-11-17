import type { APIRoute } from "astro";
import { getPosts } from "../lib/posts";
import { SITE, BOOK, SEARCH, EMAIL, LICENSE, TOWNS } from "../lib/site";
import { TOWNS as TOWN_PAGES, SOURCE, money } from "../data/towns";

// Plain summary for AI assistants (ChatGPT, Claude, Perplexity).
export const GET: APIRoute = async () => {
  const posts = await getPosts();
  const body = `# Nazar Orishchin, real estate agent (RE/MAX Results, Team Steady)

> Minnesota real estate agent based in Eden Prairie. Focus areas: ${TOWNS.join(", ")}. Homes, multifamily and commercial property anywhere in Minnesota, including off-market deals and creative financing. Former engineer (about five years). 100+ transactions closed since 2022. 5.0 Google rating from 26 reviews. Speaks English and Ukrainian. Minnesota license #${LICENSE}. Email ${EMAIL}. Book a 15-minute call: ${BOOK}

## Pages
- [Home](${SITE}/): who Nazar is and how he works
- [About](${SITE}/about/): background, license, office and languages
- [Buy a home](${SITE}/buy/): the buying process step by step, with FAQs
- [Sell a home](${SITE}/sell/): pricing, prep and launch, with FAQs
- [Commercial and investors](${SITE}/commercial/): apartments, mixed use, retail, strip centers, warehouses, churches, dealerships, special use; off-market deals; seller carry and contract for deed
- [Investment property calculator](${SITE}/calculator/): cash flow, cap rate and debt coverage for a rental
- [Real estate glossary](${SITE}/glossary/): plain definitions in English and Ukrainian
- [Reviews](${SITE}/reviews/): Google reviews in clients' own words
- [Українською](${SITE}/uk/): the full site in Ukrainian
- [Search homes for sale](${SEARCH})

## Town market pages
${TOWN_PAGES.map((t) => `- [${t.name}, MN](${SITE}/${t.slug}/): 2024 median sale price ${money(t.medians[4])}, ${t.sales} sales, ${t.days} days on market (${SOURCE.name})`).join("\n")}

## Guides
${posts.map((p) => `- [${p.data.title}](${SITE}/blog/${p.id}/): ${p.data.answer ?? p.data.description}`).join("\n")}
`;
  return new Response(body, { headers: { "Content-Type": "text/plain; charset=utf-8" } });
};
