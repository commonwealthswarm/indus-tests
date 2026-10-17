import os
import re
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class DocsTest(unittest.TestCase):
    def test_corpus_sources(self):
        path = os.path.join(ROOT, "docs", "CORPUS_SOURCES.md")
        self.assertTrue(os.path.isfile(path))
        with open(path, encoding="utf-8") as f:
            text = f.read()
        sections = [s for s in text.split("\n## ")[1:] if re.search(r"https?://", s)]
        self.assertGreaterEqual(len(sections), 3)
        self.assertIn("Running privately", text)

    def test_gitignore_data(self):
        with open(os.path.join(ROOT, ".gitignore"), encoding="utf-8") as f:
            self.assertIn("data/", f.read().split())


if __name__ == "__main__":
    unittest.main()
