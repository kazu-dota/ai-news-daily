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
- [2026-07-21](summaries/2026/07/2026-07-21.md) — [続報] OpenAI Build Week 最終日 (本日 17:00 PDT 提出期限・受賞 8/12) / EU DMA: Google に Android AI 開放・検索データ共有命令 (2027年1月〜) / [続報] Moonshot Kimi K3: GPU 需要過多で新規サブスク停止・専用コーディングプラン新設へ
- [2026-07-20](summaries/2026/07/2026-07-20.md) — [続報] WAIC 2026 本日閉幕・SAIL Award 発表・「モデルからシステムへ」6大トレンド総括 / [続報] Meta: 連邦地裁が AI 解雇差別訴訟の緊急差し止め申請を棄却 (7/22 分離予定通り) / GitHub 急騰: bojieli/ai-agent-book (+1,734★・AI エージェント実践書)・OmniRoute (+1,007★・268+ プロバイダー対応 AI ゲートウェイ)
- [2026-07-19](summaries/2026/07/2026-07-19.md) — [続報] Anthropic: Fable 5 含算アクセス本日 (7/19 PT) 終了・7/20 から Max/Team Premium に永続含算確定 / GitHub 新規急騰: lingbot-map (+827★・3D シーン再構築基盤モデル)・code-review-graph (+356★・MCP/CLI AI コードレビュー)・SigNoz (+425★・AI 可観測性) / [続報] WAIC 2026 Day 3 (最終日前日)
- [2026-07-18](summaries/2026/07/2026-07-18.md) — Moonshot AI: Kimi K3 正式リリース (2.8T param MoE、世界最大オープンウェイト・GDPval-AA v2 で 3 位) / [続報] WAIC 2026 Day 2・WAICA 学術カンファレンス開幕 (Hinton/Bengio/Sutton 登壇) / [続報] Meta: AI 主導の解雇差別訴訟・7/22 から分離開始 / GitHub: Nutlope/hallmark (+1,486★・Anti-AI-slop デザインスキル) 急騰
- [2026-07-17](summaries/2026/07/2026-07-17.md) — [続報] Google: Gemini 3.5 Pro が3回目の延期 (7/17 目標日未達、Gemini 3.6 Flash ストップギャップ浮上・予測市場7/31が81%) / [続報] WAIC 2026 本日開幕・Xi Jinping 初キーノート・WAICO 設立提案・Huawei Atlas 950・ZTE AI スマートフォン発表 / GitHub: NousResearch/hermes-agent 急騰
- [2026-07-16](summaries/2026/07/2026-07-16.md) — [補完] Anthropic: Claude for Teachers 発表 (米K-12教員に1年間無料・全50州基準準拠) / [続報] Fable 5 含算アクセスを7/19まで3回目延長 / [続報] Gemini 3.5 Pro GA 明日目標 (7/17, 公式未確認) / TSMC Q2 過去最高 $39.6B (+36%) / GitHub: BrowserOS・nanobot 急騰
- [2026-07-15](summaries/2026/07/2026-07-15.md) — Anthropic: Artifacts 公開共有・マルチプレイヤー編集・Claude Tag Slack 統合 (7/14) / [続報] 中国 AI コンパニオン規制本日施行・Doubao エージェントオフライン / [続報] Meta: Muse Image Instagram 参照機能を撤去 ("missed the mark") / Cloudflare Precursor GA (ボット 57%) / WAIC 2026 が 7/17 上海開幕・Xi 初キーノート
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
