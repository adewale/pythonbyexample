## Summary

<!-- What changed and why? Link the issue or explain the concrete motivation. -->

## Verification

<!-- Check only evidence actually run. Explain any applicable unchecked item above. -->

- [ ] `make verify`
- [ ] `scripts/format_examples.py --check`
- [ ] `make verify-python-version VERSION=3.13`
- [ ] `git diff --check`
- [ ] Added or updated regression tests and verified they fail when the fix is reverted
- [ ] Manual verification: named route/flow, environment, and observed result in Summary

## Visual evidence (required for UI changes)

<!-- Delete this section only when the PR has no visual impact. Caption each
image/recording with the observable change and record how it was captured. -->

**Before — [specific observable behavior]:**
<!-- image or recording -->

**After — [specific observable behavior]:**
<!-- image or recording -->

**Reproduction:** `[command]` (base: `[sha]`; head: `[sha]`; viewport/state: `[details]`)

## Example changes

If this changes examples:

- [ ] Updated files under `src/example_sources/*.md`
- [ ] Kept exactly one `:::program` block per example
- [ ] Kept `:::cell` source/output deterministic and executable
- [ ] Ran `make verify-examples`
- [ ] Ran `make check-generated`
