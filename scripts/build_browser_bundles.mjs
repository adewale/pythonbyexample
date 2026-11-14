#!/usr/bin/env node
// Bundle the browser modules that depend on npm packages into public/.
// The packages are pinned in package-lock.json, so the code visitors run
// changes only when a commit changes it; nothing is fetched from a CDN.
import { build } from 'esbuild';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');

for (const name of ['editor', 'highlighter']) {
  await build({
    entryPoints: [path.join(root, 'web', `${name}.js`)],
    outfile: path.join(root, 'public', `${name}.js`),
    bundle: true,
    format: 'esm',
    target: 'es2022',
    minify: true,
    legalComments: 'none',
    logLevel: 'warning',
  });
  console.log(`Bundled public/${name}.js`);
}
