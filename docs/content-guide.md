# 教材と新着情報の追加・更新の手引き

## 1. 教材を公開する（概要版・詳細ガイドブック）

1. Claude Docs の該当タブを Markdown で書き出す
2. `src/content/guidebook/vol01.md`（概要版なら `src/content/overview/ch01.md` など）の本文を、書き出した内容に置き換える
   - 先頭の `---` で囲まれた部分（フロントマター）は残す
   - 本文の最初の大見出し（タイトル）は、ページ側で表示するので消す
3. PDF があれば `public/pdf/guidebook/vol01.pdf` に置き、フロントマターの `pdf:` の行の `#` を外す
4. `status: draft` を `status: published` に変える
5. 新着情報を1件足す（下の 3.）
6. `npm run dev` で表示を確かめてから、GitHub に push する

### フロントマターの項目

| 項目 | 必須 | 内容 |
|---|---|---|
| `title` | ○ | 巻名・章名（巻番号や「第○章」は guidebook では付けない） |
| `volume` | ○（ガイドブック） | 巻番号 1〜15 |
| `order` | ○（概要版） | 並び順。はじめに=0、第n章=n、付録=99 |
| `summary` | | 一覧や検索結果に出す短い説明 |
| `pdf` | | PDFのパス（例：`/pdf/guidebook/vol01.pdf`） |
| `updated` | | 最終更新日（例：`2026-12-01`） |
| `status` | | `draft`（準備中）または `published`（公開）。省略すると `draft` |

## 2. ファイル名の決まり

- 英数字と `-` だけを使う（URL になるため）
- 詳細ガイドブック：`vol01.md`〜`vol15.md`
- 概要版：`intro.md`、`ch01.md`〜`ch15.md`、`appendix.md`
- 新着情報：`YYYY-MM-DD-内容を表す英語.md`（例：`2026-12-01-vol01.md`）

## 3. 新着情報を足す

`src/content/news/` に1件1ファイルで置く。トップページには新しい順に5件出る。

```markdown
---
title: 詳細ガイドブック第1巻を公開しました
date: 2026-12-01
link: /guidebook/vol01/
---

第1巻『AXの全体像と自社診断』を公開しました。
```

## 4. 公開前の確認

- 【要更新】【架空の例】の表示が教材のとおり残っているか
- 他の巻への参照（「第○巻『正式名』」）が正しいか
- `npm run build` がエラーなく終わるか（フロントマターの書き間違いはここで止まる）
