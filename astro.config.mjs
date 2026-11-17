import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";

// Pages that only redirect somewhere else stay out of the sitemap.
const SKIP = ["/book/", "/search/", "/404"];

export default defineConfig({
  site: "https://nazarmn.com",
  trailingSlash: "always",
  build: { format: "directory" },
  integrations: [
    sitemap({
      filter: (page) => !SKIP.some((s) => page.includes(s)),
      i18n: { defaultLocale: "en", locales: { en: "en-US", uk: "uk-UA" } },
      serialize: (item) => ({ ...item, lastmod: new Date().toISOString().slice(0, 10) }),
    }),
  ],
});
