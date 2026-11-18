import { getCollection, type CollectionEntry } from "astro:content";
import { readMins } from "./site";

export type Post = CollectionEntry<"blog"> & { mins: number; uk?: CollectionEntry<"blogUk"> & { mins: number } };

/** All published posts, in Guides-page order: pinned order first, then newest first. */
export async function getPosts(): Promise<Post[]> {
  const uk = new Map((await getCollection("blogUk")).map((p) => [p.id, p]));
  const posts = (await getCollection("blog", (p) => !p.data.draft)).map((p) => {
    const u = uk.get(p.id);
    return {
      ...p,
      mins: readMins(p.body ?? ""),
      uk: u ? { ...u, mins: readMins(u.body ?? "") } : undefined,
    } as Post;
  });
  return posts.sort((a, b) =>
    (a.data.order ?? 999) - (b.data.order ?? 999) || b.data.date.getTime() - a.data.date.getTime());
}

export function related(all: Post[], p: Post, n = 2): Post[] {
  const same = all.filter((q) => q.id !== p.id && q.data.category === p.data.category);
  const rest = all.filter((q) => q.id !== p.id && q.data.category !== p.data.category);
  return [...same, ...rest].slice(0, n);
}
