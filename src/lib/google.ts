// Pulls Nazar's live Google rating and review count at build time.
// Turn on by setting GOOGLE_PLACES_KEY (a GitHub secret) and GOOGLE_PLACE_IDS (comma-separated place IDs, one per
// Google Business Profile). Without them, the numbers in GOOGLE_RATING in site.ts are used.
// Only the rating, count and Maps link are used, with "Google" named as the source. The site rebuilds weekly so
// the numbers stay fresh.
import { GOOGLE_RATING } from "./site";

type Rating = { rating: number; count: number; checked: string; url: string; live: boolean };
let cached: Promise<Rating> | undefined;

async function load(): Promise<Rating> {
  const key = process.env.GOOGLE_PLACES_KEY;
  const ids = (process.env.GOOGLE_PLACE_IDS ?? "").split(",").map((s) => s.trim()).filter(Boolean);
  if (!key || !ids.length) return { ...GOOGLE_RATING, live: false };
  try {
    const places = await Promise.all(ids.map(async (id) => {
      const r = await fetch(`https://places.googleapis.com/v1/places/${id}`, {
        headers: { "X-Goog-Api-Key": key, "X-Goog-FieldMask": "rating,userRatingCount,googleMapsUri" },
      });
      if (!r.ok) throw new Error(`Places API ${r.status}`);
      return (await r.json()) as { rating?: number; userRatingCount?: number; googleMapsUri?: string };
    }));
    const count = places.reduce((n, p) => n + (p.userRatingCount ?? 0), 0);
    const rating = count ? places.reduce((s, p) => s + (p.rating ?? 0) * (p.userRatingCount ?? 0), 0) / count : GOOGLE_RATING.rating;
    const checked = new Date().toLocaleDateString("en-US", { month: "long", year: "numeric" });
    return { rating: Math.round(rating * 10) / 10, count, checked, url: places[0]?.googleMapsUri ?? "", live: true };
  } catch (e) {
    console.warn("Google rating: using saved numbers.", (e as Error).message);
    return { ...GOOGLE_RATING, live: false };
  }
}

export const getGoogleRating = () => (cached ??= load());
