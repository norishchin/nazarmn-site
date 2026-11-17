import type { APIRoute } from "astro";
import { getPosts } from "../lib/posts";
import { SITE } from "../lib/site";

const esc = (s: string) => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

export const GET: APIRoute = async () => {
  const posts = (await getPosts()).sort((a, b) => b.data.date.getTime() - a.data.date.getTime());
  const items = posts.map((p) => `<item><title>${esc(p.data.title)}</title><link>${SITE}/blog/${p.id}/</link><guid>${SITE}/blog/${p.id}/</guid><pubDate>${p.data.date.toUTCString()}</pubDate><description>${esc(p.data.description)}</description></item>`).join("");
  return new Response(`<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>Nazar Orishchin: Minnesota real estate guides</title><link>${SITE}/blog/</link><description>Plain guides to buying, selling and investing in Minnesota.</description>${items}</channel></rss>`,
    { headers: { "Content-Type": "application/rss+xml; charset=utf-8" } });
};
