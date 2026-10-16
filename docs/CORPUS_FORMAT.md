# Corpus format

A corpus is one JSON file:

```json
{"source": "...", "license": "...", "sign_list": "M77",
 "inscriptions": [{"id": "...", "site": "..." , "signs": ["S1", "S2"]}]}
```

- `source` (str): where the corpus comes from.
- `license` (str): license of the data.
- `sign_list` (str): sign numbering system, e.g. `M77` (Mahadevan 1977), `W2015` (Wells), `SYNTH` (synthetic fixtures).
- `inscriptions`: list of objects with `id` (str, unique), `site` (str or null), `signs` (non-empty list of sign id strings).

**Direction convention:** `signs` are in reading order; the first element is the *rightmost* sign on the original object.

`indus.corpus.load_corpus(path)` raises `ValueError` for a missing top-level field, a missing inscription field, duplicate inscription ids, or an empty signs list.
