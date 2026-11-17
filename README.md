# nazarmn.com

Nazar Orishchin's website. Built with [Astro](https://astro.build) and published to GitHub Pages automatically whenever `main` changes.

## Everyday tasks

**Preview locally**

```
npm install
npm run dev
```

Then open http://localhost:4321.

**Add a blog post**

1. Copy any file in `src/content/blog/` and rename it. The file name becomes the web address (`my-post.md` → `/blog/my-post/`).
2. Fill in the top section (title, description under 160 characters, teaser, short answer, date, category, thumbnail).
3. Write the post in plain Markdown below it. End with one call to action.
4. Add a thumbnail: put the file name in `THUMBS` in `scripts/make-thumbs.mjs`, pick a drawing, and run `node scripts/make-thumbs.mjs`.
5. Optional Ukrainian version: same file name in `src/content/blog-uk/`.

**Change a fact everywhere** (email, license, booking link, towns): `src/lib/site.ts`.

**Town pages**: `src/data/towns.ts`. Market numbers must name and link their source with a date.

## Checks

`npm run build` also runs `scripts/check-build.mjs`, which stops the build if any page has a phone number, an em dash, a missing title or description, a description over 160 characters, more or fewer than one H1, an image without alt text, a broken internal link, or a missing RE/MAX Results or Equal Housing Opportunity line.

## Layout

- `src/pages/` one file per page (Ukrainian pages under `uk/`)
- `src/content/` blog posts in Markdown
- `src/layouts/Base.astro` header, footer and search tags shared by every page
- `src/components/` reusable pieces (post cards, call box, newsletter strip)
- `src/styles/site.css` all styles
- `public/` files served as-is (favicons, share images, thumbnails, CNAME)
