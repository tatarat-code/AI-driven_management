import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

// 公開の状態：draft は一覧に「準備中」と表示し、本文ページは作らない
const status = z.enum(['draft', 'published']).default('draft');

// 詳細ガイドブック（全15巻）
const guidebook = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/guidebook' }),
  schema: z.object({
    title: z.string(),
    heading: z.string().optional(), // 本文ページの見出し（正式な巻名）。一覧では title を使う
    volume: z.number().int().min(1).max(15),
    summary: z.string().optional(),
    pdf: z.string().optional(), // 例：/pdf/guidebook/vol01.pdf
    updated: z.coerce.date().optional(),
    status,
  }),
});

// 概要版（はじめに・第1〜15章・付録）
const overview = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/overview' }),
  schema: z.object({
    title: z.string(),
    heading: z.string().optional(), // 本文ページの見出し（正式な章名）。一覧では title を使う
    order: z.number().int(), // 並び順：はじめに=0、第n章=n、付録=99
    summary: z.string().optional(),
    pdf: z.string().optional(),
    updated: z.coerce.date().optional(),
    status,
  }),
});

// 新着情報
const news = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/news' }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    summary: z.string().optional(),
    link: z.string().optional(), // 関連ページへのリンク（任意）
  }),
});

// 単独ページ（シラバス、このサイトについて など）
const pages = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/pages' }),
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
    updated: z.coerce.date().optional(),
  }),
});

export const collections = { guidebook, overview, news, pages };
