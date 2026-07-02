import { EditorState } from 'https://esm.sh/@codemirror/state@6.5.2';
import { EditorView, lineNumbers } from 'https://esm.sh/@codemirror/view@6.41.1?deps=@codemirror/state@6.5.2';
import { defaultHighlightStyle, syntaxHighlighting } from 'https://esm.sh/@codemirror/language@6.12.3?deps=@codemirror/state@6.5.2,@codemirror/view@6.41.1';
import { python } from 'https://esm.sh/@codemirror/lang-python@6.2.1?deps=@codemirror/state@6.5.2,@codemirror/view@6.41.1,@codemirror/language@6.12.3';
import { oneDarkHighlightStyle } from 'https://esm.sh/@codemirror/theme-one-dark@6.1.3?deps=@codemirror/state@6.5.2,@codemirror/view@6.41.1,@codemirror/language@6.12.3';

const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
const highlightStyle = prefersDark ? oneDarkHighlightStyle : defaultHighlightStyle;

const textarea = document.getElementById('code-editor');
const form = document.querySelector('form.runner-editor');

if (textarea && form) {
  textarea.classList.add('textarea-fallback');

  const view = new EditorView({
    state: EditorState.create({
      doc: textarea.value,
      extensions: [
        python(),
        syntaxHighlighting(highlightStyle),
        lineNumbers(),
        EditorView.lineWrapping,
        EditorView.updateListener.of((update) => {
          if (update.docChanged) textarea.value = update.state.doc.toString();
        }),
      ],
    }),
  });

  textarea.insertAdjacentElement('afterend', view.dom);
  textarea.hidden = true;

  function setValue(value) {
    view.dispatch({ changes: { from: 0, to: view.state.doc.length, insert: value } });
    textarea.value = value;
  }

  function syncTextarea() {
    textarea.value = view.state.doc.toString();
  }

  form.addEventListener('submit', syncTextarea);
  window.pythonByExampleEditor = { setValue, syncTextarea };
}
