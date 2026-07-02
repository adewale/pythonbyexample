#!/usr/bin/env node
// Exercises the search ranking against the real generated index so a
// ranking regression or an index/asset drift fails verification.
import { readFileSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const { rankExamples } = await import(path.join(root, 'public', 'search.js'));
const entries = JSON.parse(readFileSync(path.join(root, 'public', 'search-index.json'), 'utf8'));

const failures = [];
function expect(condition, message) {
  if (!condition) failures.push(message);
}

// Result nodes must be built with textContent, never innerHTML, so
// catalog fields can never be parsed as markup (DOM injection guard).
const searchSource = readFileSync(path.join(root, 'public', 'search.js'), 'utf8');
expect(!searchSource.includes('innerHTML'), 'search.js must not use innerHTML');

const closures = rankExamples('closures', entries);
expect(closures[0]?.slug === 'closures', `exact title should rank first, got ${closures[0]?.slug}`);

const decorator = rankExamples('decorator', entries);
expect(decorator[0]?.slug === 'decorators', `prefix match should rank decorators first, got ${decorator[0]?.slug}`);

const walrus = rankExamples('walrus', entries);
expect(
  walrus.some((entry) => entry.slug === 'assignment-expressions'),
  'concept keyword "walrus" should surface assignment-expressions',
);

const asyncResults = rankExamples('async', entries);
expect(asyncResults.length >= 2, 'async should match multiple examples');
expect(
  asyncResults.some((entry) => entry.slug === 'async-await'),
  'async should surface async-await',
);

const multiToken = rankExamples('for loop', entries);
expect(multiToken.some((entry) => entry.slug === 'for-loops'), '"for loop" should surface for-loops');

expect(rankExamples('zzzznonexistent', entries).length === 0, 'nonsense query should return nothing');
expect(rankExamples('', entries).length === 0, 'empty query should return nothing');
expect(rankExamples('closures', entries, 3).length <= 3, 'limit should cap results');

if (failures.length) {
  for (const failure of failures) console.error(`FAIL: ${failure}`);
  process.exit(1);
}
console.log(`Search ranking checks passed against ${entries.length} index entries.`);
