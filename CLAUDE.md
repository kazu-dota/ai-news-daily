# CLAUDE.md — 開発者向け作業ガイド (このリポジトリで Claude Code を使うとき)

このファイルは Claude Code がこのリポジトリで動くとき (dev ブランチでの開発作業時)
に **自動的に読まれる恒久的な指示書** である。

> **routine が読む実行仕様** (本番 / dev-test routine の手順・著作権ルール・出力フォーマット) は
> 別ファイル [`ROUTINE.md`](./ROUTINE.md) にまとめてある。本ファイルでは routine の挙動の細部
> を再記載しない。修正したいときは `ROUTINE.md` を編集すれば、次回 routine 実行から反映される。

---

## このリポジトリの目的

毎日の生成 AI 関連ニュースを Claude Code の routine が自動収集・要約し、日本語の Markdown
アーカイブとして公開している ([README.md](./README.md) 参照)。
**開発者の役割は routine の指示書 (`ROUTINE.md`) と監視ソース (`sources.yaml`) を改善すること**。
routine 実行そのものはクラウド側で動くので、ローカル開発で必要なのは「ファイル編集 → dev-test
で動作確認 → PR で main マージ」の流れだけ。

---

## ブランチ構成

| ブランチ | 用途 | push 主体 |
|---|---|---|
| `main` | 本番 (公開先)。**branch protection で direct push 禁止** | PR 経由のみ |
| `dev` | 開発用 (人間が編集する場所) | 開発者 |
| `dev-test` | dev-test routine の使い捨て出力先 (force push される) | dev-test routine のみ |
| `routine/auto-summary-YYYY-MM-DD-HHMMSS` | 本番 routine の毎日のサマリー反映用 (auto-merge) | 本番 routine のみ |

開発作業は **必ず `dev` ブランチで** 行う。`main` は branch protection で direct push が
禁止されており、PR 経由でしかマージできない (admin であっても enforce される)。

---

## ファイル構成

```
ai-news-daily/
├── CLAUDE.md          ← このファイル (開発者向け)
├── ROUTINE.md         ← routine 用の実行仕様
├── README.md          ← リポジトリ説明 + 最新サマリーリンク
├── sources.yaml       ← 監視対象ソース定義
├── summaries/         ← 日次サマリー (YYYY/MM/YYYY-MM-DD.md)
├── docs/              ← GitHub Pages 用 (Jekyll)
├── .claude/agents/    ← サブエージェント定義 (Claude Code)
└── .github/ISSUE_TEMPLATE/
```

---

## 開発フロー

```
1. git checkout dev && git fetch origin && git rebase origin/main
   (※ main は本番 routine が毎日先行するので、必ず rebase してから作業開始)
2. ROUTINE.md / sources.yaml / docs/ などを編集
3. git commit && git push origin dev
   (rebase 後で履歴が変わっている場合は git push -f origin dev)
4. dev test routine を Run now で実行
   (claude.ai → Routines → "AI News Daily (dev test)")
5. dev-test ブランチに force push される md をレビュー
   https://github.com/kazu-dota/ai-news-daily/tree/dev-test/summaries
6. 期待どおりなら PR を main に向けて作成
   gh pr create --base main --head dev
7. PR をマージ (auto-merge / squash)
8. 翌朝 8:00 JST から本番 routine が新ルールで動作
```

### ⚠ コンフリクト回避のルール

main は本番 routine が毎日 PR + auto-merge で更新するため、**dev は気付くと数日遅れる**。
コンフリクトを防ぐために以下を厳守:

1. **README.md の `<!-- LATEST:BEGIN -->` 〜 `<!-- LATEST:END -->` セクションは絶対に触らない**
   — 本番 routine が毎日書き換える領域。ここを開発者が編集すると確実に衝突する
2. **`summaries/` 配下のファイルは手動編集しない** — routine の自動生成領域
3. **PR を出す前に必ず `git rebase origin/main`** で同期する。古い dev のまま PR を出すと、
   GitHub UI でコンフリクト警告が出る場合がある
4. PR が長く滞留した場合は、GitHub UI の「Update branch」ボタンか、ローカルで rebase + force push
   で main に追従させてから再度 push する

---

## 🤖 サブエージェント利用ポリシー (重要)

**コンテキストを大事にするため、重い作業は専用のサブエージェントに delegate すること。**

これは Anthropic の "[How we built our multi-agent research
system](https://www.anthropic.com/engineering/multi-agent-research-system)" および
"[Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)"
で述べられている設計原則に倣う:

1. **Context isolation** — 各 subagent は独立した context window で動作する。Web 探索や
   大量ファイル読みのような「最終的に少しの結論しか必要ないが、途中で大量のトークンを使う」
   作業を lead の context に流し込まない
2. **Output compression** — subagent は探索の生データではなく、**要約と結論のみ** を lead に
   返す。これにより lead の context は会話の主筋を保ったまま動ける
3. **Specialization** — 各 subagent は単一責任。description で「いつ使うか」を明確に
4. **Tool minimization** — subagent には必要最小限のツールしか渡さない
5. **Token economy** — Anthropic の評価では token 使用量が agent performance の 80% を
   説明する。重い探索は subagent に閉じ込め、lead は判断と orchestration に集中

### このリポジトリで定義済みの subagent

| 名前 | いつ呼ぶか | 主な tool |
|---|---|---|
| [`source-researcher`](.claude/agents/source-researcher.md) | 新しいニュースソースの追加候補を調査するとき (RSS/HTML 確認、更新頻度の評価、`sources.yaml` 形式での提案) | WebFetch, WebSearch, Read |
| [`summary-reviewer`](.claude/agents/summary-reviewer.md) | `summaries/` 配下の md を読んで `ROUTINE.md` のルール準拠を点検するとき (引用15語/30字、独自表現、必須セクション、no-update 記載、フォーマット崩れ) | Read, Grep, Glob |

### subagent を **使うべき** 典型作業

- 「Microsoft の AI ブログを5本 fetch して `sources.yaml` に追加候補を出して」 → `source-researcher`
- 「過去1週間の summaries が引用ルールを守っているか全件チェックして」 → `summary-reviewer`
- 「ハッカーニュースで AI 関連の RSS を探して」 → `source-researcher`

### subagent を **使わなくてよい** 作業

- ROUTINE.md の文言修正など、対象ファイルが特定済みで小さい編集
- README の typo 修正
- `git status` / `git log` などの確認系コマンド
- 単発の `gh pr create` / `gh pr merge`

### 新しい subagent が必要になったら

`.claude/agents/<name>.md` を frontmatter (`name` / `description` / `tools` / `model`) 付きで
新規作成し、本ファイルの「定義済みの subagent」表に追記する。description は **「どんなとき
に呼ぶべきか」** を明確に書くこと (lead がどの subagent を呼ぶか判断するため)。

---

## routine の役割 (詳細は ROUTINE.md)

| routine | スケジュール | 出力先 | 役割 |
|---|---|---|---|
| `AI News Daily` (本番) | 毎朝 8:00 JST | `routine/auto-summary-...` ブランチ → PR → main | 当日 md を生成して main に PR + auto-merge で反映 |
| `AI News Daily (dev test)` | 手動 Run now のみ | `dev-test` ブランチに force push | dev で行った変更を main マージ前に試運転 |

routine の prompt は claude.ai の Routines 管理 UI で管理されており、**リポジトリのファイル
ではない**。routine の動作を変えたい場合は通常 `ROUTINE.md` を編集すれば足りる (両方の routine
が起動時に必ず読み込むため)。schedule・モデル・ツール許可リストの変更だけは管理 UI で行う。

---

## 編集時の留意点

- `ROUTINE.md` を変更したら **必ず dev-test routine で動作確認** してから main にマージする
- `sources.yaml` に追加するソースは可能なら `source-researcher` subagent で事前に URL/更新頻度
  を検証する
- `summaries/` 配下のファイルは routine が自動生成するもの。**手動編集しない** (もし必要な
  ら著作権削除依頼など特殊ケースのみ)
- main の branch protection は `enforce_admins: true` なので、admin でも direct push は
  できない。必ず PR 経由
