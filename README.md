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
- [2026-10-25](summaries/2026/10/2026-10-25.md) — **NVIDIA/OpenShell 初登場 (自律 AI エージェント向けセキュア Rust ランタイム +893)** / **anthropics/sandbox-runtime 初登場 (AI エージェント OS レベルサンドボックス TypeScript +592)** / **[続報] cloudflare/security-audit-skill グローバル Trending 首位返り咲き +2,271** / **heygen-com/hyperframes 初登場 (HTML→動画 AI エージェント向け ★71k +777)** / **[続報 Day 2] SnailSploit/Claude-Red +770 (前日比3.7倍に急加速)** — 主要 vendor 本日アップデートなし
- [2026-10-24](summaries/2026/10/2026-10-24.md) — **video-shotcraft 初登場 (Claude Code/Codex 向け AI 動画制作スキル TypeScript +262)** / **SnailSploit/Claude-Red 初登場 (Claude 向けオフェンシブセキュリティスキル集 Python +209)** / **[続報 Day 6] Graphify-Labs/graphify +1,328 (★133k、コードベース→ナレッジグラフ)** / **[続報 Day 3] luongnv89/claude-howto +1,168** / **[続報 Day 10] stablyai/orca ★103,811** — 主要 vendor 本日アップデートなし
- [2026-10-23](summaries/2026/10/2026-10-23.md) — **Anthropic: Agent Skills 標準を AAIF に寄贈 (MCP に次ぐ2本目・70+プラットフォーム統合・280M インストール)** / **Anthropic: ライフサイエンス向け招待研究者プログラム公募開始 (8〜12週間共同研究)** / **[続報 Day 3] cloudflare/security-audit-skill +2,979 stars に急加速 (★39,451)** / **genspark-ai/genoffice 初登場 (Genspark AI オフィスソフト OSS)** / firecrawl/firecrawl が TypeScript Trending 2位 (★194k) — OpenAI/Google/Meta ソース取得不可
- [2026-10-22](summaries/2026/10/2026-10-22.md) — **[続報 8日目・★100k 突破] stablyai/orca ★101,180 (TypeScript Trending 首位継続)** / **Anthropic: 物理学者 Christopher Stubbs が Long-Term Benefit Trust に就任** / **Panniantong/Agent-Reach 新登場 (AI エージェントに SNS/プラットフォーム CLI 付与 ★100k +461)** / **tashfeenahmed/freellmapi (無料 LLM API ルーター +684)** / **cline/cline (自律型コーディングエージェント +410)** — OpenAI/Google/Meta ソース取得不可
- [2026-10-21](summaries/2026/10/2026-10-21.md) — **[続報 7日目] stablyai/orca ★99,676 (★100k まで残り 324 stars、今日中にも突破)** / **cloudflare/security-audit-skill 初登場 (Cloudflare 製セキュリティ監査スキル JavaScript +1,680)** / **DietrichGebert/ponytail 初登場 (「コードを書かない原則」AI エージェント ★169k +1,396)** / **anthropics/knowledge-work-plugins 初登場 (Anthropic 公式 Claude Cowork プラグイン ★30k +262)** / **openclaw/openclaw 初登場 (汎用 AI アシスタント ★392k TypeScript)** — 主要 vendor 本日アップデートなし
- [2026-10-20](summaries/2026/10/2026-10-20.md) — **[続報 5日目] stablyai/orca ★98k 突破 (★100k まであと 1,797 stars)** / **MadsLorentzen/ai-job-search +3,860 stars 急騰 (直近最高)** / **Comfy-Org/ComfyUI 初登場 (拡散モデル GUI, ★139k +1,011)** / **headroomlabs-ai/headroom 初登場 (LLM コンテキスト圧縮 Python ★76k)** / **[終幕] debpalash/VoiceStudio 9日連続 Trending 終幕 (★75k 超)** — 主要 vendor 本日アップデートなし
- [2026-10-19](summaries/2026/10/2026-10-19.md) — **Anthropic: Public Benefit Fund 設立 (株式5%初期拠出、合計約20%を公益に)** / stablyai/orca ★100k 目前 (★96,571, +1,146) / **akitaonrails/ai-memory 新登場 (クロスエージェント長期記憶 Rust +513)** / **Graphify-Labs/graphify 新登場 (コードベース→ナレッジグラフ ★128k +592)** / **diegosouzapw/OmniRoute 新登場 (375プロバイダー対応 AIゲートウェイ +411)** / TauricResearch/TradingAgents 新登場 (マルチエージェント金融取引フレームワーク +242) — OpenAI/Google/Meta/Microsoft 本日アップデートなし
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
