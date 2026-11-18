# nazarmn.com strategy, from the Muse research (November 18, 2026)

## Where we stand
- The site is live, fast and well built, but brand new. It doesn't rank yet for any of the 13 test searches. That's normal for a site this young: Google and AI tools need weeks to months, plus links and mentions from elsewhere.
- **Best opening:** Ukrainian and Russian searches. No Minnesota agent page in either language ranked in the top 10.
- **Second opening:** off-market apartment buildings. Only one investor firm shows up.
- **The biggest problem is off the site.** Your RE/MAX and Results.net bios are what AI tools read today, and they're outdated and contradict each other (2 boys vs 3, "5 years experience", no Team Steady, no commercial work). Homes.com shows 78 total sales.

## Checked and already fine
Muse read the site as plain text, so it couldn't see links and buttons. These were already working:
- All 11 town names on the home page are linked.
- There's no duplicate FAQ on Buy, and no "Price: 0 USD" text on the calculator.
- About, Sell and Invest all have booking links.
- The Save contact card exists.

## Done in this round (not live yet)
1. **All 11 town pages, the towns comparison and the AI summary updated to 2025 full-year data** from the Minneapolis Area REALTORS 2025 annual report (current as of January 8, 2026). The price trend now covers 2021 to 2025, and each page says "Updated November 2026".
2. **Robots file** now points to `sitemap.xml`, the sitemap Google and Bing already read.
3. **AI summary file (llms.txt)** shows a "Last updated" date.
4. **Ukrainian home:** "checked November 2026" is now fully in Ukrainian.
5. **Glossary links** now name the guide they go to.
6. **Reviews page** says "Showing 9 of 26 Google reviews".
7. **About** has a short factual "In short" paragraph that AI tools can quote directly.

## Phase 1: you, this week (biggest effect, nothing else beats these)
1. **Fix your bios on RE/MAX.com, Results.net and Homes.com** to match nazarmn.com:
   - Eden Prairie office, Team Steady, English, Ukrainian and Russian
   - residential plus multifamily and commercial, off-market deals, creative financing
   - 100+ transactions since 2022, engineering background
   - website link to nazarmn.com
   I can write one bio for you to paste everywhere.
2. **Google Business Profile:**
   - Set the category to Real estate agent.
   - Add the nazarmn.com link and your Calendly link.
   - Add services, service towns and 10+ photos.
   - Post weekly.
   - Ask every closed client for a review the day after closing (no gifts, no filtering).
   Also send me both Google profile links so the Reviews page can link to "read all on Google" and "leave a review".
3. **Send me your recent deals list** (address or town, close date, price, days on market, buyer or seller side), and say which clients are OK being named.

## Phase 2: me, next 2 to 3 weeks (no input needed, or a quick review)
1. **Ukrainian and Russian buyer guide** (one trilingual page): buying with no US credit history, ITIN loans, down payment programs, how closing works. You check the loan facts with a lender before it goes live.
2. **Off-market apartment buildings page:** your buy box (types, sizes, towns), how a quiet sale works for an owner, and "Can I sell off-market?" answered directly. Needs your buy box in a few lines.
3. **Creative financing page:** seller carry, contract for deed, assumable loans and a few others, each with an example labeled as an example, plus a risks FAQ. Needs a Minnesota attorney's check before publishing.
4. **Minnesota deed tax page:** short answer, table, statute cite, county exception. I can do this anytime.
5. **"Five questions to ask any agent," with your answers.** Needs your answers, about 10 minutes.
6. **Translate the three newest guides into Ukrainian** (cost to sell, multiple offers, duplex), and say clearly which pages are English-only.
7. **A FAQ page** covering fees, areas, process and timelines.

## Phase 3: ongoing habits
- **Newsletter to site:** each Friday issue becomes one dated post on nazarmn.com (500 to 800 words, a small market table with named sources, and a booking link). The Nazar Note stays on beehiiv; the search version lives on nazarmn.com.
- **Monthly town report:** one town per month, in rotation, using the official monthly town reports.
- **Proof:** a short case study after each closing (problem, what you did, result, with permission) and a "Recent deals" page.
- **Video:** one 60 to 90 second clip per listing, and one Ukrainian explainer with English subtitles. Ukrainian video got 130,000 views for Antonov versus little for the same video in English.
- **Community:** a newcomer housing checklist in Ukrainian linking to UACC and the International Institute of Minnesota. Be present at the Ukrainian Festival and UACC events before asking for business.

## Not doing, and why
- **Sold map:** looks empty without many sales in the same towns.
- **Press page:** looks thin without press coverage.
- **Heavy review widgets:** they slow the site. A short block of real reviews plus links to Google works as well.
- **Copying out-of-state legal content:** Minnesota law has to be checked locally.
- **One identical layout for all town pages:** Muse suggested it, but we varied them on purpose so they don't read as templated. The real fix is one or two local lines per town from you.

---

## Update after the second research report (November 18, 2026)

Both reports agree. Merged priority list:

1. **Proof you can check.** A "Selected deals" page (6 to 10 real deals: year, town, property type, your side, problem, what you did, result) and two longer case studies (one home deal, one multifamily or commercial deal). Also a one-line definition of what "100+ transactions since 2022" counts. **Needs you:** fill in `docs/recent-deals-template.md`.
2. **Fix your outside profiles:** the RE/MAX, Results.net and Homes.com bios, and Google Business Profile. Use `docs/results-site-review-prompt.md` for Results.net. These are what AI tools read today.
3. **An investor page for small apartment buildings and owner-users,** plus a due-diligence checklist. Note: report 2 suggested a "5 to 30 unit" page, but your rules say not to describe multifamily by unit count, so the page will describe building types and buyers instead.
4. **Ukrainian and Russian guides** with human review, starting with the buying process, seller costs, contract for deed and the duplex guide. A separate Russian page only if it has enough original content.
5. **Newsletter to site,** weekly. Add a "What happens on the 15-minute call?" note once you confirm how your calls go.

### Fixed in this round (report 2)
- **Fair housing:** the Reviews page no longer shows the review that described a neighborhood by family status. The client's wording wasn't edited, it just isn't displayed. The build check now blocks that kind of wording anywhere on the site.
- **Neutral example:** the first-step guide's example changed from "a yard for the kids" to "a fenced yard for the dog", in English and Ukrainian.
- **Sell page:** "fixes that pay for themselves" became "fixes worth doing before you list".
- **Deed tax:** now explained as the 0.33% state rate plus the 0.01% Environmental Response Fund tax in Hennepin and Ramsey, with the current Department of Revenue link.
- **Contract for deed guide:** now links to the Minnesota Attorney General and Commerce Department guides.
- **Town pages:** now say medians move with the mix of homes sold and aren't an estimate of any one home's value.
- **Generic lines replaced:** "Ready when you are", the Zillow teaser and the investing teaser.
- **iCloud duplicates removed:** iCloud had created " 2" copies inside the project, and some were committed. They're removed, and the project now blocks them from being saved again. Long term, move the project out of the iCloud-synced Documents folder.

### Disagreements with the reports, and our call
- **FAQ markup:** Google rarely shows FAQ rich results for business sites anymore. We keep the FAQ markup because it's accurate and helps AI tools read the questions, but we don't count on it for rankings.
- **llms.txt:** the AI summary file isn't a ranking tool. We keep it because it's cheap. The real work is proof, outside profiles and useful content.
