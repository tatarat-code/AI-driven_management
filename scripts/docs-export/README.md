# Claude Docs からの書き出し手順（教材本文の更新用）

Claude Docs の教材を、このサイトのコンテンツ（`src/content/`）に変換するための補助スクリプトです。Claude との作業で使います。

| ファイル | 役割 |
| --- | --- |
| `decode.py` | Claude Docs の書き出し結果（JSON、base64）を元のファイルに戻す |
| `convert.py` | docx または markdown を、サイトの md（frontmatter 付き、`status: published`）に変換する。図は `public/images/<collection>/<id>-figN.png` に置く |
| `pdffigs.sh` | PDF 書き出しから図（埋め込みウィジェットの画像）を取り出す（詳細ガイドブック用） |
| `fixlinks.py` | claude.ai の成果物リンクを、サイト内リンク（`/guidebook/volNN/` など）に置き換える |

## 流れ

1. 概要版の各章：Claude Docs から **docx** で書き出す（図の画像が入る）→ `convert.py <docx> overview chNN`
2. 詳細ガイドブックの各巻：**markdown**（本文）と **PDF**（図）で書き出す → `pdffigs.sh` → `convert.py <md> guidebook volNN`
3. `fixlinks.py src/content/*/*.md` → `npx astro build` で確認

注意：図の書き出しには回数の制限があります（目安：約1分半に5〜6枚）。超えると図が文字のまま書き出されるので、時間を置いて書き出し直します。
