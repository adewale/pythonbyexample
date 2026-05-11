#!/usr/bin/env bash
# One-time local git config so merges and rebases regenerate the asset
# manifest automatically instead of producing conflict markers.
#
#   * `merge.ours.driver = true` lets `.gitattributes`' `merge=ours`
#     resolve `src/asset_manifest.py` conflicts by keeping our side.
#   * `core.hooksPath = .githooks` activates the post-merge and
#     post-rewrite hooks that re-run `scripts/fingerprint_assets.py`
#     after the merge or rebase finishes.
#
# Both settings are local-only; nothing in this script touches the
# remote or shared config.
set -e
cd "$(git rev-parse --show-toplevel)"
git config merge.ours.driver true
git config core.hooksPath .githooks
chmod +x .githooks/post-merge .githooks/post-rewrite
echo "git hooks installed: merge.ours.driver=true, core.hooksPath=.githooks"
