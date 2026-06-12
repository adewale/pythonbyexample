## Summary

<!-- What changed? -->

## Verification

- [ ] `make verify`
- [ ] `scripts/format_examples.py --check`
- [ ] `make verify-python-version VERSION=3.13`
- [ ] `git diff --check`

## Example changes

If this changes examples:

- [ ] Updated files under `src/example_sources/*.md`
- [ ] Kept exactly one `:::program` block per example
- [ ] Kept `:::cell` source/output deterministic and executable
- [ ] Ran `make verify-examples`
- [ ] Ran `make check-generated`
