# Reproducibility manifests

`indus/manifest.py` records where a test-bench result came from so it can be
re-verified later. A manifest is JSON with:

| field | meaning |
|---|---|
| `manifest_version` | currently `1` |
| `source_paths`, `source_sha256` | source/input file(s) and one combined hash |
| `corpus_path`, `corpus_sha256` | corpus JSON, hashed canonically (sorted keys, no extra whitespace, UTF-8) |
| `code_paths`, `code_sha256` | counting code files, listed by path, combined hash |
| `semantics` | declared count semantics (see below) |
| `counts_path`, `counts_sha256` | counts output, hashed canonically |

Several files are combined by hashing `path NUL sha256 LF` lines in the order
listed. Relative paths are resolved from the manifest's own directory.

Supported semantics (data in `SUPPORTED_SEMANTICS`; all four keys required):

- `sequence_matches`: `overlapping` or `non_overlapping`
- `sequence_texts`: `distinct_inscriptions`
- `denominator`: `nonzero_tokens` or `all_tokens`
- `zero_tokens`: `excluded` or `included`

`denominator=nonzero_tokens` with `zero_tokens=included`, and
`denominator=all_tokens` with `zero_tokens=excluded`, are rejected as
contradictory.

```sh
python3 -m indus.manifest build --source in.txt --corpus corpus.json \
    --code indus/score.py --counts counts.json \
    --semantics sequence_matches=overlapping \
    --semantics sequence_texts=distinct_inscriptions \
    --semantics denominator=nonzero_tokens --semantics zero_tokens=excluded \
    --out manifest.json
python3 -m indus.manifest check manifest.json   # exit 0 on match, 1 otherwise
```

Each mismatch is reported on its own line naming the hash or field. Keep
manifests for real corpora outside the repository, like the corpora
themselves.
