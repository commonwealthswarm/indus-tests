"""Shuffled-value null baseline for a reading's score."""
import dataclasses
import math
import random

from indus.score import score


def null_baseline(corpus, reading, metric="lexicon_hits", n=1000, seed=0):
    """Compare a reading's metric with readings whose values are shuffled.

    Each of the n permutations shuffles the values among the reading's mapped
    signs (same keys, same multiset of values; a multi-valued list moves as a
    unit) using a single random.Random(seed), rescores with indus.score.score
    and reads `metric`. Returns {"observed", "null_mean", "null_sd"
    (population sd), "p_value", "n"} with
    p_value = (1 + count of null scores >= observed) / (1 + n).
    Raises ValueError if n < 1 or metric is not a key of score().

    coverage_tokens, coverage_types, full_inscriptions, consistency and
    repeat_agreement are invariant under this shuffle, so only
    assignment-dependent metrics such as lexicon_hits are meaningful.
    Qualification: the coverage metrics and full_inscriptions are always
    invariant (the mapped keys never change). consistency and
    repeat_agreement are invariant when every value is single-valued;
    consistency is also invariant when every mapped key occurs in the corpus.
    Otherwise moving a multi-valued list onto another sign can change them.
    """
    if n < 1:
        raise ValueError("n must be at least 1, got %r" % (n,))
    scores = score(corpus, reading)
    if metric not in scores:
        raise ValueError("unknown metric %r; expected one of %s"
                         % (metric, ", ".join(sorted(scores))))
    observed = scores[metric]
    keys = list(reading.values)
    pool = [reading.values[k] for k in keys]
    rng = random.Random(seed)
    null = []
    for _ in range(n):
        rng.shuffle(pool)
        shuffled = dataclasses.replace(reading, values=dict(zip(keys, pool)))
        null.append(score(corpus, shuffled)[metric])
    mean = sum(null) / n
    sd = math.sqrt(sum((x - mean) ** 2 for x in null) / n)
    p_value = (1 + sum(1 for x in null if x >= observed)) / (1 + n)
    return {"observed": observed, "null_mean": mean, "null_sd": sd,
            "p_value": p_value, "n": n}
