# AI News Daily 🤖🗞

毎日の生成AI関連ニュースを Claude Code が自動収集・要約してまとめる日本語アーカイブ。

## 仕組み

- **実行基盤**: claude.ai の Routines (Anthropic クラウド側) で毎朝 **8:00 JST** (UTC 23:00) に起動
- **対象ソース**: 企業/モデル発表、技術コミュニティ、メディア記事、話題の研究論文 (詳細: [`sources.yaml`](./sources.yaml))
- **出力先**:
  - `summaries/YYYY/MM/YYYY-MM-DD.md` … 日次アーカイブ (人が読む本文)
  - `docs/data/items/YYYY-MM-DD.json` … 構造化された機械可読データ
  - `docs/data/index.json` … 全期間累積インデックス (UI が fetch する)
- **Web UI**: <https://kazu-dota.github.io/ai-news-daily/> で日付ナビ・vendor フィルタ・キーワード検索つきのアーカイブを閲覧可能
- **整合性**: routine も人間も `main` への直接 push は禁止。すべて PR + auto-merge で反映 (詳細は [`CLAUDE.md`](./CLAUDE.md))

## 最新のサマリー

> 自動更新されるセクション。最新7日分へのリンクを表示。

<!-- LATEST:BEGIN -->
- [2026-10-19](summaries/2026/10/2026-10-19.md) — **Anthropic: Public Benefit Fund 設立 (株式5%初期拠出、合計約20%を公益に)** / stablyai/orca ★100k 目前 (★96,571, +1,146) / **akitaonrails/ai-memory 新登場 (クロスエージェント長期記憶 Rust +513)** / **Graphify-Labs/graphify 新登場 (コードベース→ナレッジグラフ ★128k +592)** / **diegosouzapw/OmniRoute 新登場 (375プロバイダー対応 AIゲートウェイ +411)** / TauricResearch/TradingAgents 新登場 (マルチエージェント金融取引フレームワーク +242) — OpenAI/Google/Meta/Microsoft 本日アップデートなし
- [2026-10-18](summaries/2026/10/2026-10-18.md) — **[終幕] morluto/rea が10日連続首位ののちトレンド圏外へ (最終 ★290k)** / stablyai/orca ★100k 目前 (★95,354, +829) / debpalash/VoiceStudio 8回目 Trending ★73k突破 (+2,135) / **elie222/rakazo 初登場 (Grok Bot OSS 代替 TypeScript +146)** / xerj-org/xerj 続報 (+1,102) / affaan-m/ECC 続報 (+1,145) — 主要 vendor 本日アップデートなし
- [2026-10-17](summaries/2026/10/2026-10-17.md) — **Anthropic: METR に Tier 3「従業員同等アクセス」付与・承認不要で評価報告書公開可能に** / [続報 10日目] morluto/rea (+25,333, ★290K・300K目前) / **xerj-org/xerj 新登場 (AI エージェント向け検索エンジン Rust +1,647)** / **obra/superpowers 新登場 (★300K エージェントスキルフレームワーク +973)** / **affaan-m/ECC 新登場 (★281K AI コーディングエージェント最適化 +1,057)** / cursor/plugins 新登場 / google/artemis 新登場 (自然言語→Android 操作)
- [2026-10-15](summaries/2026/10/2026-10-15.md) — **Anthropic: シンガポール事務所開設 + 政府 MOU 締結** / **Anthropic: 2026年米中間選挙への選挙保護施策を詳報** / [続報 9日目] morluto/rea (+41,187, ★240K突破) / **ifixai-ai/iFixAi 新登場 (AI エージェント動作監査 OSS +2,143)** / stablyai/orca 新登場 (コーディングエージェント並列管理環境 +962) / vercel-labs/skills 新登場 (npx スキル管理ツール +732) / vxcontrol/pentagi 新登場 (自律型 AI ペンテストエージェント +1,070)
- [2026-10-14](summaries/2026/10/2026-10-14.md) — [続報] **morluto/rea が8日連続 TypeScript Trending 首位・単日 +54,706 stars で累計 ★205,437 (8日間累計 200k stars 超)** / **Alishahryar1/free-claude-code 新登場 (61プロバイダー×11コーディングエージェント統合 +1,591)** / **heygen-com/hyperframes 新登場 (エージェント向け HTML→動画フレームワーク +831)** / **tashfeenahmed/freellmapi 新登場 (34社フリー LLM OpenAI互換ルーター +786)** / debpalash/VoiceStudio 4日連続 (+2,277) — 主要 vendor 本日アップデートなし
- [2026-10-13](summaries/2026/10/2026-10-13.md) — [続報] **morluto/rea が7日連続グローバル Trending 首位・単日 +45,495 stars で週間最大サージ更新 (★154,288)** / **paperclipai/paperclip 新登場 (AI エージェント組織管理 OSS ★100,937 +652)** / **calesthio/OpenMontage 新登場 (エージェント動画制作 +737)** / **Microsoft Research: StudentSim (AI チューター向け生徒シミュレーション)** / OpenBMB/VoxCPM 新登場 (30言語 TTS Apache 2.0)
- [2026-10-12](summaries/2026/10/2026-10-12.md) — [続報] **morluto/rea が 100K stars 突破・6日連続グローバル Trending 首位 (+25,585)** / **storytold/artcraft 新登場 (Rust 製 AI 創作エンジン、画像・動画・3D 統合 +2,956)** / lyogavin/airllm (4GB GPU で 70B LLM 動作、再浮上 +541) / MadsLorentzen/ai-job-search (Claude Code ベース求人支援 新規) — 主要 vendor 本日アップデートなし
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
├── CLAUDE.md            ← 開発者向けガイド (Claude Code が自動で読む)
├── ROUTINE.md           ← routine 用の実行仕様 (本番 / dev-test routine が読む)
├── sources.yaml         ← 監視対象ソース一覧
├── summaries/           ← 日次サマリー (YYYY/MM/YYYY-MM-DD.md, 人が読む)
├── docs/                ← GitHub Pages の配信ルート (Jekyll 不使用、.nojekyll)
│   ├── index.html       ← SPA UI (data/index.json を読み込んで表示)
│   ├── .nojekyll
│   └── data/
│       ├── index.json   ← 全期間累積インデックス
│       └── items/       ← 日付ごとの構造化データ
├── .claude/agents/      ← サブエージェント定義
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
4. **[事前検証] dev test routine を Run now で実行** (下記参照)
5. **`dev-test` ブランチ** に force push される当日 md をレビューし、期待どおりの出力であることを確認
   - レビュー URL: https://github.com/kazu-dota/ai-news-daily/tree/dev-test/summaries
6. PR を作成して main にマージ: `gh pr create --base main --head dev`
   - PR の対象は `dev` のみ。**`dev-test` ブランチは PR の対象外** なので、テスト出力が main に混入することはない
7. main の routine は翌朝 8:00 JST から新ルールで動作

### main の保護ルール (branch protection)

`main` は GitHub の branch protection で **PR 経由でしかマージできない** ように保護しています。

- ✅ Pull request required (PR 必須)
- ✅ Required approvals: **0 件** (auto-merge をシンプルに動かすため)
- ✅ Enforce for admins (admin も PR が必須 — 「うっかり直接 push」を防ぐ)
- ✅ Allow auto-merge (リポジトリ設定)
- ❌ Force push 禁止 / ブランチ削除禁止

**人間が直接 main に push しようとすると拒否されます**。すべての変更は PR 経由 (人間は dev → PR → main、本番 routine は `routine/auto-summary-...` → PR → main)。

### 事前検証用の dev test routine

`main` にマージする前に dev ブランチで実際にルーティンを動かすための**非アクティブな routine** を用意しています。

- **目的**: `sources.yaml` / `CLAUDE.md` などの変更を本番に入れる前に、dev の内容で出力を確認する
- **動作**:
  - 起動時に `git checkout -B dev-test origin/dev` で **dev のtipから `dev-test` ブランチを再作成** (既存履歴は破棄)
  - `sources.yaml` / `CLAUDE.md` は **dev の最新を参照**
  - 当日 md を生成し、`[dev-test]` 接頭辞付きの commit を **`dev-test` ブランチに force push**
  - dev / main には一切 push しない → **PR に混入しない・main に持ち込まれない**
  - README.md の LATEST セクションは更新しない・Discussion 投稿もしない
- **実行方法**: [claude.ai の Routines 画面](https://claude.ai/code/routines) を開き、`AI News Daily (dev test)` を選んで **Run now** をクリック (オーナーのみ閲覧可)
- **レビュー先**: https://github.com/kazu-dota/ai-news-daily/tree/dev-test/summaries
- **状態**: デフォルト無効 (enabled: false)、手動 Run now 専用

### routine 自体の改修について

- routine への恒久的な指示書は **`CLAUDE.md`** にまとめてあり、毎回 routine が起動時に読みます。指針を変えたい場合は `CLAUDE.md` を更新すれば、次回実行から反映されます
- routine の **schedule・モデル・許可ツール・MCP接続** の変更は claude.ai の routine 管理UIで行います (リポジトリ側のファイルでは管理しません)
- routine は2つあります (オーナーは [claude.ai → Routines](https://claude.ai/code/routines) から管理):
  - **本番** `AI News Daily` — 毎朝 8:00 JST に起動。`routine/auto-summary-YYYY-MM-DD-HHMMSS` ブランチを切って **PR を作成し auto-merge** で main に反映 (main の branch protection を尊重)
  - **dev test** `AI News Daily (dev test)` — `dev-test` ブランチに force push、Run now のみ

## ライセンス

- リポジトリ内のコード・設定: [MIT License](./LICENSE)
- サマリーコンテンツ: 各記事の事実情報を独自にまとめたもので、引用部分の権利は元の権利者に帰属します
