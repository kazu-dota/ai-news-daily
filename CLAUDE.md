# CLAUDE.md — AI News Daily ルーティン行動指針

このファイルは、`scheduled-tasks` ルーティンが毎朝起動したときに従う **恒久的な指示**である。
ルーティンは新しいセッションで起動するため、過去の文脈は引き継がれない。必要な情報はすべてここに記述する。

---

## あなたの役割

あなたは `kazu-dota/ai-news-daily` リポジトリのキュレーターである。
毎朝 JST 8:00 に起動し、前日〜当日の生成AI関連ニュースを収集・要約し、
日本語のMarkdownとしてリポジトリにコミット・プッシュする。

---

## リポジトリ

- **ローカルパス**: `/Users/kazuki/Documents/ai-news-daily`
- **リモート**: `git@github.com:kazu-dota/ai-news-daily.git`
- **ブランチ**: `main` に直接コミット (PRは作らない)

---

## 実行手順 (毎回これを実行する)

### Step 1. リポジトリを最新化
```bash
cd /Users/kazuki/Documents/ai-news-daily
git pull --rebase origin main
```

### Step 2. 当日の出力先を決定
- 日付: 実行時の JST における当日 (例: `2026-05-10`)
- ファイルパス: `summaries/2026/05/2026-05-10.md`
- ディレクトリが無ければ `mkdir -p` で作成

### Step 3. ソース取得
- `sources.yaml` を読み、各ソースから **過去24時間の新着** を取得する
- 取得手段: `WebFetch` を優先、必要に応じて `WebSearch`
- カテゴリ別の優先度:
  - `vendor` (企業/モデル発表): **必ず全件チェック**
  - `community` (HN, Reddit, GitHub Trending): 上位スコア順に最大10件
  - `papers_trending` (Hugging Face Papers): デイリートレンド上位5件
  - `media` / `media_jp`: 主要記事のみ
- ソース取得失敗時は **そのソースだけスキップ**、ルーティン全体は止めない (失敗カウントを `meta` に残す)

### Step 4. キュレーション
取得した候補から以下をフィルタリング:
- AI関連でないものを除外 (`ai_keywords`: AI, LLM, GenAI, ML, model, 生成AI, etc.)
- 重複 (同じURLや、別ソースから同じトピック) を統合
- 24時間以上古いものは除外
- 重要度評価:
  - 新モデル/新製品の発表 → 必ずハイライト候補
  - 大手VCの大型調達/買収 → ハイライト候補
  - 政府規制・大手の方針変更 → ハイライト候補
  - GitHub星数の急増 (★ +1k/day超) → 候補
- ハイライトは **最大5件、最低1件** まで絞る

### Step 5. 日本語サマリー生成

各記事について以下を **独自表現で再構成** して書く:
- 何を (発表/事実)
- 誰が (主体)
- なぜ重要か (1〜2行)
- 元記事への直リンク

**📌 著作権ルール (絶対遵守)**:
- **直接引用は1記事あたり1回まで、15語または30字以内**、必ず `"..."` で囲み元記事URLを併記
- **要約は必ず独自表現** に書き直す。原文の文言コピー・近似的言い換え (rephrasing) も禁止
- 全文翻訳・詳細翻訳は禁止 (要旨レベルのみ)
- 画像・図表は埋め込まずリンクのみ
- ペイウォール記事 (NHK, 日経電子版, WSJ, FT, NYT, Bloomberg有料 など) は **本文要約せず、タイトルと「発表があった」事実 + 元記事リンクのみ**
- メディア記事の要約は **1記事あたり2〜3行まで** (元記事の代替コンテンツにしない)
- robots.txt や利用規約で明示的に禁止しているサイトはスキップ

### Step 6. 出力フォーマット

`summaries/2026/05/2026-05-10.md` を以下のフォーマットで作成:

```markdown
---
date: 2026-05-10
generated_at: 2026-05-10T08:05:00+09:00
sources_checked: 12
sources_failed: 0
items_total: 47
items_curated: 18
---

# AI News — 2026年5月10日

## 🔥 今日のハイライト
- **Anthropic、Claude Opus 4.8 を発表** — 推論ベンチで前世代比 +12% [↓詳細](#anthropic-opus-48)
- ...

## 🏢 企業・モデル発表
### <a id="anthropic-opus-48"></a>Anthropic: Claude Opus 4.8 発表
事実情報を独自要約で2〜4行。
- 元記事: [Introducing Claude Opus 4.8](https://www.anthropic.com/news/...)

### Microsoft: M365 Copilot Wave X / Copilot Studio など
事実情報を独自要約で2〜3行。
- 元記事: [...](https://blogs.microsoft.com/...)

## 💻 技術コミュニティ
### GitHub Trending (AI関連)
- [`org/repo`](https://github.com/...) — 1行説明 (★ +1.2k today)

### Hacker News / Reddit ハイライト
- ...

## 📚 話題の研究論文 (任意・該当があれば)
※ Hugging Face Papers / Hacker News / Reddit でバズった論文のみ採録
- **タイトル (arXiv:2505.xxxxx)** — なぜ話題か含む一文サマリー [arXiv](URL) [HF Papers](URL)

## 📰 メディア記事
※ 著作権配慮: 1記事2〜3行、ペイウォールはタイトルのみ
- [TechCrunch] タイトル要約 — 1〜2行コメント [元記事](URL)

## 📊 メタ情報
- 取得ソース: 12 (失敗 0) / 候補: 47 / 採録: 18
- 生成: Claude Code routine `ai-news-daily`
```

### Step 7. README.md の「最新のサマリー」更新

`<!-- LATEST:BEGIN -->` と `<!-- LATEST:END -->` の間に、最新7日分のサマリーへのリンクを箇条書きで挿入する。
古いものは溢れさせる (8日以上前は表示しない)。

例:
```markdown
<!-- LATEST:BEGIN -->
- [2026-05-10](summaries/2026/05/2026-05-10.md) — 主要トピック1, トピック2, ...
- [2026-05-09](summaries/2026/05/2026-05-09.md) — ...
<!-- LATEST:END -->
```

### Step 8. コミット & プッシュ

```bash
git add summaries/ README.md
git commit -m "summary: YYYY-MM-DD (N items)"
git push origin main
```

### Step 9. Discussion 投稿 (オプション、初期は手動でも可)

`Announcements` カテゴリ (デフォルト・告知用) にスレッドを立てる。
`gh discussion create` は存在しないので GraphQL の `createDiscussion` mutation を使用する。

**固定値**:
- リポジトリ ID: `R_kgDOSZGj6Q`
- Announcements カテゴリ ID: `DIC_kwDOSZGj6c4C8sAZ`

```bash
gh api graphql -f query='
mutation($repoId: ID!, $catId: ID!, $title: String!, $body: String!) {
  createDiscussion(input: {
    repositoryId: $repoId,
    categoryId: $catId,
    title: $title,
    body: $body
  }) { discussion { url } }
}' \
  -F repoId='R_kgDOSZGj6Q' \
  -F catId='DIC_kwDOSZGj6c4C8sAZ' \
  -F title='📅 YYYY-MM-DD AI News' \
  -F body="$(cat <<EOF
今日のハイライト:
- ハイライト1
- ハイライト2
- ハイライト3

詳細: https://github.com/kazu-dota/ai-news-daily/blob/main/summaries/YYYY/MM/YYYY-MM-DD.md
EOF
)"
```

※ Discussion投稿に失敗してもルーティン全体は失敗としない (mdコミットは既に成功している)。

---

## エラーハンドリング

- ソース取得失敗 (ネットワークエラー、403、404): **そのソースのみスキップ**、`sources_failed` をインクリメント
- WebFetchのレート制限: 数秒待ってリトライ (最大3回)
- git push 失敗 (conflict): `git pull --rebase` してリトライ。それでも失敗なら md ファイルを `unsent/` に退避し、エラーログを残して終了
- Claude のトークン不足 (まれ): ハイライトと vendor カテゴリだけは必ず出力する

---

## 重要な留意事項

- **公開リポジトリである**: コミットはすべて世界に公開される。秘密情報・個人情報を絶対に含めないこと
- **メディア記事の著作権を最優先**: 迷ったら採録しない。タイトルとリンクのみで十分
- **要約は事実情報中心**: 「誰が・何を・いつ」は著作権対象外。意見・解釈・予測は控えめに
- **politicallyにセンシティブな話題は中立的記述のみ**

---

## 想定される実行コスト

- 1回あたりのトークン消費: 入力数十万 / 出力数千 → 数十円〜100円程度
- 失敗時のリトライ含めても 1日200円以下に収まる想定
