# ROUTINE.md — AI News Daily ルーティン行動指針 (本番 / dev-test routine 用)

このファイルは、claude.ai の Routines (`AI News Daily` および `AI News Daily (dev test)`) が
毎回起動するときに **prompt から明示的に参照する恒久的な指示書** である。
routine は新しいセッションで起動し、過去の文脈は引き継がれない。必要な情報はすべてここに記述する。

> **開発者向けの作業手引き** (Claude Code を dev ブランチで動かすときに自動で読まれる) は別ファイル
> [`CLAUDE.md`](./CLAUDE.md) にある。サブエージェント利用ポリシーや開発フローはそちらを参照。
> 本ファイルは routine 専用の実行仕様。

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

### Step 3.5. 過去 7 日分のサマリーを参照 (重複防止)

同じニュースが何日も繰り返し記載されることを防ぐため、当日のキュレーション前に
**過去 7 日分の md ファイル** を読み込んで「既出 URL」と「既出トピック」を抽出する。

#### 読み込み対象
当日 ($TODAY) を起点に、過去 7 日 (= $TODAY-1 〜 $TODAY-7) の以下のファイルを Read:
```
summaries/$(date -d "$TODAY -1 day" +%Y/%m)/$(date -d "$TODAY -1 day" +%Y-%m-%d).md
summaries/$(date -d "$TODAY -2 day" +%Y/%m)/$(date -d "$TODAY -2 day" +%Y-%m-%d).md
... (-7 day まで)
```
存在しない日 (まだサマリーがない日) はスキップして良い。

bash で日付ループを回す場合の例:
```bash
for d in 1 2 3 4 5 6 7; do
  PAST=$(TZ=Asia/Tokyo date -d "$TODAY -$d day" +%Y/%m/%Y-%m-%d 2>/dev/null \
       || TZ=Asia/Tokyo date -v-${d}d -j -f %Y-%m-%d "$TODAY" +%Y/%m/%Y-%m-%d)
  [ -f "summaries/${PAST}.md" ] && cat "summaries/${PAST}.md"
done
```
(GNU date / BSD date の両対応)

#### 抽出するもの
読み込んだ md から以下を集計してメモリに保持:
- **`seen_urls`**: 各 md 内の Markdown link `[...](URL)` の URL を全て抽出 (重複除去)
- **`seen_topics`**: 各 md の `### <vendor>: <製品/トピック>` 見出し行を抽出 (vendor 名 + 製品名の組み合わせ)
   - 例: `Anthropic: Claude Opus 4.7 の詳細`、`Microsoft: M365 Copilot Wave X 公開`

これら2つのリストを Step 4 のキュレーションで参照する。

### Step 4. キュレーション
取得した候補から以下をフィルタリング:
- AI関連でないものを除外 (`ai_keywords`: AI, LLM, GenAI, ML, model, 生成AI, etc.)
- **過去との重複判定** (Step 3.5 で抽出した `seen_urls` / `seen_topics` を使用):
  1. **完全重複** (元記事 URL が `seen_urls` に存在) → **採録しない**
  2. **続報** (URL は新しいが、トピック=vendor+製品/トーマ が `seen_topics` に存在)
     → 採録するが、見出しに `[続報]` を付ける。前回記載済みの内容は再記載せず、**新情報 (差分) のみ** を 2〜3 行で書く
     - 例: 前日に「Anthropic: Claude Opus 4.7 GA」を記載 → 当日「Opus 4.7 が Stanford HELM で首位」 → `### [続報] Anthropic: Claude Opus 4.7 — Stanford HELM ベンチ首位獲得`
  3. **新規** (どちらにも該当しない) → 通常通り記載
- 別ソースから来た同じトピックは統合 (当日内の重複)
- 24時間以上古いものは除外 (公式発表日が当日 or 前日のものに限る)
- 重要度評価 (続報の重要度判定にも適用):
  - 新モデル/新製品の発表 → 必ずハイライト候補
  - 大手VCの大型調達/買収 → ハイライト候補
  - 政府規制・大手の方針変更 → ハイライト候補
  - GitHub星数の急増 (★ +1k/day超) → 候補
  - 続報のうち「ベンチマーク結果・採用事例・価格変更」など実質的な新情報があるもの → 候補
  - 続報のうち「同じ事実の蒸し返し・前回の言い換え」しか無いもの → ハイライトに上げない (本文に短く触れるのみ)
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

**📌 該当アップデートがない場合の記載ルール (絶対遵守)**:
読者が「routine が探さなかった」のと「本当に該当発表がなかった」を区別できるように、**黙って項目・セクションを省略してはならない**。

- **各メインセクションは必ず存在させる** (`🔥 ハイライト` / `🏢 企業・モデル発表` / `💻 技術コミュニティ` / `📚 話題の研究論文` / `📰 メディア記事`)。該当0件でもセクション見出しは出し、本文に「**本日該当アップデートなし**」と1行記載する
- **主要 vendor は必ず言及する**: 以下の vendor は、当日アップデートがない場合でも `### <vendor名>: 本日アップデートなし` の1行を残す
  - Anthropic
  - OpenAI
  - Google / Google DeepMind
  - **Microsoft** (Microsoft 365 Copilot / Copilot Studio / GitHub Copilot / Azure AI 等を確認した上で、無ければ「本日アップデートなし」と明記)
  - Meta
- 上記以外の vendor (Mistral, xAI, Hugging Face 等) は、当日発表があった場合のみ記載で良い
- ハイライトが0件の場合は「本日特筆すべき大型発表なし」と1行記載
- メタ情報の `items_curated` が 0 になることは原則ない (vendor 各社の "アップデートなし" を含めれば最低5件は記載される)

### Step 6. 出力フォーマット

`summaries/2026/05/2026-05-10.md` を以下のフォーマットで作成:

```markdown
---
date: 2026-05-10
generated_at: 2026-05-10T08:05:00+09:00
sources_checked: 18
sources_failed: 0
items_total: 47
items_curated: 18
---

# AI News — 2026年5月10日

## 🔥 今日のハイライト
- **Anthropic、Claude Opus 4.8 を発表** — 推論ベンチで前世代比 +12% [↓詳細](#anthropic-opus-48)
- ...

(該当0件の場合: 「本日特筆すべき大型発表なし」と1行記載)

## 🏢 企業・モデル発表
### <a id="anthropic-opus-48"></a>Anthropic: Claude Opus 4.8 発表
事実情報を独自要約で2〜4行。
- 元記事: [Introducing Claude Opus 4.8](https://www.anthropic.com/news/...)

### [続報] Anthropic: Claude Opus 4.7 — Stanford HELM で首位
※ 過去 7 日に既に取り上げた話題の続報の場合は `[続報]` プレフィックスを付け、
   **新情報 (今日の差分) のみ**を2〜3行で書く。前回記載済みの内容は再掲しない。
- 関連: 前回 [2026-05-08](summaries/2026/05/2026-05-08.md) に Opus 4.7 GA を記載済み
- 元記事 (新): [HELM benchmark result](https://crfm.stanford.edu/helm/...)

### OpenAI: 本日アップデートなし

### Google / Google DeepMind: Gemini 3.x の機能拡張
事実情報を独自要約で2〜3行。
- 元記事: [...](https://blog.google/...)

### Microsoft: Microsoft 365 Copilot Wave X 公開
事実情報を独自要約で2〜3行。Copilot 本体・Copilot Studio・GitHub Copilot・Azure AI Foundry のいずれかでアップデートがあれば各々を1ブロックとして記載。
- 元記事: [...](https://blogs.microsoft.com/...)

### Microsoft (Copilot Studio): エージェント機能のGA
事実情報を独自要約で2〜3行。
- 元記事: [...](https://www.microsoft.com/en-us/power-platform/blog/...)

### Microsoft (GitHub Copilot): 本日アップデートなし

### Meta: 本日アップデートなし

(その他 vendor: 当日発表があれば記載、なければ省略可)

## 💻 技術コミュニティ
### GitHub Trending (AI関連)
- [`org/repo`](https://github.com/...) — 1行説明 (★ +1.2k today)

(該当0件の場合: 「本日 AI 関連の急騰なし」)

### Hacker News / Reddit ハイライト
- ...

(該当0件の場合: 「本日該当なし」)

## 📚 話題の研究論文
※ Hugging Face Papers / Hacker News / Reddit でバズった論文のみ採録
- **タイトル (arXiv:2505.xxxxx)** — なぜ話題か含む一文サマリー [arXiv](URL) [HF Papers](URL)

(該当0件の場合: 「本日バズった論文なし」)

## 📰 メディア記事
※ 著作権配慮: 1記事2〜3行、ペイウォールはタイトルのみ
- [TechCrunch] タイトル要約 — 1〜2行コメント [元記事](URL)

(該当0件の場合: 「本日特筆すべきメディア記事なし」)

## 📊 メタ情報
- 取得ソース: 18 (失敗 0) / 候補: 47 / 採録: 18
- 生成: Claude Code routine `ai-news-daily`
```

### Step 6.5. 構造化データの出力 (UI 用)

GitHub Pages 上の SPA (`docs/index.html`) が UI として読むため、md と並行して **機械可読な
JSON** を出力する。Pages から fetch する都合上、**ファイルは `docs/data/` 配下** に置く。

#### A. 当日の items ファイル
`docs/data/items/YYYY-MM-DD.json` を新規作成 (`mkdir -p` で親ディレクトリ作成):

```json
{
  "date": "2026-05-10",
  "generated_at": "2026-05-10T08:05:00+09:00",
  "sources_checked": 18,
  "sources_failed": 0,
  "items": [
    {
      "id": "2026-05-10-anthropic-opus-48",
      "type": "new",
      "vendor": "Anthropic",
      "section": "vendor",
      "title": "Claude Opus 4.8 発表",
      "summary": "推論ベンチで前世代比 +12%。視覚精度も向上。",
      "url": "https://www.anthropic.com/news/claude-opus-4-8",
      "importance": "highlight",
      "tags": ["model-release", "anthropic"]
    },
    {
      "id": "2026-05-10-openai-no-update",
      "type": "no-update",
      "vendor": "OpenAI",
      "section": "vendor"
    },
    {
      "id": "2026-05-10-anthropic-opus-47-helm",
      "type": "followup",
      "vendor": "Anthropic",
      "section": "vendor",
      "title": "[続報] Claude Opus 4.7 — Stanford HELM 首位",
      "summary": "直前のベンチ評価で首位。新情報のみ短く。",
      "url": "https://crfm.stanford.edu/helm/...",
      "related_date": "2026-05-08",
      "importance": "standard",
      "tags": ["benchmark", "anthropic", "opus"]
    }
  ]
}
```

各 item のフィールド仕様:
- `id`: `YYYY-MM-DD-<slug>` 形式 (slug は md の `<a id="...">` と同じものを推奨)
- `type`: `new` / `followup` / `no-update`
- `vendor`: vendor 名 (Anthropic / OpenAI / Google / Microsoft / Meta / Mistral / xAI / Hugging Face / その他は自由)
- `section`: `vendor` / `community` / `papers` / `media` / `governance`
- `title`: md と同じ見出し本文
- `summary`: 1〜2 行の要旨 (md 本文より短い、検索表示用)
- `url`: 元記事 URL (no-update の場合は省略)
- `importance`: `highlight` (今日のハイライト) / `standard` (通常) / `minor` (短く触れる程度)
- `tags`: 自由なキーワード配列 (UI のフィルタ・検索で使う)
- `related_date` (followup のみ): 元の話題を取り上げた日付

#### B. 累積インデックスの更新

`docs/data/index.json` を読み込み、**当日の items を append** して書き戻す。

```python
# 擬似コード
existing = json.load("docs/data/index.json") if exists else []
new_items = [{"date": "2026-05-10", **item} for item in today_items]
existing.extend(new_items)
json.dump(existing, "docs/data/index.json")
```

`docs/data/index.json` の中身は **フラットな配列** (1 アイテム = 1 オブジェクト):
```json
[
  {"date": "2026-05-10", "id": "...", "vendor": "Anthropic", "title": "...", "type": "new", ...},
  {"date": "2026-05-10", "id": "...", "vendor": "OpenAI", "type": "no-update", ...},
  {"date": "2026-05-09", ...},
  ...
]
```

新しい順 (最新が先) で並べる。古い項目はライフサイクル管理で別途扱うので、ここではすべて残す。

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
git add summaries/ README.md docs/data/
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
