"""Scoring a reading (proposed decipherment) against a corpus.

These metrics are evidence about how a reading fits a corpus, not proof that it
is correct.
"""

NGRAM_SIZES = (2, 3, 4)
LEXICON_MAX_LEN = 6


def _first(value):
    return value if isinstance(value, str) else value[0]


def _single(value):
    """A string or a one-element list counts as exactly one value."""
    return isinstance(value, str) or len(value) == 1


def _ratio(num, den):
    return num / den if den else 0.0


def render(reading, signs):
    """Join each sign's value with "-".

    A multi-valued sign renders as its first value; a sign that is not a key
    of reading.values renders as "?".
    """
    return "-".join(_first(reading.values[s]) if s in reading.values else "?"
                    for s in signs)


def score(corpus, reading):
    """Score a reading against a corpus; returns a dict of six metrics.

    'Mapped' means the sign id is a key of reading.values. Each ratio metric is
    0.0 when its denominator is 0.

    - coverage_tokens: mapped sign tokens / all sign tokens.
    - coverage_types: distinct corpus signs mapped / distinct corpus signs.
    - full_inscriptions: inscriptions with every sign mapped / all inscriptions.
    - consistency: among DISTINCT signs both mapped and occurring in the
      corpus, the fraction with exactly one value (a string or a one-element
      list).
    - repeat_agreement: among DISTINCT contiguous n-grams (n=2,3,4) occurring
      in at least 2 DIFFERENT inscriptions, the fraction in which every sign
      is mapped with exactly one value. Repeats within one inscription do not
      count.
    - lexicon_hits: int count of occurrences (every position in every
      inscription) of contiguous sequences of length 1..6 containing no
      unmapped sign whose render() equals a reading.lexicon entry (0 if the
      lexicon is empty). Each occurrence counts once, even if the lexicon
      lists the same word twice.
    """
    values = reading.values
    texts = [ins.signs for ins in corpus.inscriptions]
    tokens = [s for signs in texts for s in signs]
    types = set(tokens)
    mapped_types = {s for s in types if s in values}

    coverage_tokens = _ratio(sum(1 for s in tokens if s in values), len(tokens))
    coverage_types = _ratio(len(mapped_types), len(types))
    full = sum(1 for signs in texts if all(s in values for s in signs))
    full_inscriptions = _ratio(full, len(texts))
    consistency = _ratio(sum(1 for s in mapped_types if _single(values[s])),
                         len(mapped_types))

    inscriptions_with = {}
    for signs in texts:
        grams = {tuple(signs[i:i + n])
                 for n in NGRAM_SIZES for i in range(len(signs) - n + 1)}
        for gram in grams:
            inscriptions_with[gram] = inscriptions_with.get(gram, 0) + 1
    repeated = [g for g, count in inscriptions_with.items() if count >= 2]
    agreeing = sum(1 for g in repeated
                   if all(s in values and _single(values[s]) for s in g))
    repeat_agreement = _ratio(agreeing, len(repeated))

    lexicon = set(reading.lexicon)
    lexicon_hits = 0
    if lexicon:
        for signs in texts:
            for start in range(len(signs)):
                for end in range(start + 1, min(start + LEXICON_MAX_LEN, len(signs)) + 1):
                    if signs[end - 1] not in values:
                        break  # every longer window from here contains it too
                    if render(reading, signs[start:end]) in lexicon:
                        lexicon_hits += 1

    return {
        "coverage_tokens": coverage_tokens,
        "coverage_types": coverage_types,
        "full_inscriptions": full_inscriptions,
        "consistency": consistency,
        "repeat_agreement": repeat_agreement,
        "lexicon_hits": lexicon_hits,
    }
