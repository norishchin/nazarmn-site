# Research brief: make nazarmn.com the site people (and AI tools) pick

You are a research agent. Your job is to study what works for real estate agent websites, in Minnesota and elsewhere, compare that against **https://nazarmn.com**, and come back with specific, evidence-backed ideas. A second agent will turn your findings into a plan and build it, so be concrete and cite what you saw.

Do the research. Do not change the site, contact anyone, fill in forms, or create accounts.

---

## 1. Who this is for

**Nazar Orishchin**, real estate agent, RE/MAX Results (Team Steady), office at 11200 W 78th St, Eden Prairie, MN 55344. Minnesota license #40776361.

- Former mechanical engineer: BS, Minnesota State University, Mankato; five years in the semiconductor industry (startup, then applications engineering).
- Grew up working construction jobs with his father (carpenter, painter, handyman). Does his own renovations, has pulled his own permits, owns rental property, homeowner 10+ years.
- Born in Ukraine, came to Minnesota at three. Speaks **English, Ukrainian and Russian**.
- Track record: **100+ transactions closed since 2022** (his own). His team, Team Steady at RE/MAX Results: RealTrends Verified 2025 data, 364 sides, $166.63M, No. 2 in Minnesota by sides and volume, No. 1 in Minneapolis; 2,907 total team sales and 698 team reviews (5.0) on Zillow.
- Work: residential buying and selling; multifamily and commercial (apartments, churches, retail, strip centers, mixed use, warehouses, dealerships, special use); off-market deals and creative financing (seller carry, contract for deed). He cold-calls owners to find buildings for buyers.
- Focus towns: Chaska, Chanhassen, Victoria, Eden Prairie, Hopkins, Savage, Shakopee, Burnsville, Prior Lake, Plymouth, Maple Grove. Works anywhere in Minnesota.
- Weekly newsletter: The Nazar Note (beehiiv, news.nazarmn.com), sent Fridays.
- Separate team site on Lofty for listing search: nazarorishchin.teamsteadyrealestate.com.

**Goals, in order:**
1. Get found on Google and in AI tools (ChatGPT, Claude, Perplexity, Google AI Overviews, Copilot).
2. Turn readers into booked 15-minute calls (Calendly).
3. Host a blog that reuses the newsletter.

---

## 2. What the site is today

Static site built with Astro, hosted on GitHub Pages. Fast, little JavaScript. English, plus a Ukrainian version of the main pages.

**Pages:**
- Home, About (bio, family and closing photos, experience box with team stats), Buy, Sell, Invest/Commercial, Reviews (real Google reviews, quoted exactly)
- `/ukrainian-realtor-minnesota/` (English page with Ukrainian and Russian sections)
- `/towns/` comparison table plus 11 town pages (2024 Minneapolis Area REALTORS data, pros and cons, FAQs)
- `/glossary/` (English and Ukrainian terms), `/calculator/` (rental cash flow, cap rate, DSCR)
- 12 guides: first step before buying, buying start to finish, the 30 days before you list, cost to sell in Minnesota, winning multiple offers, inspection reports, contract for deed, which investment properties make sense, off-market commercial deals, buying a duplex and living in one unit, spring photos in fall
- `/uk/` Ukrainian versions of home, buy, sell, invest, about, guides

**Already in place:** structured data (RealEstateAgent, Person, FAQPage, BlogPosting, Dataset), sitemap, robots.txt open to AI crawlers, llms.txt, IndexNow, Google Search Console, Bing Webmaster Tools, Cloudflare Web Analytics, "Short answer" boxes on guides, a downloadable contact card, header with "Book a call" as the main button.

**Known gaps (don't just repeat these; tell us how others solve them):**
- Few first-person client stories; mostly portraits and closing photos
- Town pages run on one data source that's nearly two years old (2024 annual report)
- No video, no Instagram or social proof on the site, no listings or sold history shown
- Search Console and AI visibility data are only days old
- Ukrainian versions exist for main pages and older guides, not town pages or newer guides

---

## 3. Rules any recommendation must respect

These are the owner's rules. Flag any idea that would break one, or skip it.

- No phone number on the website (Calendly replaces it). Phone only in the contact card.
- No em dashes. Plain, short writing. No hype, no "best/#1/top" claims without a source anyone can check.
- No invented reviews, stats, testimonials or client stories. Market numbers need a named, linked, dated source.
- Fair housing: describe homes and markets, never neighborhoods or people by protected class (no "family-friendly", "safe", "good schools" as selling points).
- RE/MAX Results and Equal Housing Opportunity on every page.
- Listing search stays on the Lofty team site, not rebuilt here.
- Keep pages fast. Avoid heavy third-party widgets unless the payoff is clear.
- His name is the brand. No logo or mascot.

---

## 4. What to research

### A. Direct competitors in the Twin Cities
Find and review at least 10 agent or small-team sites. Include:
- **The Antonov Group / Herman Antonov** (theantonovgroup.com), the closest competitor: Russian- and Ukrainian-speaking, Minnetonka.
- Other Ukrainian-, Russian- or Eastern European-speaking agents in Minnesota.
- Top individual agents and small teams in the west and southwest metro (Eden Prairie, Chanhassen, Chaska, Plymouth, Maple Grove, Shakopee, Prior Lake).
- Agents known for investors, multifamily or small commercial in Minnesota.

For each, note: what they lead with, how they show proof (stats, reviews, sold homes, video), town and neighborhood content, lead capture, how they handle languages, what feels genuine vs. templated, and what looks like it actually brings in business. Link to specific pages.

### B. Best-in-class examples anywhere in the US
Find 8 to 12 agent or team sites in other states that are clearly working (strong search rankings, cited by AI tools, active content, real engagement). Prioritize:
- Personal-brand sites for individual agents, not big brokerage templates
- Agents serving a language community (Spanish, Russian, Ukrainian, Chinese, Vietnamese and others)
- Investor-focused agents (house hacking, small multifamily, creative financing)
- Agents whose content gets quoted in AI answers

What exactly do they do that we don't? Formats, page types, proof, calls to action, update cadence.

### C. How people actually search
- Test these in Google, ChatGPT, Perplexity, Google AI Overviews and Copilot. Record who shows up, which pages get cited, and why those pages might win:
  - "Ukrainian speaking realtor Minnesota"
  - "рієлтор у Міннесоті" and "риелтор в Миннесоте"
  - "Russian speaking real estate agent Twin Cities"
  - "realtor Chaska MN", "real estate agent Eden Prairie", "Chanhassen home prices 2025"
  - "cost to sell a house in Minnesota", "Minnesota deed tax seller"
  - "contract for deed Minnesota how it works", "buy a duplex FHA Minnesota"
  - "off-market apartment buildings Minnesota", "commercial real estate agent Eden Prairie"
- Note where nazarmn.com appears, or doesn't.
- Suggest 15 to 25 more questions real Minnesota buyers, sellers and investors ask that a page on this site could answer better than what ranks now.

### D. Content and trust that converts
- Which proof formats work best for individual agents: video walkthroughs, case studies, sold maps, "recent deals" lists, review widgets, press, community involvement?
- How top agents turn a newsletter into search traffic.
- Local-community plays: Ukrainian churches, cultural groups, newcomer resources, Facebook groups. What do agents in other language communities do that's helpful, not spammy?
- Google Business Profile tactics that move local rankings (posts, Q&A, photos, review requests).

### E. A fresh audit of nazarmn.com
Go through every page on phone and desktop. Report:
- First impression in 5 seconds: is it clear who he is, who he helps, and what to do next?
- Anything that reads as generic, AI-written or templated. Quote it and suggest a fix.
- Confusing navigation, dead ends, missing next steps, weak calls to action.
- Technical SEO issues: titles, descriptions, headings, internal links, structured data, page speed (run PageSpeed Insights on the home page, a town page and a guide).
- How AI tools describe Nazar today when asked directly ("Who is Nazar Orishchin?", "Is there a Ukrainian-speaking realtor in Eden Prairie?").

---

## 5. What to hand back

One Markdown file named `nazarmn-research-findings.md`, with these sections:

1. **Summary (10 bullets max):** the most important things you found.
2. **Competitor notes:** a table (name, site, strengths, weaknesses, one idea worth borrowing), then short notes with links.
3. **Best-in-class examples:** what each does well, with links to the exact pages.
4. **Search and AI visibility results:** each test query, who shows up and who gets cited, and where nazarmn.com stands.
5. **Audit of nazarmn.com:** issues by page, each with a quote or screenshot description and a suggested fix.
6. **Recommendations:** 15 to 30 ideas, each with:
   - What to do, in one or two sentences
   - Why (evidence, with links)
   - Effort: S / M / L
   - Expected impact on: search, AI citations, booked calls
   - Whether Nazar has to provide anything (photos, stories, data, accounts)
   - Any conflict with the rules in section 3
7. **Top 5 to do first,** in order, with reasoning.
8. **Things to avoid,** with examples of what failed or looks bad elsewhere.
9. **New page and content ideas:** titles plus target questions, in English and Ukrainian where relevant.
10. **Sources:** every URL you used.

**Standards:**
- Back every claim with something you saw, and link it. Mark guesses as guesses.
- Prefer specific ("add a 'Recent deals' strip like X does at [link]") over general ("build trust").
- If a tactic only works for big teams or big budgets, say so.
- Don't invent numbers. If you can't verify a stat, leave it out.
