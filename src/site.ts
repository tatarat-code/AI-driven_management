// サイト全体で使う基本情報（ここを直せば全ページに反映される）
export const SITE = {
  name: '企業経営とAI',
  description:
    '財務会計を軸に、AIによる経営の変革（AX）を体系的に学ぶための講義教材サイトです。',
  lang: 'ja',
  owner: '山口大学大学院 技術経営研究科',
};

// サイト内の主なページ（ヘッダーとトップページの目次で共通に使う）
export const NAV = [
  { href: '/', label: 'トップ' },
  { href: '/overview/', label: '概要版' },
  { href: '/guidebook/', label: '詳細ガイドブック' },
  { href: '/syllabus/', label: 'シラバス' },
  { href: '/news/', label: '新着情報' },
  { href: '/about/', label: 'このサイトについて' },
];
