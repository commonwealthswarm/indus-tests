"""Report: score every reading in a directory against one corpus.

Usage: python3 -m indus.report --corpus PATH --readings DIR
       [--n 1000] [--seed 0] [--out FILE]
"""
import argparse
import sys

from indus.baseline import null_baseline
from indus.corpus import load_corpus
from indus.readings import load_readings
from indus.score import score

DISCLAIMER = "A good score is evidence, not proof of decipherment."
COLUMNS = ("name", "author", "year", "coverage_tokens", "coverage_types",
           "full_inscriptions", "consistency", "repeat_agreement",
           "lexicon_hits", "null_mean", "p_value")


def _cell(value):
    if isinstance(value, float):
        return "%.3f" % value
    return str(value).replace("|", "\\|")


def build_report(corpus, readings, n=1000, seed=0):
    """Return the report text: header lines, one table row per reading whose
    sign_list matches the corpus, then one skip line per other reading."""
    lines = ["Corpus: %s" % corpus.source,
             "License: %s" % corpus.license,
             "Inscriptions: %d" % len(corpus.inscriptions),
             DISCLAIMER,
             "",
             "| " + " | ".join(COLUMNS) + " |",
             "|" + "---|" * len(COLUMNS)]
    skipped = []
    for reading in readings:
        if reading.sign_list != corpus.sign_list:
            skipped.append("Skipped %s: sign_list %s does not match corpus %s"
                           % (reading.name, reading.sign_list, corpus.sign_list))
            continue
        row = dict(score(corpus, reading))
        baseline = null_baseline(corpus, reading, "lexicon_hits", n=n, seed=seed)
        row.update(name=reading.name, author=reading.author, year=reading.year,
                   null_mean=float(baseline["null_mean"]),
                   p_value=float(baseline["p_value"]))
        lines.append("| " + " | ".join(_cell(row[c]) for c in COLUMNS) + " |")
    if skipped:
        lines.append("")
        lines.extend(skipped)
    return "\n".join(lines) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="python3 -m indus.report",
        description="Score readings against a corpus with a shuffled null baseline.")
    parser.add_argument("--corpus", required=True, help="corpus JSON file")
    parser.add_argument("--readings", required=True, help="directory of reading JSON files")
    parser.add_argument("--n", type=int, default=1000, help="null permutations (default 1000)")
    parser.add_argument("--seed", type=int, default=0, help="random seed (default 0)")
    parser.add_argument("--out", help="write the report here instead of stdout")
    args = parser.parse_args(argv)

    text = build_report(load_corpus(args.corpus), load_readings(args.readings),
                        n=args.n, seed=args.seed)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(text)
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
