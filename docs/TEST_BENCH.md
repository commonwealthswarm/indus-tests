# The test bench at a glance

This page maps each part of the plan "Plan the Indus decipherment test bench"
(plan_29e43742) to the files that deliver it, so a reader can check the whole
bench in one place. Python 3 standard library only.

## Components

| Plan item | Files | Subtask |
|---|---|---|
| Corpus format, loader, synthetic fixture | `docs/CORPUS_FORMAT.md`, `indus/corpus.py` (`load_corpus`), `tests/fixtures/tiny_corpus.json`, `tests/test_corpus.py` | t_0eb13b9a |
| Private runs, ignored data | `docs/PRIVATE_RUNS.md`, `.gitignore` (`data/`, `*.private.json`) | t_0eb13b9a |
| Corpus sources (links and citations only) | `docs/CORPUS_SOURCES.md`, `tests/test_docs.py` | t_54b0c312 |
| Readings format and validator | `docs/READINGS_FORMAT.md`, `indus/readings.py` (`load_reading`, `load_readings`), `tests/fixtures/tiny_reading.json`, `tests/test_readings.py` | t_73e6ac08 |
| Seeded published readings, cited | `readings/*.json` plus their load test | t_6c78f634 |
| Scoring metrics | `indus/score.py` (`render`, `score`), `tests/test_score.py` | t_0a3d98f4 |
| Null baseline | `indus/baseline.py` (`null_baseline`), `tests/test_baseline.py` | t_13b2128e |
| Report generator | `indus/report.py` (`build_report`, `main`), `tests/fixtures/readings_dir/`, report test | t_13b2128e |
| Fast tests | `test.sh` (`python3 -m unittest discover -s tests -v`) | t_0eb13b9a |
| Method, limits, private use | `README.md` | t_60e9b38a |

## How the pieces connect

```
corpus JSON (private, outside the repo) --load_corpus--> Corpus
readings/*.json --load_readings--> [Reading, ...]

for each Reading whose sign_list matches the Corpus:
    score(Corpus, Reading)              -> six metrics
    null_baseline(..., "lexicon_hits")  -> null_mean, p_value
other Readings -> "Skipped <name>: sign_list ... does not match corpus ..."

build_report -> header, disclaimer line, Markdown table, skip lines
```

## Try it

```sh
sh test.sh
python3 -m indus.report --corpus tests/fixtures/tiny_corpus.json \
    --readings tests/fixtures/readings_dir --n 200
```

Real runs use a corpus file kept outside the repo; see
[PRIVATE_RUNS.md](PRIVATE_RUNS.md). No real inscriptions are in this
repository.

## Limits

A good score is evidence, not proof of decipherment. Coverage, consistency
and repeat_agreement say how much of the corpus a reading covers and how
tidily, not whether its values are right. Only `lexicon_hits` is tested
against chance, and a lexicon fitted to the corpus can beat the shuffled
baseline without being correct. The Indus signs may or may not encode a
language.
