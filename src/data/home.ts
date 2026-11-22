// トップページ（インフォグラフィックLP）で使うデータ
// 数値は講義の設計と教材の検算スクリプトの値だけを使う

// 講義の数字（帯）
export const STATS = [
  { value: '15', unit: '回', note: '90分×15回・2単位。木曜日に1日2コマ' },
  { value: '2', unit: '層の教材', note: '概要版（15章）と詳細ガイドブック（15巻）' },
  { value: '3', unit: '社の模擬企業', note: '規模も業種も違う3社で、同じ型を当てはめる' },
  { value: '1', unit: 'つの成果物', note: '最終課題「AX Transformation Blueprint（AX計画書）」' },
];

// AX成熟度の5段階（背景色・文字色・高さ）
export const MATURITY = [
  { level: 1, name: '個人利用', bg: '#E3EAF2', fg: '#14202E', num: '#1B3A5C', h: 140 },
  { level: 2, name: '業務組込み', bg: '#C9D6E4', fg: '#14202E', num: '#1B3A5C', h: 180 },
  { level: 3, name: '半自律', bg: '#8FA8C3', fg: '#0E2238', num: '#0E2238', h: 220 },
  { level: 4, name: '監督付き自律', bg: '#3F6189', fg: '#FFFFFF', num: '#FFFFFF', h: 260 },
  { level: 5, name: '業務の再設計', bg: '#1B3A5C', fg: '#FFFFFF', num: '#FFFFFF', h: 300 },
];

// 15章の路線図：章番号（order）で各路線に割り当てる
export const LINES = [
  { name: '基礎線', color: '#1B3A5C', chapters: [1, 2, 3] },
  { name: '財務ハブ線', color: '#B4531B', chapters: [4, 5, 6, 7] },
  { name: '機能別線', color: '#1F6B5E', chapters: [8, 9, 10] },
  { name: '設計・統制線', color: '#5B4596', chapters: [11, 12, 13] },
  { name: '実践線', color: '#14202E', chapters: [14, 15] },
];
export const TRANSFER_CHAPTER = 4; // 乗換駅
export const TERMINAL_CHAPTER = 15; // 終点

// 模擬企業3社（架空）のROICの推移（3時点、%）
export const COMPANIES = [
  { name: 'A社', profile: 'B2B製造・商社／120名', roic: [8.4, 6.3, 4.4], cause: '回転率（運転資本）' },
  { name: 'B社', profile: '食品加工・卸／20名', roic: [9.2, 6.8, 4.3], cause: '粗利率' },
  { name: 'C社', profile: '金属部品加工（地域の製造業）／45名', roic: [11.8, 7.2, 3.9], cause: '稼働率と固定費' },
];
export const ROIC_SCALE_MAX = 12; // 棒の長さの基準（%）
