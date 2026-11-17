// Runs after every build. Fails the build if a page breaks a site rule (see CLAUDE.md).
import { readFileSync, readdirSync, statSync, copyFileSync, existsSync } from "node:fs";
import { join } from "node:path";

const DIST = "dist";
const problems = [];
const warn = [];

function walk(dir) {
  return readdirSync(dir).flatMap((f) => {
    const p = join(dir, f);
    return statSync(p).isDirectory() ? walk(p) : [p];
  });
}

const files = walk(DIST);
const pages = files.filter((f) => f.endsWith(".html"));
const exists = new Set(files.map((f) => "/" + f.slice(DIST.length + 1)));
const titles = new Map();
const descs = new Map();

for (const f of pages) {
  const html = readFileSync(f, "utf8");
  const path = "/" + f.slice(DIST.length + 1).replace(/index\.html$/, "");
  const redirect = /http-equiv="refresh"/.test(html);
  const bad = (msg) => problems.push(`${path}: ${msg}`);

  // No phone number anywhere. Calendly replaces it.
  if (/846-?9173|9528469173|tel:/.test(html)) bad("phone number or tel: link found");
  if (redirect) continue;

  const visible = html.replace(/<script[\s\S]*?<\/script>/g, "").replace(/<style[\s\S]*?<\/style>/g, "");
  // No em dashes, except inside client reviews quoted exactly as written.
  const noQuotes = visible.replace(/<figure class="(quote|pull)[^"]*">[\s\S]*?<\/figure>/g, "");
  if (/[—–]|&mdash;|&ndash;/.test(noQuotes)) bad("em or en dash found");

  // Structured data must be valid JSON.
  for (const m of html.matchAll(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/g)) {
    try { JSON.parse(m[1]); } catch { bad("invalid JSON-LD structured data"); }
  }

  // One H1.
  const h1 = (visible.match(/<h1[\s>]/g) || []).length;
  if (h1 !== 1) bad(`${h1} H1 tags (need exactly 1)`);

  // Title and meta description: present, unique, description under 160 characters.
  const title = html.match(/<title>([^<]*)<\/title>/)?.[1];
  const desc = html.match(/<meta name="description" content="([^"]*)"/)?.[1]?.replace(/&#39;|&amp;|&quot;/g, "x");
  if (!title) bad("missing <title>");
  if (!desc) bad("missing meta description");
  if (desc && desc.length > 160 && !path.includes("404")) bad(`meta description is ${desc.length} characters`);
  if (title) { if (titles.has(title)) bad(`same title as ${titles.get(title)}`); titles.set(title, path); }
  if (desc && !path.includes("404")) { if (descs.has(desc)) bad(`same description as ${descs.get(desc)}`); descs.set(desc, path); }
  if (!path.includes("404") && !/<link rel="canonical"/.test(html)) bad("missing canonical link");
  if (!/og:image/.test(html)) bad("missing Open Graph image");

  // Brokerage and Equal Housing in the footer.
  if (!/RE\/MAX Results/.test(html)) bad("RE/MAX Results missing");
  if (!/Equal Housing Opportunity/.test(html)) bad("Equal Housing Opportunity statement missing");

  // Every image needs alt text.
  for (const img of visible.match(/<img\b[^>]*>/g) || []) {
    const alt = img.match(/\balt="([^"]*)"/);
    if (!alt || !alt[1].trim()) bad(`image without alt text: ${img.slice(0, 90)}`);
  }

  // No "best", "#1" or "top agent" claims in our own words.
  if (/\b(#1|number one|top agent|best agent|top-rated)\b/i.test(noQuotes)) bad("unverified ranking claim");

  // Unfinished copy should never go live.
  if (/TODO/.test(visible)) bad("TODO left in visible text");

  // Internal links must resolve.
  for (const m of visible.matchAll(/href="(\/[^"#?]*)/g)) {
    let u = m[1];
    if (u.endsWith("/")) u += "index.html";
    if (!exists.has(u) && !exists.has(u + "/index.html")) bad(`broken link ${m[1]}`);
  }
}

// Keep the old sitemap address working for search engines that already know it.
if (existsSync(join(DIST, "sitemap-0.xml"))) copyFileSync(join(DIST, "sitemap-0.xml"), join(DIST, "sitemap.xml"));

for (const w of warn) console.warn("warning:", w);
if (problems.length) {
  console.error(`\nBuild check failed (${problems.length}):\n- ` + problems.join("\n- "));
  process.exit(1);
}
console.log(`Build check passed: ${pages.length} pages.`);
