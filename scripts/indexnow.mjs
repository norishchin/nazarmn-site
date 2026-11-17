// Tells Bing (and other IndexNow engines) about every page in the sitemap. Bing powers ChatGPT search and Copilot.
// Run after a publish: node scripts/indexnow.mjs
const KEY = "90291af56f7c5c39f78dd712a7ffa07f";
const HOST = "nazarmn.com";
const xml = await (await fetch(`https://${HOST}/sitemap.xml`)).text();
const urlList = [...xml.matchAll(/<loc>([^<]+)<\/loc>/g)].map((m) => m[1]);
const res = await fetch("https://api.indexnow.org/indexnow", {
  method: "POST",
  headers: { "Content-Type": "application/json; charset=utf-8" },
  body: JSON.stringify({ host: HOST, key: KEY, keyLocation: `https://${HOST}/${KEY}.txt`, urlList }),
});
console.log(`IndexNow: sent ${urlList.length} URLs, response ${res.status}`);
