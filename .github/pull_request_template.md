<!--
このリポジトリは `dev → main` 運用です (詳細は CLAUDE.md / README.md)。
本 PR が main 向けである場合は dev-test routine の試運転結果を必ず確認してください。
-->

## 変更内容

<!-- 何を、なぜ変えたか。1〜3行で簡潔に。 -->

## 影響範囲

- [ ] `ROUTINE.md` (routine 実行仕様)
- [ ] `sources.yaml` (監視ソース)
- [ ] `docs/` (Pages UI / 構造化データ)
- [ ] `.github/` (CI / workflow)
- [ ] その他:

## チェックリスト

- [ ] `<!-- LATEST:BEGIN -->` 〜 `<!-- LATEST:END -->` (`README.md`) を編集していない
- [ ] `summaries/` 配下を手動編集していない (著作権削除依頼など特殊ケースを除く)
- [ ] `git rebase origin/main` 済み (main は本番 routine が毎日先行するため)
- [ ] dev-test routine の試運転結果を確認した
  - PR open 時に `dev-test-trigger.yml` が webhook を起動 → routine が `dev-test` ブランチに force push
  - レビュー先: https://github.com/kazu-dota/ai-news-daily/tree/dev-test/summaries
  - 差分: https://github.com/kazu-dota/ai-news-daily/compare/main...dev-test

## 補足

<!-- 関連 Issue / 参考リンク / レビュアー向けの注意点 -->
