"""Reference counter for a contiguous sign sequence in a list of inscriptions.

This reproduces two numbers the corpus tool reports for a sequence, so they can
be checked independently. Tokens are treated as opaque values; how lost or
illegible tokens are handled is decided elsewhere.
"""


def count_sequence(inscriptions, sequence):
    """Count a contiguous sequence; returns {"matches": int, "texts": int}.

    - matches: every position in every inscription where the sequence starts.
      Overlapping occurrences all count: (5, 5) matches twice in 5, 5, 5.
    - texts: number of distinct inscriptions containing the sequence at least
      once.

    inscriptions is an iterable of token sequences. An empty sequence raises
    ValueError, since it would match everywhere.
    """
    seq = list(sequence)
    if not seq:
        raise ValueError("sequence must not be empty")
    n = len(seq)
    matches = 0
    texts = 0
    for signs in inscriptions:
        signs = list(signs)
        found = sum(1 for i in range(len(signs) - n + 1) if signs[i:i + n] == seq)
        matches += found
        if found:
            texts += 1
    return {"matches": matches, "texts": texts}
