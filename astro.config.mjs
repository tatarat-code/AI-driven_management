// @ts-check
import { defineConfig } from 'astro/config';

// 静的サイトとして書き出す（Cloudflare Workers の静的アセットで配信）
export default defineConfig({
  // 公開URLが決まったら設定する（サイトマップや正規URLに使う）
  // site: 'https://example.com',
  output: 'static',
  trailingSlash: 'ignore',
  build: {
    format: 'directory',
  },
});
