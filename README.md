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
- [2026-06-15](summaries/2026/06/2026-06-15.md) — [続報] Anthropic 6/15 二重期限が本日発効 (Agent SDK 課金分離・旧モデル廃止)・開発者コミュニティに大反響 / Microsoft: M365 Copilot が 8 時間超の大規模障害 (今年 3 回目) / Moonshot AI: Kimi K2.7-Code 公開 (1T パラメータ OSS MoE、MCPMark で Claude Opus 4.8 超) / GitHub Trending: OpenHands・Kronos
- [2026-06-14](summaries/2026/06/2026-06-14.md) — [続報] Anthropic 6/15 二重期限が本日深夜発効 (Sonnet 4 / Opus 4 廃止 & エージェント課金分離) / OpenAI: GPT-5.2 全廃止・GPT-5.5 Instant が ChatGPT 完全標準化 (6/12) / Meta: 社内 AI トークン消費が月 73.7 兆に急増・AI Gateway 展開へ / xAI: Grok Build Plugin Marketplace β 公開 / GitHub Trending: anthropics/skills (+375)・LMCache (+246)
- [2026-06-13](summaries/2026/06/2026-06-13.md) — Anthropic × DXC: 多年グローバル同盟で世界最大規模の金融・航空・保険企業に Claude を展開 / OpenAI: Ona (旧Gitpod) 買収発表 (Codex エージェントがクラウドで常時稼働) / Anthropic: 6/15 二重期限 — Claude Sonnet 4 / Opus 4 廃止 + エージェント課金分離が同日発効 / GitHub Trending: NVIDIA/SkillSpector (+811・急加速)・claude-bug-bounty (新規)
- [2026-06-12](summaries/2026/06/2026-06-12.md) — SpaceX (SPCX) Nasdaq 初上場・史上最大 IPO ($75B・$1.75T) で xAI・Grok が公開市場デビュー / OpenAI: Oracle Cloud パートナーシップ (既存 OCI 予算で GPT モデル・Codex を利用可能) / Meta: Manus 買収 ($2B) 解除開始 (北京命令) / GitHub Trending: NVIDIA/SkillSpector・anomalyco/opencode・mksglu/context-mode
- [2026-06-11](summaries/2026/06/2026-06-11.md) — Anthropic: Claude Managed Agents に Cron スケジュール + Credential Vault がパブリックベータ追加 / Anthropic: 6/15 課金改訂 (Agent SDK が独立クレジット化、残り4日) / Google: `google/skills` 公式エージェントスキルリポジトリを公開 / xAI: Grok V9-Medium が Tesla・X に展開開始 / GitHub Trending: MoneyPrinterTurbo・OpenSpec
- [2026-06-10](summaries/2026/06/2026-06-10.md) — Anthropic: Claude Fable 5 一般公開 (SWE-Bench Pro 80.3%・Terminal-Bench 88.0%・1M+ コンテキスト、GitHub Copilot/Bedrock 同日展開) / Anthropic: Apple Foundation Models 向け Swift パッケージ公開 (iOS 27/macOS 27 でオンデバイスモデルと無段切替) / xAI: Grok V9-Medium (1.5T) 訓練完了・今週中リリースへ / GitHub Trending: whichllm・Personal_AI_Infrastructure
- [2026-06-09](summaries/2026/06/2026-06-09.md) — Apple WWDC Day 2: iOS 27 開発者ベータ公開・Core AI (Core ML 後継) と MCP システム横断統合の詳細を開発者向けに解禁 / Meta: Best Buy に「Meta Lab」体験コーナー全米展開 / GitHub Trending: turbovec (+1,730)・last30days-skill (+3,558 急加速)・LibreChat・project-nomad
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
