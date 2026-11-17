// Makes blog thumbnails in one house style: a color for the topic and a simple line drawing for the post.
// Run: node scripts/make-thumbs.mjs
// New post? Add its file name to THUMBS below with one of the drawings in ICONS (or add a drawing), then run this.
import sharp from "sharp";
import { readFileSync, readdirSync, mkdirSync } from "node:fs";

const OUT = "public/images/thumbs";
const COLORS = { "Start here": "#1b6a85", Buying: "#0f1f33", Selling: "#7a4b32", Investing: "#24524a", Guide: "#3d4a5c" };
const LINE = "#f7f3ec";
const ACCENT = "#dcebef";

// Drawings on a 400 x 400 grid, line art only.
const ICONS = {
  checklist: `<rect x="95" y="60" width="210" height="280" rx="18"/><rect x="160" y="40" width="80" height="44" rx="10"/>
    <path d="M135 150l20 20 34-38M215 158h55M135 220l20 20 34-38M215 228h55M135 290h30M215 290h55"/>`,
  key: `<circle cx="140" cy="200" r="70"/><circle cx="140" cy="200" r="26"/><path d="M210 200h140M300 200v42M330 200v30"/>`,
  calendar: `<rect x="70" y="85" width="260" height="250" rx="18"/><path d="M70 145h260M135 60v50M265 60v50"/>
    <path d="M110 190h40M180 190h40M250 190h40M110 240h40M180 240h40M110 290h40M180 290h40"/><path d="M245 285l18 18 34-40"/>`,
  building: `<path d="M60 340V120l110-50v270M170 340V150h90v190"/><path d="M95 150h40M95 200h40M95 250h40M200 190h30M200 240h30"/>
    <path d="M40 340h320"/><path d="M290 340v-70M320 340v-110M350 340v-150" stroke="${ACCENT}"/>`,
  magnifier: `<path d="M70 210l100-85 100 85M95 190v120h150V190"/><path d="M150 310v-55h40v55"/>
    <circle cx="275" cy="175" r="62" stroke="${ACCENT}"/><path d="M320 220l50 50" stroke="${ACCENT}"/>`,
  contract: `<path d="M110 50h140l60 60v240H110z"/><path d="M250 50v60h60"/><path d="M150 180l50-40 50 40M162 170v50h76v-50"/>
    <path d="M145 290c20-30 35 20 55-5s30 15 55-10" stroke="${ACCENT}"/>`,
  phone: `<path d="M80 340V190h140v150M60 190h180l-20-50H80z"/><path d="M115 340v-70h45v70M175 240h30"/>
    <rect x="265" y="110" width="80" height="150" rx="14" stroke="${ACCENT}"/><path d="M295 240h20" stroke="${ACCENT}"/>`,
  camera: `<rect x="60" y="130" width="230" height="160" rx="18"/><path d="M120 130l20-30h70l20 30"/><circle cx="175" cy="210" r="48"/>
    <path d="M345 105c-45 10-65 55-48 100 46-6 68-50 48-100zM297 205l48-100" stroke="${ACCENT}"/>`,
};

ICONS.duplex = `<path d="M50 330V170l150-100 150 100v160z"/><path d="M200 70v260"/><path d="M90 230h60v60H90zM250 230h60v60h-60z"/>
    <circle cx="300" cy="120" r="22" stroke="${ACCENT}"/><path d="M322 120h40M348 120v18" stroke="${ACCENT}"/>`;

const THUMBS = {
  "your-first-step-before-buying-a-home": "checklist",
  "buying-your-first-home-in-minnesota": "key",
  "selling-your-home-what-the-first-30-days-look-like": "calendar",
  "which-investment-properties-make-sense": "building",
  "what-i-look-for-in-an-inspection-report": "magnifier",
  "contract-for-deed-minnesota": "contract",
  "how-off-market-commercial-deals-happen": "phone",
  "selling-in-spring-take-photos-in-fall": "camera",
  "buying-a-duplex-and-living-in-one-unit": "duplex",
};

function svg(category, icon) {
  const bg = COLORS[category] ?? COLORS.Guide;
  const dots = [];
  for (let x = 60; x < 520; x += 36) for (let y = 60; y < 600; y += 36) dots.push(`<circle cx="${x}" cy="${y}" r="2.2"/>`);
  return `<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
  <rect width="1200" height="630" fill="${bg}"/>
  <g fill="${LINE}" opacity=".14">${dots.join("")}</g>
  <circle cx="790" cy="315" r="250" fill="#000" opacity=".12"/>
  <g transform="translate(550 75) scale(1.2)" fill="none" stroke="${LINE}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round">${ICONS[icon]}</g>
</svg>`;
}

mkdirSync(OUT, { recursive: true });
const files = readdirSync("src/content/blog").filter((f) => f.endsWith(".md"));
for (const f of files) {
  const slug = f.replace(/\.md$/, "");
  const icon = THUMBS[slug];
  if (!icon) { console.warn(`No drawing set for ${slug}. Add it to THUMBS.`); continue; }
  const category = readFileSync(`src/content/blog/${f}`, "utf8").match(/^category:\s*"?([^"\n]+)"?/m)?.[1];
  const img = sharp(Buffer.from(svg(category, icon)));
  await img.clone().png({ compressionLevel: 9 }).toFile(`${OUT}/${slug}.png`);
  await img.clone().webp({ quality: 82 }).toFile(`${OUT}/${slug}-1200.webp`);
  await img.clone().resize(600).webp({ quality: 80 }).toFile(`${OUT}/${slug}-600.webp`);
  console.log("thumbnail", slug);
}
