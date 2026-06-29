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
- [2026-06-30](summaries/2026/06/2026-06-30.md) — Claude in Microsoft Foundry GA (Azure ネイティブ・Opus 4.8 / Haiku 4.5・NVIDIA GB300) / [続報] Fable 5 停止 18 日目・Jerusalem Post「まもなく復旧」報道 / Google: Meta の Gemini コンピュートを制限・Muse Spark へ移行加速 / Gemini パーソナライズ画像生成を米国一般ユーザーに無料開放 / GitHub Trending: OmniRoute (+614★) / facebook/astryx (+394★)
- [2026-06-29](summaries/2026/06/2026-06-29.md) — Austria が EU に Anthropic 誘致を要請 (輸出規制対抗の AI 主権戦略) / [続報] Zhipu GLM-5.2 が停止 16 日で Mythos 5 同水準のセキュリティ能力を主張 / [続報] Fable 5 停止 17 日目 / 明日 (6/30) Anthropic「AI for Science」ライブ配信 / GitHub Trending: Vibe-Trading (+490★) / video-use (+324★)
- [2026-06-28](summaries/2026/06/2026-06-28.md) — [続報] Anthropic: 米商務省が Mythos 5 の輸出規制解除・100+ 米国機関が即時アクセス可能・Fable 5 は依然停止 / [補完] Google: Gemini 3.5 Pro の 6/30 GA を 7 月に延期・GPT-5.6・Grok 5 も 7 月スリップ / GitHub Trending: topoteretes/cognee (AIエージェントメモリプラット・+808★) / ppt-master (+589★) / graphify (+435★)
- [2026-06-27](summaries/2026/06/2026-06-27.md) — OpenAI × Broadcom: 推論専用チップ「Jalapeño」発表 / OpenAI: GPT-5.6「Sol/Terra/Luna」限定プレビュー＋ホワイトハウスが慎重公開を要請 / OpenAI: GPT-4.5 本日引退 / [続報] Gemini 研究者6日間で4名 Anthropic へ / 米4州が AI 規制法を一斉処理＋ホワイトハウス AI 大統領令
- [2026-06-26](summaries/2026/06/2026-06-26.md) — Anthropic: Alibaba が Claude に最大規模の蒸留攻撃 (偽アカウント 25,000・会話 2,880 万件) / Claude が Apple Foundation Models 対応 (WWDC 6/8 補完) / [続報] Fable 5 停止 15 日目・Tom Brown が交渉の前面へ・Polymarket 60% に上昇 / Meta: AI 予測市場アプリ計画浮上
- [2026-06-25](summaries/2026/06/2026-06-25.md) — Anthropic: Claude Tag 発表 (Slack に @Claude を共有 AI チームメンバーとして招待、6/23 初報・本日補完) / xAI: Grok Build に `/goal` 追加 (長時間タスクを自律完結、6/22 発表補完) / Google: gemini 画像生成プレビュー 2 モデルが本日廃止 / OpenAI: GPT-5 が免疫学者の 3 年越し謎解きに貢献 / [続報] Fable 5 停止 14 日目
- [2026-06-24](summaries/2026/06/2026-06-24.md) — Anthropic: Claude Corps 発表 ($150M・1,000 名フェローを全米 NPO へ、初報) / Google DeepMind: A24 に $75M 投資・AI 映画制作ツール共同開発 / SpaceX: Reflection AI と $6.3B コンピュートディール (Colossus 2・NVIDIA GB300) / Microsoft: Azure Copilot Observability Agent GA / [続報] Fable 5 停止 13 日目
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
