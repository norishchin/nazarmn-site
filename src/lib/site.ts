// Shared facts and labels for nazarmn.com. Change a fact here and it updates everywhere.

export const SITE = "https://nazarmn.com";
export const BOOK = "https://calendly.com/nazar-ts-re/call"; // 15-minute call
export const SEARCH = "https://nazarorishchin.teamsteadyrealestate.com/listing";
export const TEAM_STEADY = "https://nazarorishchin.teamsteadyrealestate.com";
export const NOTE = "https://news.nazarmn.com/";
export const EMAIL = "Nazar@ts-re.com";
// Cloudflare Web Analytics (free, no cookies). Paste the site token here to turn it on. Empty = off.
export const ANALYTICS_TOKEN = "db540cefe8bf46ccbb61d3dce5e93806";
export const LICENSE = "40776361";
export const OFFICE = {
  street: "11200 W 78th St",
  city: "Eden Prairie",
  region: "MN",
  zip: "55344",
};
export const SOCIAL = {
  facebook: "https://www.facebook.com/NazarOrishchinRealEstate",
  instagram: "https://instagram.com/nazar_realtor_mn",
  linkedin: "https://linkedin.com/in/nazar-orishchin",
  zillow: "https://www.zillow.com/profile/NazarOrishchin",
};
export const TOWNS = [
  "Chaska", "Chanhassen", "Victoria", "Eden Prairie", "Hopkins", "Savage",
  "Shakopee", "Burnsville", "Prior Lake", "Plymouth", "Maple Grove",
];

// Team record. Always shown as TEAM results, with source and date. Nazar's own line stays "100+ transactions closed since 2022".
export const TEAM = {
  realtrends: {
    url: "https://www.realtrends.com/team-profile/team-steady-minnesota-remax-results/",
    year: 2025, sides: 364, volume: "$166.63M", volumeM: 166.63, mnRank: 2, cityRank: 1, city: "Minneapolis", checked: "November 2026",
  },
  zillow: {
    url: "https://www.zillow.com/profile/TeamSteady",
    rating: 5.0, reviews: 698, totalSales: 2907, last12: 341, checked: "November 18, 2026",
  },
};

// Nazar's own Google rating. Replaced automatically at build time when Google Places is set up (see src/lib/google.ts).
export const GOOGLE_RATING = { rating: 5.0, count: 26, checked: "November 2026", url: "" };

export type Lang = "en" | "uk";

export const UI = {
  en: {
    bs: "Buy & sell", buy: "Buy a home", buy_s: "Process, costs and first steps",
    sell: "Sell your home", sell_s: "Pricing, prep and marketing",
    invest: "Invest", guides: "Guides", about: "About", search: "Search homes", reviews: "Reviews",
    book: "Book a call", f_site: "Site", f_else: "Elsewhere", f_buy: "Buy a home", f_sell: "Sell a home",
    f_inv: "Invest and commercial", f_ts: "Team Steady site",
    f_rights: "Each office independently owned and operated. Equal Housing Opportunity.",
    f_lic: `RE/MAX Results · Team Steady · Minnesota license #${LICENSE}`,
    next: "Next step", email_or: `Or email ${EMAIL}`, book_btn: "Book a 15-min call",
    read: "Read it", mins: "min read", all: "All guides", keep: "Keep reading",
    byline: "Real estate agent, RE/MAX Results, Team Steady.",
    ns_head: "Have a move or a property in mind?",
    ns_text: "Book 15 minutes and we'll work out the next step. No pressure, and you'll leave with a plan.",
    menu: "Open menu", short: "Short answer", other: "Українська",
  },
  uk: {
    bs: "Купівля і продаж", buy: "Купити будинок", buy_s: "Процес, витрати, перші кроки",
    sell: "Продати будинок", sell_s: "Ціна, підготовка, маркетинг",
    invest: "Інвестиції", guides: "Поради", about: "Про мене", search: "Пошук будинків", reviews: "Відгуки",
    book: "Запис на дзвінок", f_site: "Сайт", f_else: "Також", f_buy: "Купівля", f_sell: "Продаж",
    f_inv: "Інвестиції та комерційна нерухомість", f_ts: "Сайт Team Steady",
    f_rights: "Кожен офіс RE/MAX є незалежним. Equal Housing Opportunity.",
    f_lic: `RE/MAX Results · Team Steady · ліцензія Міннесоти #${LICENSE}`,
    next: "Наступний крок", email_or: `Або напишіть на ${EMAIL}`, book_btn: "Запишіться на 15-хвилинну розмову",
    read: "Читати", mins: "хв читання", all: "Усі поради", keep: "Читайте також",
    byline: "Агент з нерухомості, RE/MAX Results, Team Steady.",
    ns_head: "Плануєте переїзд чи маєте об'єкт на прикметі?",
    ns_text: "Запишіться на 15 хвилин, і ми визначимо наступний крок. Без тиску, і ви матимете план.",
    menu: "Відкрити меню", short: "Коротка відповідь", other: "English",
  },
} as const;

export const CAT_UK: Record<string, string> = {
  "Start here": "З чого почати", Buying: "Купівля", Selling: "Продаж", Investing: "Інвестиції", Guide: "Поради",
};

// English pages that have a Ukrainian twin. Blog posts are added from the blog-uk collection.
export const UK_PAGES = new Set(["/", "/buy/", "/sell/", "/commercial/", "/blog/", "/about/"]);

/** Ukrainian path for an English path, if it exists. */
export function ukPath(path: string, ukSlugs: Set<string>): string | null {
  if (UK_PAGES.has(path)) return path === "/" ? "/uk/" : "/uk" + path;
  const m = path.match(/^\/blog\/([^/]+)\/$/);
  if (m && ukSlugs.has(m[1])) return "/uk" + path;
  return null;
}

/** Localize an internal link for the current language. */
export function L(lang: Lang, href: string): string {
  if (lang !== "uk" || !href.startsWith("/")) return href;
  if (UK_PAGES.has(href)) return href === "/" ? "/uk/" : "/uk" + href;
  return href;
}

export function fmtDate(d: Date, lang: Lang): string {
  if (lang === "uk") {
    const m = ["січня", "лютого", "березня", "квітня", "травня", "червня", "липня", "серпня", "вересня", "жовтня", "листопада", "грудня"];
    return `${d.getUTCDate()} ${m[d.getUTCMonth()]} ${d.getUTCFullYear()}`;
  }
  return d.toLocaleDateString("en-US", { month: "long", day: "numeric", year: "numeric", timeZone: "UTC" });
}

export function readMins(text: string): number {
  return Math.max(2, Math.round(text.replace(/<[^>]+>/g, " ").split(/\s+/).filter(Boolean).length / 230));
}

export const agentSchema = (extra: Record<string, unknown> = {}) => ({
  "@context": "https://schema.org",
  "@type": "RealEstateAgent",
  "@id": SITE + "/#agent",
  name: "Nazar Orishchin",
  url: SITE + "/",
  image: SITE + "/images/nazar-orishchin.jpg",
  email: EMAIL,
  knowsLanguage: ["en", "uk", "ru"],
  address: {
    "@type": "PostalAddress", streetAddress: OFFICE.street, addressLocality: OFFICE.city,
    addressRegion: OFFICE.region, postalCode: OFFICE.zip, addressCountry: "US",
  },
  areaServed: [...TOWNS, "Minnesota"],
  parentOrganization: { "@type": "Organization", name: "RE/MAX Results" },
  sameAs: [SOCIAL.facebook, SOCIAL.instagram, SOCIAL.linkedin, SOCIAL.zillow, TEAM_STEADY],
  ...extra,
});
