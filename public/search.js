// Client-side example search. Ranking is exported so
// scripts/check_search_ranking.mjs can exercise it in Node.

export function rankExamples(query, entries, limit = 8) {
  const tokens = query.toLowerCase().split(/\s+/).filter(Boolean);
  if (!tokens.length) return [];
  const scored = [];
  for (const entry of entries) {
    const title = entry.title.toLowerCase();
    const slug = entry.slug.toLowerCase();
    const section = entry.section.toLowerCase();
    const summary = entry.summary.toLowerCase();
    let score = 0;
    let matched = true;
    for (const token of tokens) {
      let tokenScore = 0;
      if (title === token) tokenScore = 100;
      else if (title.startsWith(token)) tokenScore = 80;
      else if (new RegExp(`\\b${token.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}`).test(title)) tokenScore = 60;
      else if (slug.includes(token)) tokenScore = 50;
      else if (section.startsWith(token)) tokenScore = 30;
      else if (summary.includes(token)) tokenScore = 25;
      else if (entry.text.includes(token)) tokenScore = 15;
      if (!tokenScore) { matched = false; break; }
      score += tokenScore;
    }
    if (matched) scored.push({ entry, score });
  }
  scored.sort((a, b) => b.score - a.score || a.entry.title.localeCompare(b.entry.title));
  return scored.slice(0, limit).map((item) => item.entry);
}

function wireSearch() {
  const container = document.querySelector('.site-search');
  const input = document.getElementById('site-search-input');
  const results = document.getElementById('site-search-results');
  if (!container || !input || !results) return;

  let entries = null;
  let loading = null;
  function loadIndex() {
    if (!loading) {
      loading = fetch(container.dataset.searchIndex)
        .then((response) => response.json())
        .then((data) => { entries = data; })
        .catch(() => { loading = null; });
    }
    return loading;
  }

  function hideResults() {
    results.hidden = true;
    results.replaceChildren();
  }

  // Result nodes are built with textContent so catalog fields can never
  // be parsed as markup.
  function resultNode(entry) {
    const item = document.createElement('li');
    const link = document.createElement('a');
    link.href = `/examples/${encodeURIComponent(entry.slug)}`;
    const title = document.createElement('strong');
    title.textContent = entry.title;
    const meta = document.createElement('span');
    meta.className = 'meta';
    meta.textContent = ` · ${entry.section}`;
    link.append(title, meta);
    item.appendChild(link);
    return item;
  }

  function renderResults() {
    if (!entries) return;
    const matches = rankExamples(input.value, entries);
    if (!matches.length) {
      if (input.value.trim()) {
        const empty = document.createElement('li');
        empty.className = 'search-empty';
        empty.textContent = 'No matching examples.';
        results.replaceChildren(empty);
        results.hidden = false;
      } else {
        hideResults();
      }
      return;
    }
    results.replaceChildren(...matches.map(resultNode));
    results.hidden = false;
  }

  input.addEventListener('focus', loadIndex, { once: true });
  input.addEventListener('input', () => { loadIndex().then(renderResults); });
  input.addEventListener('keydown', (event) => {
    const links = [...results.querySelectorAll('a')];
    if (event.key === 'Escape') {
      input.value = '';
      hideResults();
    } else if (event.key === 'ArrowDown' && links.length) {
      event.preventDefault();
      links[0].focus();
    } else if (event.key === 'Enter' && links.length) {
      event.preventDefault();
      links[0].click();
    }
  });
  results.addEventListener('keydown', (event) => {
    const links = [...results.querySelectorAll('a')];
    const index = links.indexOf(document.activeElement);
    if (event.key === 'ArrowDown' && index >= 0 && index + 1 < links.length) {
      event.preventDefault();
      links[index + 1].focus();
    } else if (event.key === 'ArrowUp' && index > 0) {
      event.preventDefault();
      links[index - 1].focus();
    } else if (event.key === 'ArrowUp' && index === 0) {
      event.preventDefault();
      input.focus();
    } else if (event.key === 'Escape') {
      input.focus();
      hideResults();
    }
  });
  document.addEventListener('keydown', (event) => {
    if (event.key !== '/' || event.metaKey || event.ctrlKey || event.altKey) return;
    const target = event.target;
    if (target instanceof HTMLInputElement || target instanceof HTMLTextAreaElement || target.isContentEditable) return;
    event.preventDefault();
    input.focus();
  });
  document.addEventListener('click', (event) => {
    if (!container.contains(event.target)) hideResults();
  });
}

if (typeof document !== 'undefined') wireSearch();
