import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

// One Markdown file per post. The file name is the URL: src/content/blog/my-post.md -> /blog/my-post/
const post = z.object({
  title: z.string(),
  description: z.string().max(160, "Meta description must be under 160 characters"),
  teaser: z.string(),
  answer: z.string().optional(), // "Short answer" box at the top, 1 to 3 plain sentences
  date: z.coerce.date(),
  updated: z.coerce.date().optional(),
  category: z.enum(["Start here", "Buying", "Selling", "Investing", "Guide"]),
  town: z.string().optional(), // city or area tag, when the post is about one place
  thumbnail: z.string(), // /images/thumbs/<slug>.png
  thumbnailAlt: z.string(),
  order: z.number().optional(), // lower shows first on the Guides page; new posts can leave it out
  draft: z.boolean().default(false),
});

export const collections = {
  blog: defineCollection({ loader: glob({ pattern: "*.md", base: "./src/content/blog" }), schema: post }),
  // Ukrainian versions. Same file name as the English post. Date, category and thumbnail come from the English post.
  blogUk: defineCollection({
    loader: glob({ pattern: "*.md", base: "./src/content/blog-uk" }),
    schema: z.object({
      title: z.string(),
      description: z.string().max(160),
      teaser: z.string(),
      answer: z.string().optional(),
    }),
  }),
};
