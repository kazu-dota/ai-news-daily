# AI News Daily 🤖🗞

毎日の生成AI関連ニュースを Claude Code が自動収集・要約してまとめる日本語アーカイブ。

## 仕組み

- **実行基盤**: Claude Code のルーティン (cron) が毎朝 **8:00 JST** に起動
- **対象ソース**: 企業/モデル発表、技術コミュニティ、メディア記事、話題の研究論文 (詳細: [`sources.yaml`](./sources.yaml))
- **出力先**:
  - `summaries/YYYY/MM/YYYY-MM-DD.md` … 日次アーカイブ (本体)
  - GitHub Discussions「Daily News」カテゴリ … 当日告知
- **公開**: GitHub Pages で `summaries/` をブログ化 (準備中)

## 最新のサマリー

> 自動更新されるセクション。最新7日分へのリンクを表示。

<!-- LATEST:BEGIN -->
- [2026-05-10](summaries/2026/05/2026-05-10.md) — Anthropic $900B 調達ラウンド最終局面 / OpenAI GPT-Realtime-2 音声3モデル / Gemini 3.1 Flash-Lite GA / Claude Managed Agents 並列20エージェント追加
<!-- LATEST:END -->

過去ログは [`summaries/`](./summaries/) ディレクトリを参照。

## このリポジトリの方針

本リポジトリの要約は、各ニュース・記事・論文の **事実情報を独自に再構成**したものです。
詳細・全文は必ず元記事をご参照ください。

- 直接引用は最小限 (1引用あたり15語または30字以内) で、必ず引用符と元記事リンクを付けています
- ペイウォール記事の本文要約は行わず、発表事実のリンク紹介のみとしています
- 画像・図表の転載は行いません
- 全文翻訳・詳細翻訳は行いません

## 著作権者・関係者の方へ

掲載に関するご懸念や削除のご希望がある場合は、以下からお知らせください。確認のうえ速やかに対応いたします。

- [Issue を作成](https://github.com/kazu-dota/ai-news-daily/issues/new?template=copyright-takedown.md) (テンプレートあり)
- もしくはリポジトリオーナーまでメール

## 構成

```
ai-news-daily/
├── README.md            ← このファイル
├── CLAUDE.md            ← ルーティンへの行動指針
├── sources.yaml         ← 監視対象ソース一覧
├── summaries/           ← 日次サマリー (YYYY/MM/YYYY-MM-DD.md)
├── docs/                ← GitHub Pages 用 (Jekyll)
└── .github/ISSUE_TEMPLATE/
```

## 開発フロー

このリポジトリは2つのブランチで運用しています:

| ブランチ | 用途 | 直接 push |
|---|---|---|
| `main` | **実行用 (本番)**。日次 routine がここに直接 push します | routine のみ |
| `dev`  | **開発用**。`CLAUDE.md` / `sources.yaml` / `docs/` などの修正は dev で行い、PR で main にマージ | 開発者 |

### 変更を入れる手順

1. `git checkout dev && git pull origin dev`
2. 必要な編集 (`CLAUDE.md` / `sources.yaml` / `docs/` など)
3. `git commit -m "..." && git push origin dev`
4. PR を作成して main にマージ: `gh pr create --base main --head dev`
5. routine の次回実行 (毎朝 8:00 JST) から反映。即時試したい場合は [routine 管理UI](https://claude.ai/code/routines) で **Run now**

### routine 自体の改修について

- routine への恒久的な指示書は **`CLAUDE.md`** にまとめてあり、毎回 routine が起動時に読みます。指針を変えたい場合は `CLAUDE.md` を更新すれば、次回実行から反映されます
- routine の **schedule・モデル・許可ツール・MCP接続** の変更は claude.ai の routine 管理UIで行います (リポジトリ側のファイルでは管理しません)

## ライセンス

- リポジトリ内のコード・設定: [MIT License](./LICENSE)
- サマリーコンテンツ: 各記事の事実情報を独自にまとめたもので、引用部分の権利は元の権利者に帰属します
