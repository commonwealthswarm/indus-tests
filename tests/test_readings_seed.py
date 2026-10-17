import unittest
from pathlib import Path

from indus.readings import load_readings


READINGS = Path(__file__).resolve().parents[1] / "readings"


class SeedReadingsTest(unittest.TestCase):
    def test_published_readings_load_and_have_citations(self):
        paths = sorted(READINGS.glob("*.json"))
        self.assertGreaterEqual(len(paths), 2)
        readings = load_readings(READINGS)
        self.assertEqual(len(readings), len(paths))
        for path, reading in zip(paths, readings):
            with self.subTest(file=path.name):
                self.assertTrue(reading.citation.strip())


if __name__ == "__main__":
    unittest.main()
