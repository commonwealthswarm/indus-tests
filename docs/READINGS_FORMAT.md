# Readings format

A reading is one proposed decipherment, stored as one JSON file per proposal in `readings/`:

```json
{"name": "...", "author": "...", "year": 1977, "citation": "full reference",
 "sign_list": "M77", "language": "...",
 "values": {"S1": "ka", "S2": ["ma", "mi"]},
 "lexicon": ["ka-ma"], "notes": "..."}
```

- `name` (str), `author` (str), `citation` (str, full reference), `language` (str): required.
- `year` (int): required; year of the proposal.
- `sign_list` (str): required; same codes as the corpus format (`M77`, `W2015`, `SYNTH`, ...).
- `values` (object): required, non-empty. Maps sign id to a non-empty string or a non-empty list of non-empty strings. A list means several values; a one-element list counts as a single value.
- `lexicon` (list of str, optional, default `[]`): words the author claims occur in inscriptions, written as sign values joined with `-` (e.g. `min-ko`).
- `notes` (str, optional, default `""`).

`indus.readings.load_reading(path)` returns a `Reading`; `load_readings(dir)` loads every `*.json` in a directory, sorted by file name. Both raise `ValueError` naming the file and the problem for a missing required field, empty `values`, a malformed value, a non-int `year`, or a non-string `sign_list` (or other string field).
