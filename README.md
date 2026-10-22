# Indus script: testing proposed decipherments

This repository scores published proposals for reading the Indus script
("readings") against a corpus of inscriptions, and compares each score with
a shuffled-value null baseline. It is a test bench. It does not decipher
anything.

**A good score is evidence, not proof of decipherment.** A reading can score
well by overfitting: if its lexicon was built by looking at the corpus, its
words will match the corpus whatever the script actually means. The Indus
signs may or may not encode a language, and none of these numbers settles
that.

Every change arrives as a pull request from an agent, passes `sh test.sh`
and is reviewed by another member's agent before it is merged.

## Run the tests

```sh
sh test.sh
```

This runs `python3 -m unittest discover -s tests -v` (Python 3 standard
library only). All tests use the synthetic fixtures in `tests/fixtures/`.

## Try the report on the synthetic fixture

```sh
python3 -m indus.report --corpus tests/fixtures/tiny_corpus.json \
    --readings tests/fixtures/readings_dir --n 200
```

This prints the corpus source, license and inscription count, the line
"A good score is evidence, not proof of decipherment.", a Markdown table
with one row per reading, and a `Skipped ...` line for any reading whose
`sign_list` does not match the corpus (here `mismatched.json`, which uses
`M77` against the `SYNTH` corpus). Options: `--n` (number of permutations,
default 1000), `--seed` (default 0) and `--out FILE` (write to a file
instead of stdout).

## Real corpora: private runs only

There are **no real inscriptions in this repository**, not even small cited
samples. Never commit, paste into lab notes or upload a real corpus or any
real inscription sequence. The available datasets, their sign numbering and
the rights evidence for each are documented, as links and citations only, in
[docs/CORPUS_SOURCES.md](docs/CORPUS_SOURCES.md). Settle the source's terms
yourself before you make a private copy.

Convert your own copy to the format in
[docs/CORPUS_FORMAT.md](docs/CORPUS_FORMAT.md), keep it outside the repo,
and pass it by path:

```sh
python3 -m indus.report --corpus /path/outside/repo/corpus.json --readings readings/
```

See [docs/PRIVATE_RUNS.md](docs/PRIVATE_RUNS.md). `data/` and
`*.private.json` are git-ignored as an extra safeguard, but that does not
make publishing them acceptable. Readings are compared only with a corpus
that uses the same `sign_list` (for example `M77`).

## What the metrics mean

A sign is *mapped* if it is a key of the reading's `values`. Each ratio is
0.0 when its denominator is 0. Definitions are in `indus/score.py`.

- **coverage_tokens**: share of all sign occurrences in the corpus that are
  mapped.
- **coverage_types**: share of the distinct signs in the corpus that are
  mapped.
- **full_inscriptions**: share of inscriptions in which every sign is
  mapped.
- **consistency**: among distinct signs that are both mapped and present in
  the corpus, the share that have exactly one value (a string or a
  one-element list).
- **repeat_agreement**: among distinct runs of 2, 3 or 4 adjacent signs that
  occur in at least two different inscriptions, the share in which every sign
  is mapped with exactly one value.
- **lexicon_hits**: how many times (counting every position in every
  inscription) a run of 1 to 6 adjacent, all-mapped signs renders as a word
  in the reading's `lexicon`. Rendering joins each sign's value with `-`; a
  multi-valued sign uses its first value. Runs that contain an unmapped sign
  never match.

For example, if `S1` = `ka` and `S2` = `ma` and the lexicon contains
`ka-ma`, each occurrence of `S1, S2` in the corpus adds one hit.

The first five metrics describe how much of the corpus a reading covers and
how tidily it does so. They say nothing about whether its values are right:
any arbitrary assignment of values to the same signs gets the same numbers.

## The shuffled null baseline

`indus.baseline.null_baseline` keeps the reading's set of mapped signs and
shuffles its values among them: same keys, same multiset of values, and a
multi-valued list moves as one unit. It does this `n` times with one seeded
`random.Random`, rescores each shuffled reading and reports `observed`,
`null_mean`, `null_sd` (population sd), `n` and

    p_value = (1 + number of shuffled scores >= observed) / (1 + n)

Coverage (`coverage_tokens`, `coverage_types`, `full_inscriptions`),
`consistency` and `repeat_agreement` are unchanged by this shuffle, so the
report tests only `lexicon_hits` against chance. (Strictly, the coverage
metrics never change. `consistency` and `repeat_agreement` never change for
readings with one value per sign; with multi-valued signs they can move a
little, but the report does not test them.) A small p-value means the
reading's own sign-to-value assignment matches its lexicon more often than
shuffled assignments do. It does not rule out a lexicon fitted to the
corpus, and it does not show that the values are correct.

## Adding a reading

1. Create `readings/<short-name>.json` in the format of
   [docs/READINGS_FORMAT.md](docs/READINGS_FORMAT.md): `name`, `author`,
   `year`, full `citation`, `sign_list`, `language`, `values` and optionally
   `lexicon` and `notes`.
2. Copy values and lexicon words only from the cited publication, using its
   own sign numbering. Never invent, normalise or "fix" a value. If the
   source numbers signs differently from the corpus, record its `sign_list`
   honestly; the report will skip it instead of comparing mismatched ids.
3. Do not put any inscription sequence in the reading or its notes.
4. Check that it loads, then run the tests:

```sh
python3 -c "from indus.readings import load_readings; print(len(load_readings('readings')))"
sh test.sh
```

A synthetic example (see `tests/fixtures/tiny_reading.json`):

```json
{"name": "Synthetic test reading", "author": "Night Shift fixture", "year": 2026,
 "citation": "Synthetic test fixture; not a published reading.",
 "sign_list": "SYNTH", "language": "synthetic",
 "values": {"S1": "ka", "S2": "ma", "S3": "ta", "S4": "ri", "S5": "nu", "S6": "pa"},
 "lexicon": ["ka-ma", "ta-ri-nu"]}
```

## Documents

- [docs/CORPUS_FORMAT.md](docs/CORPUS_FORMAT.md): corpus JSON schema and
  reading-order convention.
- [docs/READINGS_FORMAT.md](docs/READINGS_FORMAT.md): reading JSON schema.
- [docs/CORPUS_SOURCES.md](docs/CORPUS_SOURCES.md): datasets, numbering and
  terms (links and citations only).
- [docs/PRIVATE_RUNS.md](docs/PRIVATE_RUNS.md): the rule for keeping real
  corpora outside the repo.
