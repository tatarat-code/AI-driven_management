# 企業経営とAI（講義教材サイト）

講義「企業経営とAI」（山口大学大学院 技術経営研究科、2027年度前期）の教材を公開するWebサイトのリポジトリです。

- 仕組み：[Astro](https://astro.build/)（静的サイト）
- 公開先：Cloudflare Workers（静的アセット）。GitHub に push すると自動で公開
- 教材：概要版（はじめに・全15章・付録）、詳細ガイドブック（全15巻）、シラバス。本文はWebページ、あわせてPDFも配布

## フォルダの構成

```
AI-driven_management/
├─ src/
│  ├─ content/            ← 教材や記事の本文（Markdown）。ふだん編集するのはここ
│  │  ├─ overview/        概要版（intro, ch01〜ch15, appendix）
│  │  ├─ guidebook/       詳細ガイドブック（vol01〜vol15）
│  │  ├─ news/            新着情報（1件1ファイル）
│  │  └─ pages/           単独ページ（syllabus, about）
│  ├─ pages/              ページの型（URLの決まり方）
│  ├─ layouts/            全ページ共通の枠
│  ├─ components/         ヘッダー・フッターなどの部品
│  ├─ styles/global.css   見た目（仮のもの。デザイン確定後に差し替え）
│  ├─ site.ts             サイト名・説明・メニュー
│  └─ content.config.ts   教材ファイルの項目（タイトル、巻番号など）の決まり
├─ public/
│  ├─ pdf/overview/       概要版のPDF
│  ├─ pdf/guidebook/      詳細ガイドブックのPDF
│  └─ favicon.svg
├─ docs/                  運用の手引き（このサイトには表示されない）
├─ scripts/               変換などの補助スクリプト（今後追加）
├─ astro.config.mjs       Astroの設定
├─ wrangler.jsonc         Cloudflareの設定
└─ package.json
```

## URLの一覧

| ページ | URL | 元になるファイル |
|---|---|---|
| トップ（概要・サイト内目次・新着情報） | `/` | `src/pages/index.astro` |
| 概要版の一覧／各章 | `/overview/`、`/overview/ch01/` など | `src/content/overview/*.md` |
| 詳細ガイドブックの一覧／各巻 | `/guidebook/`、`/guidebook/vol01/` など | `src/content/guidebook/*.md` |
| シラバス | `/syllabus/` | `src/content/pages/syllabus.md` |
| このサイトについて | `/about/` | `src/content/pages/about.md` |
| 新着情報 | `/news/` | `src/content/news/*.md` |

教材のファイルは `status: draft` の間は一覧に「準備中」と出るだけで、本文のページは作られません。`status: published` にすると公開されます。

## はじめての準備（Windows）

1. Node.js 22 以上と Git を入れる
2. このフォルダで依存パッケージを入れる

   ```powershell
   cd C:\Users\naoki\Claude\Projects\AI-driven_management
   npm install
   ```

3. 手元で確認する

   ```powershell
   npm run dev
   ```

   表示された `http://localhost:4321/` をブラウザで開く。

## よく使うコマンド

| コマンド | 内容 |
|---|---|
| `npm run dev` | 手元で確認（保存するとすぐ反映） |
| `npm run build` | 公開用のファイルを `dist/` に作る |
| `npm run preview` | 作ったファイルを Cloudflare と同じ仕組みで手元確認 |
| `npm run deploy` | 手元から直接公開（ふだんは GitHub 連携で自動公開するので使わない） |

## 手引き

- 教材や新着情報の追加・更新：[docs/content-guide.md](docs/content-guide.md)
- GitHub と Cloudflare の設定、公開の流れ：[docs/deploy-cloudflare.md](docs/deploy-cloudflare.md)
