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
- [2026-08-18](summaries/2026/08/2026-08-18.md) — Anthropic: Decart を $60 億で買収交渉中 (未掲載・8/13、チップ効率化＋世界モデル技術) / Microsoft: Consumer 向け Copilot 廃止機能が本日実施 (Podcasts・Deep Research 等終了) + 統合 Copilot アプリ URL 移行開始
- [2026-08-17](summaries/2026/08/2026-08-17.md) — Google: Gemini 3.7 Flash 公開 (未掲載・8/13、コーディング/エージェント向け・半額イントロ価格) / Google: Imagen 4 API が本日廃止 (gemini-3.1-flash-image へ移行必須) / xAI: Grok Bot beta 公開 (未掲載・8/11、常時稼働 AI エージェントチーム) / Z.ai: GLM-5.3 リリース (オープンウェイト最強コーディングモデル、ウェイトは2週間後)
- [2026-08-16](summaries/2026/08/2026-08-16.md) — Anthropic: Q2 2026 初の営業黒字 (売上 $11.5B 超・営業利益 $559M 超、2028年予測より2年前倒し) / Alibaba: Qwen3.8-27B open weights 公開 (27B multimodal・Apache 2.0・RTX 4090で動作) / Google: HEIR — 暗号化データ上で AI 推論を実現するオープンソース FHE コンパイラ (8/15) / DeepSeek: V4 Pro API 価格改定本日発動 (ピーク時最大 1,100% 超)
- [2026-08-15](summaries/2026/08/2026-08-15.md) — Google: Gemini アプリが月間 10 億ユーザー突破 (未掲載・8/11、Google 史上最速成長) / Meta: Manus AI が中国 NDRC 命令で Meta 買収から強制独立復帰 (米中 AI デカップリング) / DeepSeek: V4-Pro-0813 正式 GA (1.6T MoE・1M コンテキスト・8/16 価格引き上げ) / Anthropic: Claude Code v2.1.232 (サブエージェントフォーキング デフォルト ON)
- [2026-08-14](summaries/2026/08/2026-08-14.md) — Alibaba: Qwen3.8-Max (2.4T MoE) open weights がついに HuggingFace 公開 (Alibaba 初 Max クラス OSSリリース) / Anthropic: Claude Code auto mode が本日からデフォルトへ (分類器で危険コマンド 89% 検出) / OpenAI: GPT-5.6 Sol Ultrafast mode (14倍高速・750 tokens/sec・Cerebras 基盤) / Mistral: EU/US Regional Inference + Priority Tier 正式提供
- [2026-08-13](summaries/2026/08/2026-08-13.md) — Google: Made by Google 2026 で Pixel 11 シリーズ正式発表 (Tensor G6 TSMC 2nm・Pixel Watch 5・Pixel Tag、8/20発売) / Anthropic: Claude テキスト透かし (watermark) 全世界適用 (EU AI Act準拠・C2PA) / OpenAI: ChatGPT 週間10億ユーザー突破 (7/31・未掲載) + レストラン予約機能追加 / Microsoft: M365 Copilot 8月大型アップデート (GPT-5.6 + Claude統合・Cowork)
- [2026-08-12](summaries/2026/08/2026-08-12.md) — OpenAI: Daybreak Red / GPT-5.6-Cyber 公開 (セキュリティ特化、Chrome V8 ゼロデイ発見・CVE-2026-15903) / Anthropic: Claude for Teachers 発表 (全米50州対応、認定教師無償) / Google: Made by Google 2026 本日開催 — Pixel 11 シリーズ / ChatGPT Business にプレミアム席追加
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
