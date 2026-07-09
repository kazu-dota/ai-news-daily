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
- [2026-07-10](summaries/2026/07/2026-07-10.md) — [補完] Meta: Muse Image が Meta AI・Instagram・WhatsApp に展開 (Meta Superintelligence Labs 初の画像生成モデル) / [補完] Anthropic: Claude Reflect ベータ (AI 使用パターン可視化ダッシュボード) / [続報] GPT-5.6 が本日 ChatGPT Plus に展開 (Team プラン 1.5M コンテキスト) / [補完] xAI: Grok Voice Agent Builder ベータ + 21 新フラグシップ音声 (7/6 発表)
- [2026-07-09](summaries/2026/07/2026-07-09.md) — OpenAI: GPT-5.6 Sol/Terra/Luna が全世界 GA (Ultra モード・サブエージェント駆動・Sol $5/$30 per Mtok) / xAI: Grok 4.5 パブリックローンチ (V9 1.5T・Cursor 統合・$2/$6 per Mtok) / Mistral 3 正式ローンチ (Large 3 675B MoE + Ministral 3 小型シリーズ Apache 2.0) / [補完] Anthropic: Claude Cowork が Web・モバイルに拡張 (バックグラウンド実行・M365 書き込み連携)
- [2026-07-08](summaries/2026/07/2026-07-08.md) — [補完] Microsoft: MAI モデルが Excel・Outlook の AI プロンプトを週数万件規模で内製代替 (Suleiman「Anthropic 支出をゼロにしたい」) / [補完] xAI: Grok Imagine アップデート 7/7 公開 / [続報] Mistral Large 3 詳細: 41B active / 675B total sparse MoE・Apache 2.0 / GitHub 急騰: ai-job-search (+2,402★ Claude Code 就活フレームワーク)
- [2026-07-07](summaries/2026/07/2026-07-07.md) — [補完] Anthropic × Samsung カスタム AI チップ交渉 (2nm プロセス) / Fable 5 が本日よりクレジット制移行 ($10/$50 per Mtok) / 国連 AI ガバナンス対話閉会 (2027/5 NY 第 2 セッション) / Mistral CEO: 夏の新旗艦オープンウェイトモデルを確認 / Meta: ワシントン州 1,395 名解雇 7/22 開始
- [2026-07-06](summaries/2026/07/2026-07-06.md) — OpenAI: 元ホワイトハウス AI 顧問 Dean Ball が Strategic Futures 部門長として入社 / 国連: 世界初の政府間 AI ガバナンス対話がジュネーブで開幕 (193 カ国参加・Yoshua Bengio × Maria Ressa 共同議長) / 米ホワイトハウス「自発的 AI 公開基準」明日 (7/7) 発表見込み / [補完] Mistral: Leanstral 1.5 公開 (Lean 4 形式証明・PutnamBench 587/672)
- [2026-07-05](summaries/2026/07/2026-07-05.md) — Anthropic: 中国企業による Claude 不正利用を全面遮断 (Alibaba Qwen ラボが 2,880 万回の蒸留攻撃) / Meituan: LongCat-2.0 — 1.6T MoE オープンソース公開 (SWE-bench Pro 59.5 で GPT-5.5 超) / Together AI: $800M Series C 調達・評価額 $8.3B / 国連: AI ガバナンス初の政府間対話がジュネーブで開幕 (193 カ国参加)
- [2026-07-04](summaries/2026/07/2026-07-04.md) — OpenAI: 米国政府への 5% 株式提供を提案 (~$42.6B) / Anthropic ARR $30B 超で OpenAI を追い越したとの報道 / White House が主要 AI 3 社と「自発的 AI 公開基準」策定を協議 / [補完] Claude Enterprise 管理者向け新機能 GA / [補完] xAI: Grok 4.5 が SpaceX・Tesla で private beta 開始
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
