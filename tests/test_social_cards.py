import json
import tempfile
import unittest
from io import BytesIO
from pathlib import Path

from PIL import Image

from scripts import build_social_cards as cards


class SocialCardProvenanceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.output = Path(self.temp.name)
        self.saved_output = cards.OUTPUT_DIR
        self.saved_manifest = cards.PROVENANCE_PATH
        cards.OUTPUT_DIR = self.output
        cards.PROVENANCE_PATH = self.output / 'manifest.json'

    def tearDown(self):
        cards.OUTPUT_DIR = self.saved_output
        cards.PROVENANCE_PATH = self.saved_manifest
        self.temp.cleanup()

    def _write_current(self, sources):
        self.output.mkdir(exist_ok=True)
        cards.PROVENANCE_PATH.write_text(json.dumps(cards.provenance(sources)))
        buffer = BytesIO()
        Image.new('RGB', (1200, 630), '#fff').save(buffer, format='JPEG')
        for name in cards.provenance(sources)['inputs']:
            (self.output / name).write_bytes(buffer.getvalue())

    def test_current_provenance_and_exact_jpeg_set_pass(self):
        sources = {'home': '<html>home</html>', 'values': '<html>values</html>'}
        self._write_current(sources)
        self.assertEqual(cards.check_current(sources), [])

    def test_changed_input_missing_and_orphan_cards_fail(self):
        sources = {'home': '<html>old</html>'}
        self._write_current(sources)
        (self.output / 'orphan.jpg').write_bytes(b'jpeg')
        failures = cards.check_current({'home': '<html>new</html>', 'values': '<html>values</html>'})
        self.assertTrue(any('provenance' in failure for failure in failures))
        self.assertTrue(any('missing social card values.jpg' in failure for failure in failures))
        self.assertTrue(any('unexpected stale social card orphan.jpg' in failure for failure in failures))

    def test_corrupt_and_wrong_size_cards_fail(self):
        sources = {'home': '<html>home</html>'}
        self._write_current(sources)
        valid_jpeg = (self.output / 'home.jpg').read_bytes()
        (self.output / 'home.jpg').write_bytes(b'not-a-jpeg')
        self.assertTrue(any('invalid JPEG' in failure for failure in cards.check_current(sources)))

        (self.output / 'home.jpg').write_bytes(valid_jpeg[:-10])
        self.assertTrue(any('invalid JPEG' in failure for failure in cards.check_current(sources)))

        buffer = BytesIO()
        Image.new('RGB', (1, 1), '#fff').save(buffer, format='JPEG')
        (self.output / 'home.jpg').write_bytes(buffer.getvalue())
        self.assertTrue(any('expected 1200x630' in failure for failure in cards.check_current(sources)))


if __name__ == '__main__':
    unittest.main()
