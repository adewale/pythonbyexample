// Source for public/editor.js, bundled by scripts/build_browser_bundles.mjs.
import { closeBrackets, closeBracketsKeymap } from '@codemirror/autocomplete';
import { defaultKeymap, history, historyKeymap, indentWithTab } from '@codemirror/commands';
import { python } from '@codemirror/lang-python';
import { bracketMatching, defaultHighlightStyle, indentOnInput, indentUnit, syntaxHighlighting } from '@codemirror/language';
import { Compartment, EditorState } from '@codemirror/state';
import { oneDarkHighlightStyle } from '@codemirror/theme-one-dark';
import { EditorView, keymap, lineNumbers } from '@codemirror/view';

const themePreference = window.matchMedia('(prefers-color-scheme: dark)');
const highlightStyle = () => themePreference.matches ? oneDarkHighlightStyle : defaultHighlightStyle;
const highlightCompartment = new Compartment();

const textarea = document.getElementById('code-editor');
const form = document.querySelector('form.runner-editor');

if (textarea && form) {
  textarea.classList.add('textarea-fallback');

  const runKeymap = [{
    key: 'Mod-Enter',
    preventDefault: true,
    run: () => {
      form.requestSubmit();
      return true;
    },
  }];

  const view = new EditorView({
    state: EditorState.create({
      doc: textarea.value,
      extensions: [
        // Run first so Mod-Enter is not taken by the default "insert blank line".
        keymap.of(runKeymap),
        history(),
        python(),
        indentUnit.of('    '),
        EditorState.tabSize.of(4),
        indentOnInput(),
        bracketMatching(),
        closeBrackets(),
        highlightCompartment.of(syntaxHighlighting(highlightStyle())),
        lineNumbers(),
        EditorView.lineWrapping,
        // Tab indents, as Python learners expect. CodeMirror keeps keyboard
        // users from being trapped: Escape then Tab moves focus onward, and
        // the hint under the editor says so.
        keymap.of([...closeBracketsKeymap, ...defaultKeymap, ...historyKeymap, indentWithTab]),
        EditorView.contentAttributes.of({
          'aria-label': textarea.getAttribute('aria-label') || 'Editable Python example code',
          'aria-describedby': 'editor-keys-hint',
        }),
        EditorView.updateListener.of((update) => {
          if (update.docChanged) textarea.value = update.state.doc.toString();
        }),
      ],
    }),
  });

  textarea.insertAdjacentElement('afterend', view.dom);
  textarea.hidden = true;
  const hint = document.getElementById('editor-keys-hint');
  if (hint) hint.hidden = false;
  themePreference.addEventListener?.('change', () => {
    view.dispatch({ effects: highlightCompartment.reconfigure(syntaxHighlighting(highlightStyle())) });
  });

  function resize() {
    view.dom.style.minHeight = '';
    const minimum = Number.parseFloat(getComputedStyle(view.dom).minHeight) || 0;
    view.dom.style.minHeight = `${Math.max(minimum, view.contentDOM.scrollHeight)}px`;
  }

  function scheduleResize() {
    requestAnimationFrame(resize);
  }

  function setValue(value) {
    view.dispatch({ changes: { from: 0, to: view.state.doc.length, insert: value } });
    textarea.value = value;
    scheduleResize();
  }

  resize();

  function syncTextarea() {
    textarea.value = view.state.doc.toString();
  }

  form.addEventListener('submit', syncTextarea);
  window.pythonByExampleEditor = { setValue, syncTextarea, resize: scheduleResize, focus: () => view.focus() };
}
