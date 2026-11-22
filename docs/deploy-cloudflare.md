# GitHub と Cloudflare での公開の手引き

公開は Cloudflare Workers（静的アセット）で行います。Cloudflare は新しいサイトには Pages ではなく Workers を勧めています。このサイトはすべて静的ページなので、Workers のプログラムは書かず、`dist/` のファイルをそのまま配信します（設定は `wrangler.jsonc`）。

## 1. 最初に1回だけ行うこと

### (1) Git の初期化と最初の記録

```powershell
cd C:\Users\naoki\Claude\Projects\AI-driven_management
git init -b main
git add .
git commit -m "リポジトリの骨組みを作成"
```

### (2) GitHub にリポジトリを作って push

1. GitHub で新しいリポジトリを作る（例：`AI-driven_management`。README などは追加しない）
2. 表示された手順に沿って push する

```powershell
git remote add origin https://github.com/〈アカウント名〉/AI-driven_management.git
git push -u origin main
```

### (3) Cloudflare で GitHub と連携

1. Cloudflare のダッシュボードで「Workers & Pages」→「作成」→「GitHub からインポート」を選ぶ
2. 上のリポジトリを選ぶ
3. 設定を確かめる
   - ビルドコマンド：`npm run build`
   - デプロイコマンド：`npx wrangler deploy`
   - プロジェクト名：`ai-driven-management`（`wrangler.jsonc` の `name` とそろえる）
4. 保存して最初の公開を行う。`〈名前〉.workers.dev` のURLで確認できる

### (4) 独自ドメイン（使う場合）

Workers の設定画面の「ドメインとルート」で追加する。決まったら `astro.config.mjs` の `site:` にそのURLを書く。

## 2. ふだんの流れ

1. 教材や新着情報を編集する（`docs/content-guide.md`）
2. `npm run dev` で確認する
3. 記録して push する

```powershell
git add .
git commit -m "第1巻を公開"
git push
```

push すると Cloudflare が自動でビルドし、数分で公開されます。

## 3. 下書きを確かめたいとき

`main` 以外のブランチに push すると、Cloudflare がプレビュー用のURLを作ります（ダッシュボードの設定による）。公開前の確認に使えます。
