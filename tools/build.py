#!/usr/bin/env python3
"""Builds nazarmn.com. Run from the repo root: python3 tools/build.py"""
import os, html, json

SITE = "https://nazarmn.com"
PHONE = '<a href="tel:+19528469173">(952) 846-9173</a>'
TS = "https://nazarorishchin.teamsteadyrealestate.com"
NOTE = "https://nazars-newsletter-73890a.beehiiv.com/"
TODAY = "2026-11-13"
PAGES = []

NAV = [("/buy/", "Buy"), ("/sell/", "Sell"), ("/commercial/", "Commercial"),
       ("/reviews/", "Reviews"), ("/blog/", "Blog"), ("/uk/", "Українською")]


def nav_links(active):
    return "".join(
        '<a href="%s"%s>%s</a>' % (u, ' aria-current="page"' if u == active else "", t)
        for u, t in NAV)


def page(path, title, desc, body, active="", lang="en", extra_head="", image="/images/share.jpg"):
    url = SITE + path
    out = f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Nazar Orishchin">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="{SITE}{image}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='8' fill='%230f1f33'/%3E%3Ctext x='32' y='45' font-family='Georgia,serif' font-size='40' font-weight='600' text-anchor='middle' fill='%23f7f3ec'%3EN%3C/text%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&amp;family=Inter:wght@400;600&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/site.css">
{extra_head}</head>
<body>
<header class="site-header">
<div class="wrap bar">
<a class="wordmark" href="/">Nazar Orishchin</a>
<nav class="nav" aria-label="Main">{nav_links(active)}<a class="call" href="tel:+19528469173">(952) 846-9173</a></nav>
<details class="menu"><summary>Menu</summary><nav aria-label="Mobile">{nav_links(active)}<a href="/#contact">Contact</a><a href="tel:+19528469173">Call (952) 846-9173</a></nav></details>
</div>
</header>
<main>
{body}
</main>
<footer class="site-footer">
<div class="wrap">
<div>
<a class="wordmark" href="/">Nazar Orishchin</a>
<p>RE/MAX Results · Team Steady · Minnesota license #40776361</p>
<p>11200 W 78th St, Eden Prairie, MN 55344</p>
<p>Each office independently owned and operated. Equal Housing Opportunity.</p>
<p>© 2026 Nazar Orishchin</p>
</div>
<div>
<h4>Site</h4>
<a href="/buy/">Buy a home</a><a href="/sell/">Sell a home</a><a href="/commercial/">Commercial and investors</a><a href="/reviews/">Reviews</a><a href="/blog/">Blog</a><a href="/uk/">Українською</a>
</div>
<div>
<h4>Elsewhere</h4>
<a href="{TS}">Team Steady site</a><a href="{NOTE}">The Nazar Note</a><a href="https://facebook.com/NazarO15">Facebook</a><a href="https://instagram.com/nazar_realtor_mn">Instagram</a><a href="https://linkedin.com/in/nazar-orishchin">LinkedIn</a>
</div>
</div>
</footer>
</body>
</html>
"""
    fp = path.strip("/")
    fp = os.path.join(fp, "index.html") if fp and not fp.endswith(".html") else (fp or "index.html")
    os.makedirs(os.path.dirname(fp) or ".", exist_ok=True)
    open(fp, "w", encoding="utf-8").write(out)
    if not path.endswith("404.html"):
        PAGES.append(path)


def newsletter(label="The Nazar Note", head="One short email every Friday."):
    return f"""<section class="band" id="note">
<div class="wrap section tight band-grid">
<div class="stack">
<p class="label">{label}</p>
<h2>{head}</h2>
<p class="soft">West metro market numbers, new openings, and one thing worth doing this weekend. Short enough to read with your coffee.</p>
</div>
<div class="sub">
<a class="btn primary" href="{NOTE}" target="_blank" rel="noopener">Get the Friday note</a>
<small>Opens the sign-up page for The Nazar Note. Free. Unsubscribe anytime.</small>
</div>
</div>
</section>"""


# ---------- reviews (Google, clients' own words, captured Nov 12, 2026) ----------
REVIEWS = [
    ("Alena Golovchuk", "Buyer", ["Working with Nazar was the best decision we made during our home buying process. He is a true professional who knows the market, is very responsive, honest, and works hard behind the scenes to help you purchase your dream home. He was able to get our offer accepted within 2 days of the home going on market AND drop 15k from the asking price. HE is the guy you need in your corner! The home buying process was smooth and stress-free. We cannot recommend him enough!"]),
    ("Pavlo Fursyak", "First-time buyer", ["Buying our first home felt overwhelming, and We were honestly very nervous about the whole process. From day one, Nazar made everything feel simple, organized, and stress-free. He patiently answered every question, explained every step, and made sure we always knew what to expect. His support gave us so much confidence throughout the entire journey. What impressed us the most was that his help didn’t stop after closing. Even after the deal was completed, he continued to check in, answer our questions, and guide us through the next steps. That level of care is something we truly appreciate and will never forget. We are incredibly grateful for everything Nazar did for us and couldn’t have asked for a better realtor for our first home. We highly recommend him to anyone looking for a knowledgeable, professional, and genuinely caring real estate agent. Thank you, Nazar, for making such an important milestone such a wonderful experience!"]),
    ("Heather Sinz", "Buyer and seller", ["Nazar went above and beyond for my husband and I, from start to finish, helping us balance selling and buying at the same time. He is creative, knowledgeable and personable. He helped us find the most house for our money and was even personally generous to us in a way he did not have to be when the seller really dropped the ball in a big way. We can’t say enough good things about Nazar."]),
    ("jarred knapp", "Buyer", ["I had a fantastic experience working with Nazar. From start to finish, he was on top of every detail—communicative, proactive, and always a step ahead. He helped me secure a great purchase price and guided us through a competitive offer situation to ultimately win the deal.", "What stood out most was his problem-solving mindset. When unexpected issues came up (as they always do in real estate), he never got rattled—he calmly found solutions and kept everything moving forward. He's extremely easy to work with and made the entire process smooth and efficient.", "If you're looking for a knowledgeable, steady, and responsive agent who knows how to get deals done, I'd highly recommend working with him."]),
    ("Pavlo Kaploukhyi", "Buyer", ["Working with Nazar was awesome. I could clearly tell that he cared about about getting us the best deal possible during the whole process of buying a home. He responded quickly, explained details clearly and made the whole process of finding the right home and negotiating a good price easy. Great experience!"]),
    ("Yevy Drachev", "Buyer", ["Nazar didn't waste ours or his own time while finding us a home. We were pregnant with twins and needed to get our own house asap. Nazar didn't let us settle for anything less then what we needed. He found us a home that's perfect for our growing family in a neighborhood full of kids for our kids to play with. Nazar was very responsive any time of day or evening. Absolutely professional and really knows the market. Will DEFINITELY call him again with our next house purchase. We are very happy with our choice of realtor."]),
    ("Sergey Timoshenko", "Investor", ["Lots of good things to say about Nazar. Any real estate purchases I make, I’m ALWAYS going with Nazar. If you want THE DEAL, this is a guy you WANT to keep in your phone book... on speed dial. Great personality, honest with me, gave me all my options for my future real estate investments. Recommended him to anyone 100/10"]),
    ("Sam Jones", "Buyer", ["From the beginning I felt very comfortable with him as he really listened to what I was looking for in a new home. He had an endless amount of patience as I asked him a million questions. I didn't have to wait very long for him to get back to me if I had to leave a message as he always got back to me in a timely fashion. And when I was ready to give up after being repeatedly outbid, he found me the perfect place for me and when I found out I got it, he made sure the closing went very smoothly. And then he brought me a nice bottle of wine to my housewarming party! I would definitely recommend Nazar and should I ever decide to move again, I'll use his services again."]),
    ("Josh Little", "Client", ["Nazar is top notch! Very knowledgable on the process and market. I'd recommend him to any of my friends."]),
]


def quote(name, text, cls="quote"):
    paras = "".join(f"<p>{html.escape(t)}</p>" for t in ([text] if isinstance(text, str) else text))
    return f"""<figure class="{cls}"><div class="stars" aria-label="5 out of 5 stars">★★★★★</div><blockquote>{paras}</blockquote><figcaption><b>{html.escape(name)}</b> · Google review</figcaption></figure>"""


def pull(name, text):
    return f"""<figure class="pull"><blockquote>“{html.escape(text)}”</blockquote><figcaption><b>{html.escape(name)}</b> · Google review</figcaption></figure>"""


# ---------- blog posts ----------
POSTS = [
 dict(slug="what-i-look-for-in-an-inspection-report", title="What I look for first in a home inspection report",
      desc="An engineer turned real estate agent on how to read a home inspection report: what matters, what is normal, and what to ask the seller to fix.",
      teaser="A 60-page report looks scary. Most of it is routine. Here is how I sort the real problems from the noise.",
      body="""
<p>I spent about five years as an engineer before I sold houses. The habit that carried over is simple: read the whole document, then sort it. An inspection report is long because inspectors write down everything they see. Long does not mean bad.</p>
<h2>Sort every item into three piles</h2>
<ul>
<li><strong>Safety and structure.</strong> Foundation movement, roof at the end of its life, active water in the basement, unsafe wiring, a furnace that is venting poorly. These can change the deal.</li>
<li><strong>Systems near the end.</strong> An older water heater or air conditioner that works today. Not a defect, but a cost you should plan for.</li>
<li><strong>Maintenance.</strong> Caulk, a loose handrail, a dripping faucet, a missing downspout extension. Every house has a list like this, including new ones.</li>
</ul>
<h2>The four places I read twice</h2>
<p><strong>Water.</strong> Where does rain go when it leaves the roof? Grading, gutters, and downspouts cause more basement trouble than anything else, and they are usually cheap to fix. Stains with no clear source are worth a second look.</p>
<p><strong>Roof.</strong> I want the inspector's read on remaining life and whether there is hail or wind damage. Insurance companies care about roof age, so you should too.</p>
<p><strong>Electrical panel.</strong> The brand, the age, and whether the wiring matches the breakers. Some older panels are a known problem and worth pricing before you close.</p>
<p><strong>Mechanicals.</strong> Furnace, AC, and water heater age. I ask for service records. A 20-year-old furnace that has been maintained is a different conversation than one that hasn't.</p>
<h2>What to ask the seller for</h2>
<p>Ask for the first pile. Be reasonable about the second. Leave the third alone. Sellers respond better to a short, specific request with a contractor quote attached than to a list of 30 small items. That is also how you keep the deal together when another buyer is waiting.</p>
<h2>When to bring in a specialist</h2>
<p>A general inspector flags things. A structural engineer, roofer, electrician, or sewer scope answers them. If a single item could cost you five figures, spend the few hundred dollars to get a real answer before your inspection period ends.</p>
<p class="note">Buying in the west metro and want a second read on a report? Call or text me at (952) 846-9173. I'll tell you which pile each item belongs in.</p>
"""),
 dict(slug="contract-for-deed-minnesota", title="Contract for deed in Minnesota: how it works and when it makes sense",
      desc="A plain-English guide to contract for deed in Minnesota for buyers and sellers: how payments work, the risks on each side, and when seller financing fits.",
      teaser="Seller financing can close a deal a bank won't. It also carries real risk on both sides. A plain-English walkthrough.",
      body="""
<p>A contract for deed is seller financing. The buyer makes payments to the seller, not to a bank, and gets the deed once the contract is paid off. I use it in the right situations for homes, small apartment buildings, and commercial property.</p>
<h2>How it works</h2>
<ol>
<li>Buyer and seller agree on price, down payment, interest rate, monthly payment, and term.</li>
<li>The buyer moves in or takes over the building and pays the seller every month. The buyer usually covers taxes, insurance, and repairs.</li>
<li>Many contracts end with a balloon: the remaining balance is due on a set date, often paid by refinancing with a bank.</li>
<li>When the balance is paid, the seller signs over the deed.</li>
</ol>
<h2>When it makes sense</h2>
<ul>
<li>The buyer is self-employed, new to the country, or has income a bank underwrites poorly, but has a solid down payment.</li>
<li>The property is hard to finance: mixed use, a building that needs work, a special-use property like a church.</li>
<li>The seller owns it free and clear and wants steady income more than a lump sum.</li>
</ul>
<h2>The risks, plainly</h2>
<p><strong>For buyers:</strong> if you miss payments, the seller can cancel the contract through a legal notice process that moves much faster than a bank foreclosure. You could lose the property and what you've paid in. If a balloon is coming, you need a real plan to refinance before it arrives.</p>
<p><strong>For sellers:</strong> you are the bank. If the buyer stops paying, you take the property back in whatever condition it is in. If you still have a mortgage on it, your lender may have the right to call the loan due.</p>
<h2>How to do it right</h2>
<ul>
<li>Have a real estate attorney draft or review the contract. Minnesota has specific rules for these, and the state tightened them in 2024, especially for investors who sell this way often.</li>
<li>Close at a title company and record the contract with the county.</li>
<li>Get a title search and an inspection, same as any purchase.</li>
<li>Write down who pays taxes and insurance, and how the seller will get proof.</li>
<li>Underwrite the balloon. If the plan is to refinance in five years, talk to a lender now about what that will take.</li>
</ul>
<p class="note">This is general information, not legal advice. If you're weighing a contract for deed as a buyer or a seller, call or text me at (952) 846-9173 and I'll walk through the numbers with you.</p>
"""),
 dict(slug="how-off-market-commercial-deals-happen", title="How off-market commercial deals actually happen",
      desc="How off-market apartment and commercial property deals come together in Minnesota: finding owners, earning the conversation, and structuring terms.",
      teaser="Most small apartment buildings and commercial properties never get a sign in the yard. Here is how they change hands.",
      body="""
<p>Many apartment buildings, strip centers, and warehouses in Minnesota sell without ever being listed. The owner gets a call, has a conversation, and a deal comes together quietly. Here is what that looks like from the inside.</p>
<h2>It starts with the owner, not the property</h2>
<p>Off-market work is research and phone calls. County records, rental licenses, and business filings tell you who owns a building and for how long. Then you call. Most owners say no. Some say "not now." A few say "what would you pay?" That is the whole job, repeated.</p>
<h2>Why owners sell this way</h2>
<ul>
<li><strong>Privacy.</strong> Tenants and employees don't find out from a sign.</li>
<li><strong>Simplicity.</strong> One serious buyer, no parade of showings.</li>
<li><strong>Terms.</strong> A direct conversation leaves room for seller carry, a longer close, or a sale structured around taxes.</li>
</ul>
<h2>What a buyer needs before the call comes</h2>
<p>When I bring a deal to an investor, the ones who win are ready. They have proof of funds or a lender who knows them, a clear picture of what they buy, and the ability to answer in days. An off-market seller picked a quiet sale to avoid hassle. Slow buyers are hassle.</p>
<h2>Underwrite it like no one else has</h2>
<p>A listed property comes with a marketing package. An off-market one comes with whatever the owner hands you. I rebuild the numbers from the rent roll, actual expenses, and tax records, then stress them: what if two units sit empty, what if insurance goes up, what does the roof have left. If it still works, we make an offer.</p>
<h2>Property types I work</h2>
<p>Apartments, mixed use, retail, strip centers, warehouses, churches, dealerships, and special-use buildings. The process is the same. The buyer pool is what changes.</p>
<p class="note">Own a building and want to know what a quiet sale would look like? Or want to see deals before they hit the market? Email <a href="mailto:Nazar@ts-re.com">Nazar@ts-re.com</a> or call (952) 846-9173.</p>
"""),
 dict(slug="selling-in-spring-take-photos-in-fall", title="Selling in spring? Take the listing photos in fall",
      desc="Why Minnesota sellers planning a spring listing should shoot exterior photos in September or October, plus a short fall prep list.",
      teaser="Early spring in Minnesota is brown grass and bare trees. If you plan to list then, shoot the outside of your house now.",
      body="""
<p>The busiest listing season in Minnesota starts while the yard still looks its worst. Snow is melting, the grass is brown, and the trees are bare. Buyers scroll past photos like that.</p>
<p>The fix is easy. If you plan to sell next spring, take the exterior photos in September or October, while the lawn is green and the fall color is up.</p>
<h2>What to shoot in fall</h2>
<ul>
<li>Front of the house, straight on and from both corners</li>
<li>Backyard, deck, patio, and any view</li>
<li>Drone shots if the lot, the trees, or nearby water are selling points</li>
<li>Gardens and landscaping while they are full</li>
</ul>
<p>Interior photos can wait until right before you list, once the house is cleaned and staged.</p>
<h2>A short fall prep list</h2>
<ul>
<li>Mow and edge the day before the shoot</li>
<li>Clear leaves off the roof, gutters, and walkways</li>
<li>Put away hoses, toys, and trash bins</li>
<li>Wash the front windows and sweep the entry</li>
</ul>
<h2>What it costs you</h2>
<p>An hour of yard work and a short visit from the photographer. In return, your listing goes live in March or April with the best-looking exterior in the neighborhood.</p>
<p class="note">Thinking about listing in the west metro next spring? Call or text me at (952) 846-9173 in early fall and I'll get the photographer scheduled.</p>
"""),
 dict(slug="buying-your-first-home-in-minnesota", title="Buying your first home in Minnesota: the steps in order",
      desc="A first-time home buyer's guide to the Minnesota purchase process, from pre-approval to closing day, in plain language.",
      teaser="Pre-approval, showings, offer, inspection, appraisal, closing. What happens at each step and what you need to do.",
      body="""
<p>Buying a first home feels complicated because nobody explains the order. Here it is, start to finish.</p>
<h2>1. Talk to a lender first</h2>
<p>A pre-approval tells you what you can borrow and what the monthly payment looks like. Sellers expect one with every offer. Ask the lender about first-time buyer and down payment assistance programs while you're at it.</p>
<h2>2. Decide what matters</h2>
<p>Pick your must-haves, your nice-to-haves, and the towns you'd live in. Be honest about commute and schools. A clear list saves weekends.</p>
<h2>3. See homes</h2>
<p>I set up the showings and tell you what I see: the age of the roof and furnace, signs of water, how the price compares to recent sales. You don't need to love the first one.</p>
<h2>4. Write the offer</h2>
<p>Price is one part. Earnest money, closing date, inspection, and financing terms matter too. I pull the comparable sales so the number has a reason behind it.</p>
<h2>5. Inspection</h2>
<p>Once the seller accepts, you hire an inspector. We read the report together, sort the real problems from routine maintenance, and decide what to ask the seller to fix.</p>
<h2>6. Appraisal and underwriting</h2>
<p>The lender orders an appraisal and finishes reviewing your file. Your job is to send documents fast and not open new credit or change jobs.</p>
<h2>7. Final walkthrough and closing</h2>
<p>We walk the house one more time to confirm its condition. Then you sign at the title company and get the keys.</p>
<h2>After closing</h2>
<p>File for homestead with your county so you're taxed as an owner-occupant, change the locks, and keep my number. I answer questions long after the sale.</p>
<p class="note">Розмовляю українською. If you or your family would rather go through these steps in Ukrainian, see <a href="/uk/">the Ukrainian page</a> or call (952) 846-9173.</p>
"""),
]


def build():
    # ---------- home ----------
    ld = json.dumps({"@context": "https://schema.org", "@type": "RealEstateAgent", "name": "Nazar Orishchin",
        "url": SITE + "/", "image": SITE + "/images/nazar-orishchin.jpg", "telephone": "+1-952-846-9173",
        "email": "Nazar@ts-re.com", "knowsLanguage": ["en", "uk"],
        "address": {"@type": "PostalAddress", "streetAddress": "11200 W 78th St", "addressLocality": "Eden Prairie",
                    "addressRegion": "MN", "postalCode": "55344", "addressCountry": "US"},
        "areaServed": ["Chaska", "Chanhassen", "Victoria", "Eden Prairie", "Hopkins", "Savage", "Shakopee",
                       "Burnsville", "Prior Lake", "Minnesota"],
        "parentOrganization": {"@type": "Organization", "name": "RE/MAX Results"},
        "sameAs": ["https://facebook.com/NazarO15", "https://instagram.com/nazar_realtor_mn",
                   "https://linkedin.com/in/nazar-orishchin", TS]}, ensure_ascii=False)
    posts_cards = "".join(
        f'<a class="card post-card" href="/blog/{p["slug"]}/"><time datetime="{TODAY}">November 2026</time><h3>{p["title"]}</h3><p class="soft grow">{p["teaser"]}</p><span class="arrow">Read it</span></a>'
        for p in POSTS[:3])
    home = f"""
<div class="wrap hero" id="top">
<div class="stack lg">
<p class="label">RE/MAX Results · Team Steady · Licensed in Minnesota</p>
<h1>Nazar Orishchin, real estate agent for Chaska, Chanhassen and the west metro.</h1>
<p class="lead">Homes, investment property and commercial buildings across Minnesota. I worked as an engineer for five years before real estate, so I run the numbers before you sign anything.</p>
<div class="cta"><a class="btn primary" href="tel:+19528469173">Call or text (952) 846-9173</a><span class="small">English and Ukrainian. <a href="/uk/">Розмовляю українською.</a></span></div>
</div>
<div class="photo"><img src="/images/nazar-orishchin.jpg" alt="Nazar Orishchin, real estate agent, in a gray blazer" width="900" height="1350" fetchpriority="high"></div>
</div>

<section class="rule" aria-label="At a glance"><div class="wrap section tight stats">
<div class="stat"><b>100+</b><span>Transactions closed since 2022</span></div>
<div class="stat"><b>5.0</b><span>Google rating, 26 reviews, Nov 2026</span></div>
<div class="stat"><b>5 years</b><span>As an engineer before real estate</span></div>
<div class="stat"><b>2</b><span>Languages: English and Ukrainian</span></div>
</div></section>

<section class="rule"><div class="wrap section stack lg" id="help">
<div class="stack"><h2>How I help</h2><p class="soft">Pick the one that fits you.</p></div>
<div class="grid g3">
<a class="card" href="/buy/"><p class="label">Buying a home</p><h3>Find the right home and pay the right price.</h3><p class="soft grow">I check comps, condition and disclosures before we write an offer, and I tell you when a house isn't worth it.</p><span class="arrow">How buying works</span></a>
<a class="card" href="/sell/"><p class="label">Selling a home</p><h3>Price it right, prep it right, sell it once.</h3><p class="soft grow">A price built on real comps, a short list of fixes worth doing, and clear updates from listing day to closing.</p><span class="arrow">How selling works</span></a>
<a class="card" href="/commercial/"><p class="label">Investors and commercial</p><h3>Buildings that pencil out.</h3><p class="soft grow">Apartments, mixed use, retail, strip centers, warehouses, churches and special use. Off-market deals and creative terms.</p><span class="arrow">Commercial work</span></a>
</div>
</div></section>

<section class="rule"><div class="wrap section stack lg">
<h2>What clients say</h2>
<div class="grid g3">
{quote("Alena Golovchuk", "He was able to get our offer accepted within 2 days of the home going on market AND drop 15k from the asking price.")}
{quote("Heather Sinz", "He is creative, knowledgeable and personable. He helped us find the most house for our money.")}
{quote("Sergey Timoshenko", "Any real estate purchases I make, I’m ALWAYS going with Nazar.")}
</div>
<a class="arrow" href="/reviews/">Read the full reviews</a>
</div></section>

<section class="rule"><div class="wrap section split" id="about">
<div><h2>About Nazar</h2><img class="about-photo" src="/images/nazar-orishchin-about.jpg" alt="Nazar Orishchin smiling, seated" width="800" height="1200" loading="lazy"></div>
<div class="stack">
<p>I was born in Ukraine and came to Minnesota when I was three. I earned an engineering degree and worked as an engineer for about five years before going full time in real estate.</p>
<p>That background shows up in how I work. I read the inspection report line by line, underwrite every investment deal, and give you the number plainly. I'm handy too, so I can give you a realistic read on what a repair takes.</p>
<p>I work out of the RE/MAX Results office in Eden Prairie as part of Team Steady. Outside of work, I'm a husband and a dad.</p>
<h3 style="margin-top:16px">Where I work most</h3>
<ul class="towns"><li>Chaska</li><li>Chanhassen</li><li>Victoria</li><li>Eden Prairie</li><li>Hopkins</li><li>Savage</li><li>Shakopee</li><li>Burnsville</li><li>Prior Lake</li></ul>
<p class="soft">Investment and commercial property anywhere in Minnesota.</p>
</div>
</div></section>

<section class="rule"><div class="wrap section stack lg">
<div class="stack"><h2>From the blog</h2><p class="soft">Short, practical, written from deals I've worked.</p></div>
<div class="grid g3">{posts_cards}</div>
<a class="arrow" href="/blog/">All posts</a>
</div></section>

{newsletter()}

<section><div class="wrap section split contact" id="contact">
<div class="stack" style="align-items:flex-start"><h2>Let's talk</h2><p class="soft">Call or text is fastest. Email works too.</p><a class="btn ghost" href="mailto:Nazar@ts-re.com">Email Nazar</a></div>
<dl>
<div><dt>Phone</dt><dd>{PHONE}</dd></div>
<div><dt>Email</dt><dd><a href="mailto:Nazar@ts-re.com">Nazar@ts-re.com</a></dd></div>
<div><dt>Office</dt><dd>RE/MAX Results<br>11200 W 78th St<br>Eden Prairie, MN 55344</dd></div>
<div><dt>Follow</dt><dd><a href="https://facebook.com/NazarO15">Facebook</a><a href="https://instagram.com/nazar_realtor_mn">Instagram</a><a href="https://linkedin.com/in/nazar-orishchin">LinkedIn</a></dd></div>
</dl>
</div></section>
"""
    page("/", "Nazar Orishchin | Real Estate Agent for Chaska, Chanhassen and the West Metro",
         "Nazar Orishchin, RE/MAX Results real estate agent for Chaska, Chanhassen and the west metro. Homes, multifamily and commercial property across Minnesota. English and Ukrainian.",
         home, extra_head=f'<script type="application/ld+json">{ld}</script>\n')

    # ---------- buy ----------
    buy = f"""
<div class="wrap page-hero split">
<div class="stack lg"><p class="label">Buying a home</p><h1>Buy the right house at the right price.</h1>
<p class="lead">You get an agent who reads the disclosures, checks the comps, and tells you when to walk away. First home or fifth, the process is the same and I explain each step.</p>
<div><a class="btn primary" href="{TS}">Search homes on my Team Steady site</a></div></div>
<div class="photo"><img src="/images/nazar-smiling.jpg" alt="Nazar Orishchin standing by a window" width="800" height="1200"></div>
</div>
<section class="rule"><div class="wrap section split">
<div class="stack"><h2>How buying works</h2><p class="soft">Seven steps, in order.</p></div>
<ol class="steps">
<li><div><h3>Lender and budget</h3><p>Get pre-approved so you know your payment and sellers take your offer seriously.</p></div></li>
<li><div><h3>The list</h3><p>We agree on must-haves, towns and price range before the first showing.</p></div></li>
<li><div><h3>Showings</h3><p>I point out roof and furnace age, signs of water, and anything that will cost you later.</p></div></li>
<li><div><h3>Offer</h3><p>Price backed by recent sales, with terms built for how much competition the house has.</p></div></li>
<li><div><h3>Inspection</h3><p>We sort the report into real problems and routine maintenance, then ask the seller for what matters.</p></div></li>
<li><div><h3>Appraisal and loan</h3><p>I keep the lender, title company and seller's agent on schedule.</p></div></li>
<li><div><h3>Closing</h3><p>Final walkthrough, sign, keys. I stay available after.</p></div></li>
</ol>
</div></section>
<section class="rule"><div class="wrap section stack lg">
<h2>What you get from an engineer</h2>
<div class="grid g3">
<div class="card"><h3>A read on condition</h3><p class="soft">I'm handy and I know what repairs take. You hear the realistic cost before you fall for the kitchen.</p></div>
<div class="card"><h3>A price with reasons</h3><p class="soft">Every offer number comes from comparable sales, adjusted for condition, with the math shown.</p></div>
<div class="card"><h3>Straight answers</h3><p class="soft">If a house is overpriced or has a problem, I say so, even when it means more showings.</p></div>
</div>
{pull("Pavlo Fursyak", "From day one, Nazar made everything feel simple, organized, and stress-free. He patiently answered every question, explained every step, and made sure we always knew what to expect.")}
<a class="arrow" href="/blog/buying-your-first-home-in-minnesota/">Read the first-time buyer guide</a>
</div></section>
{newsletter("Not ready yet?", "Watch the market from your inbox.")}
"""
    page("/buy/", "Buy a Home in the West Metro | Nazar Orishchin",
         "Buying a home in Chaska, Chanhassen, Eden Prairie or the west metro. An engineer-trained agent who checks comps, condition and disclosures before you offer.", buy, active="/buy/")

    # ---------- sell ----------
    sell = f"""
<div class="wrap page-hero split">
<div class="stack lg"><p class="label">Selling a home</p><h1>Price it right, prep it right, sell it once.</h1>
<p class="lead">Homes that sit get discounted. The plan is to launch at a price the market agrees with, looking its best, and to keep you informed until closing.</p>
<div><a class="btn primary" href="{TS}">See what your home is worth</a></div></div>
<div class="photo"><img src="/images/nazar-laughing.jpg" alt="Nazar Orishchin laughing, seated" width="800" height="1200"></div>
</div>
<section class="rule"><div class="wrap section split">
<div class="stack"><h2>How selling works</h2><p class="soft">Six steps from first walk-through to closing.</p></div>
<ol class="steps">
<li><div><h3>Walk-through</h3><p>I see the house, ask about updates, and learn your timeline.</p></div></li>
<li><div><h3>Pricing</h3><p>You get recent sales, current competition and a recommended price with the reasoning.</p></div></li>
<li><div><h3>Prep</h3><p>A short list of fixes that pay for themselves. I skip the ones that don't.</p></div></li>
<li><div><h3>Photos and launch</h3><p>Professional photos, a listing written for your house, and a launch timed for the most showings.</p></div></li>
<li><div><h3>Offers</h3><p>I lay out each offer side by side: price, financing, contingencies and risk.</p></div></li>
<li><div><h3>Inspection to closing</h3><p>I handle the repair negotiation and keep title, lender and buyer's agent moving.</p></div></li>
</ol>
</div></section>
<section class="rule"><div class="wrap section stack lg">
<h2>Selling and buying at once</h2>
<p class="lead">Most sellers also need somewhere to go. I plan both sides together so you're not carrying two houses or living out of boxes.</p>
{pull("Heather Sinz", "Nazar went above and beyond for my husband and I, from start to finish, helping us balance selling and buying at the same time.")}
<a class="arrow" href="/blog/selling-in-spring-take-photos-in-fall/">Planning a spring sale? Read this first</a>
</div></section>
<section class="rule"><div class="wrap section stack center">
<h2>Want a number for your house?</h2>
<p class="soft">Call or text {PHONE}. I'll look at it in person and give you a price range, no obligation.</p>
</div></section>
"""
    page("/sell/", "Sell Your Home in the West Metro | Nazar Orishchin",
         "Selling a home in Chaska, Chanhassen, Eden Prairie or the west metro. Comp-based pricing, a short prep list, and clear updates from listing to closing.", sell, active="/sell/")

    # ---------- commercial ----------
    com = f"""
<div class="wrap page-hero split">
<div class="stack lg"><p class="label">Investors and commercial</p><h1>Apartment and commercial buildings that pencil out.</h1>
<p class="lead">I find, underwrite and close investment property across Minnesota, on and off the market. Engineer first, agent second: if the numbers don't work, I'll say so before you spend money on due diligence.</p>
<div><a class="btn primary" href="mailto:Nazar@ts-re.com?subject=Deal%20to%20look%20at">Send me a deal to look at</a></div></div>
<div class="photo"><img src="/images/nazar-window.jpg" alt="Nazar Orishchin looking out a window" width="800" height="1200"></div>
</div>
<section class="rule"><div class="wrap section stack lg">
<h2>Property types</h2>
<ul class="tags"><li>Apartments</li><li>Mixed use</li><li>Retail</li><li>Strip centers</li><li>Warehouses</li><li>Churches</li><li>Dealerships</li><li>Special use</li></ul>
</div></section>
<section class="rule"><div class="wrap section stack lg">
<h2>How I work</h2>
<div class="grid g3">
<div class="card"><p class="label">Sourcing</p><h3>Off-market first</h3><p class="soft">Many buildings sell without a listing. I research owners, make the calls, and bring you the ones worth a look.</p></div>
<div class="card"><p class="label">Underwriting</p><h3>Numbers rebuilt from scratch</h3><p class="soft">Rent roll, real expenses, taxes, and what the roof and mechanicals have left. Then I stress the numbers.</p></div>
<div class="card"><p class="label">Structure</p><h3>Creative terms</h3><p class="soft">Seller carry, contract for deed, and longer closes when a bank loan alone won't get it done.</p></div>
</div>
{pull("jarred knapp", "When unexpected issues came up (as they always do in real estate), he never got rattled—he calmly found solutions and kept everything moving forward.")}
</div></section>
<section class="rule"><div class="wrap section split">
<div class="stack"><h2>Who I work with</h2></div>
<ol class="steps">
<li><div><h3>Investors</h3><p>First rental or a growing portfolio. Tell me what you buy and I'll send what fits.</p></div></li>
<li><div><h3>Owner-users</h3><p>Business owners buying their own building: shops, dealerships, warehouses, churches.</p></div></li>
<li><div><h3>Owners thinking about selling</h3><p>A quiet conversation about value and options, with no sign and no pressure.</p></div></li>
</ol>
</div></section>
<section class="rule"><div class="wrap section split faq">
<h2>Common questions</h2>
<div>
<details><summary>Where in Minnesota do you work?</summary><p>Anywhere in the state for investment and commercial property. Most of my work is in the Twin Cities metro and the towns within a couple of hours of it.</p></details>
<details><summary>What is an off-market deal?</summary><p>A sale that happens without a public listing. The owner and a buyer are introduced directly, usually through an agent who has done the research and made the call.</p></details>
<details><summary>What are creative terms?</summary><p>Anything beyond cash or a standard bank loan. The most common are seller carry and contract for deed, where the seller finances part or all of the price. <a href="/blog/contract-for-deed-minnesota/">Here is how contract for deed works.</a></p></details>
<details><summary>Do you work with first-time investors?</summary><p>Yes. We start with what you can put down and what return you need, then look at real buildings against those numbers.</p></details>
<details><summary>I own a building. Can we talk without listing it?</summary><p>Yes. I'll give you a value range and walk through your options. Nothing is public unless you decide it should be.</p></details>
</div>
</div></section>
<section class="rule"><div class="wrap section stack center">
<h2>Have a building or a deal in mind?</h2>
<p class="soft">Email <a href="mailto:Nazar@ts-re.com">Nazar@ts-re.com</a> with the address and what you know, or call {PHONE}.</p>
</div></section>
"""
    page("/commercial/", "Commercial and Multifamily Real Estate in Minnesota | Nazar Orishchin",
         "Apartments, mixed use, retail, strip centers, warehouses, churches and special-use property in Minnesota. Off-market deals, underwriting and creative terms.", com, active="/commercial/")

    # ---------- reviews ----------
    allq = "".join(quote(n, t, "quote long") for n, r, t in REVIEWS)
    rev = f"""
<div class="wrap page-hero stack lg">
<p class="label">Reviews</p><h1>In my clients' own words.</h1>
<p class="lead">These are Google reviews, copied as written. Nothing edited, nothing invented.</p>
</div>
<section class="rule"><div class="wrap section tight stats">
<div class="stat"><b>5.0</b><span>Average Google rating</span></div>
<div class="stat"><b>26</b><span>Google reviews across two office profiles</span></div>
<div class="stat"><b>100+</b><span>Transactions closed since 2022</span></div>
<div class="stat"><b>Nov 2026</b><span>Rating and count as of Nov 12, 2026</span></div>
</div></section>
<section class="rule"><div class="wrap section"><div class="masonry">{allq}</div></div></section>
<section class="rule"><div class="wrap section stack center">
<h2>Want to be the next one?</h2>
<p class="soft">Call or text {PHONE} and tell me what you're trying to do.</p>
</div></section>
"""
    page("/reviews/", "Client Reviews | Nazar Orishchin, Real Estate Agent",
         "Google reviews from buyers, sellers and investors who worked with Nazar Orishchin of RE/MAX Results. 5.0 average across 26 reviews as of November 2026.", rev, active="/reviews/")

    # ---------- ukrainian ----------
    uk = f"""
<div class="wrap page-hero split">
<div class="stack lg"><p class="label">Українською</p><h1>Назар Оріщин, ріелтор у Міннесоті.</h1>
<p class="lead">Допомагаю купити, продати та інвестувати в нерухомість у Міннесоті. Пояснюю кожен крок українською, без поспіху і без тиску.</p>
<div><a class="btn primary" href="tel:+19528469173">Телефонуйте або пишіть: (952) 846-9173</a></div></div>
<div class="photo"><img src="/images/nazar-smiling.jpg" alt="Назар Оріщин" width="800" height="1200"></div>
</div>
<section class="rule"><div class="wrap section split">
<div class="stack"><h2>Як купити будинок у Міннесоті</h2><p class="soft">Шість кроків по порядку.</p></div>
<ol class="steps">
<li><div><h3>Розмова і план</h3><p>Обговорюємо ваш бюджет, міста, які вам підходять, і терміни.</p></div></li>
<li><div><h3>Попереднє схвалення кредиту</h3><p>Кредитор (lender) рахує, яку суму ви можете позичити. Це називається pre-approval. Я поясню, які документи потрібні.</p></div></li>
<li><div><h3>Пошук і покази</h3><p>Дивимося будинки разом. Я звертаю увагу на дах, опалення, сліди води та все, що коштуватиме грошей пізніше.</p></div></li>
<li><div><h3>Пропозиція</h3><p>Готую пропозицію (offer) на основі реальних продажів поруч і пояснюю кожен пункт договору.</p></div></li>
<li><div><h3>Інспекція</h3><p>Інспектор перевіряє будинок. Разом читаємо звіт і вирішуємо, що просити у продавця.</p></div></li>
<li><div><h3>Закриття угоди</h3><p>Підписуєте документи в title company і отримуєте ключі. Я поруч і перекладаю.</p></div></li>
</ol>
</div></section>
<section class="rule"><div class="wrap section stack lg">
<h2>Чим я можу допомогти</h2>
<div class="grid g3">
<div class="card"><h3>Купівля</h3><p class="soft">Перший будинок чи наступний. Пояснюю процес, документи та витрати зрозумілою мовою.</p></div>
<div class="card"><h3>Продаж</h3><p class="soft">Чесна ціна на основі ринку, підготовка будинку та професійні фото.</p></div>
<div class="card"><h3>Інвестиції та бізнес</h3><p class="soft">Квартирні будинки, склади, приміщення для бізнесу, церкви. Працюю також з contract for deed.</p></div>
</div>
<p class="soft">Я народився в Україні й виріс у Міннесоті. За освітою інженер, тому уважно рахую цифри й перевіряю стан будинку.</p>
</div></section>
<section class="rule"><div class="wrap section stack center">
<h2>Маєте запитання?</h2>
<p class="soft">Телефон або SMS: {PHONE}. Email: <a href="mailto:Nazar@ts-re.com">Nazar@ts-re.com</a></p>
</div></section>
"""
    page("/uk/", "Назар Оріщин | Україномовний ріелтор у Міннесоті",
         "Україномовний ріелтор у Міннесоті. Купівля, продаж та інвестиції в нерухомість: Chaska, Chanhassen, Eden Prairie та вся Міннесота.", uk, active="/uk/", lang="uk")

    # ---------- blog ----------
    cards = "".join(
        f'<a class="card post-card" href="/blog/{p["slug"]}/"><time datetime="{TODAY}">November 2026</time><h3>{p["title"]}</h3><p class="soft grow">{p["teaser"]}</p><span class="arrow">Read it</span></a>'
        for p in POSTS)
    blog = f"""
<div class="wrap page-hero stack lg"><p class="label">Blog</p><h1>Practical notes on buying, selling and investing in Minnesota.</h1>
<p class="lead">Short posts from deals I've worked. For weekly market numbers, get The Nazar Note.</p></div>
<section class="rule"><div class="wrap section"><div class="grid g3">{cards}</div></div></section>
{newsletter()}
"""
    page("/blog/", "Blog | Nazar Orishchin, Minnesota Real Estate",
         "Practical guides on buying, selling and investing in Minnesota real estate from agent Nazar Orishchin: inspections, contract for deed, off-market deals and more.", blog, active="/blog/")
    for p in POSTS:
        pld = json.dumps({"@context": "https://schema.org", "@type": "BlogPosting", "headline": p["title"],
                          "datePublished": TODAY, "author": {"@type": "Person", "name": "Nazar Orishchin", "url": SITE + "/"},
                          "mainEntityOfPage": f'{SITE}/blog/{p["slug"]}/'})
        body = f"""
<article class="article">
<a class="arrow" href="/blog/" style="padding:0">All posts</a>
<p class="post-meta" style="margin-top:20px"><time datetime="{TODAY}">November 13, 2026</time> · Nazar Orishchin</p>
<h1>{p["title"]}</h1>
<p class="lead">{p["teaser"]}</p>
{p["body"]}
<div class="byline"><img src="/images/nazar-orishchin-about.jpg" alt="" width="64" height="64" loading="lazy"><p><b>Nazar Orishchin</b><br>Real estate agent, RE/MAX Results, Team Steady. {PHONE}</p></div>
</article>
{newsletter()}
"""
        page(f'/blog/{p["slug"]}/', f'{p["title"]} | Nazar Orishchin', p["desc"], body, active="/blog/",
             extra_head=f'<script type="application/ld+json">{pld}</script>\n')

    # ---------- 404, sitemap, robots ----------
    page("/404.html", "Page not found | Nazar Orishchin", "Page not found.",
         f'<div class="wrap section stack center"><h1>That page isn\'t here.</h1><p class="soft">Try the <a href="/">home page</a> or call {PHONE}.</p></div>')
    open("sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"<url><loc>{SITE}{u}</loc><lastmod>{TODAY}</lastmod></url>\n" for u in PAGES) + "</urlset>\n")
    open("robots.txt", "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    open(".nojekyll", "w").write("")
    print("built", len(PAGES), "pages")


if __name__ == "__main__":
    build()
