"""Reference token totals and sign-frequency claims (contract indus-nonzero-tokens-v1).

Sign 0 marks a lost or illegible sign: it is counted in all_tokens but excluded
from the frequency denominator (nonzero_tokens) and never gets a percent. Every
token with a sign id above 0 counts, including one marked uncertain.

A token is either an int sign id or a (sign_id, uncertain) pair. Frequencies
are counts only; they say nothing about what a sign means.
"""

CONTRACT_ID = "indus-nonzero-tokens-v1"


def _sign_id(token):
    return token[0] if isinstance(token, (tuple, list)) else token


def token_totals(inscriptions):
    """Return all_tokens, nonzero_tokens, excluded_zero_tokens and tokens.

    tokens is the legacy alias for nonzero_tokens, not the all-token count.
    """
    all_tokens = 0
    zero = 0
    for signs in inscriptions:
        for token in signs:
            all_tokens += 1
            if _sign_id(token) == 0:
                zero += 1
    nonzero = all_tokens - zero
    return {"all_tokens": all_tokens, "nonzero_tokens": nonzero,
            "excluded_zero_tokens": zero, "tokens": nonzero}


def sign_frequency_claim(inscriptions, sign_id):
    """Frequency claim for one sign, in the shape the corpus tool reports.

    occurrences counts every token of the sign; texts counts distinct
    inscriptions containing it. percent is round(10000 * occurrences /
    nonzero_tokens) / 100, or None when nonzero_tokens is 0. Sign 0 raises
    ValueError: it has no percent.
    """
    if sign_id == 0:
        raise ValueError("sign 0 (lost or illegible) has no frequency percent")
    inscriptions = [list(signs) for signs in inscriptions]
    occurrences = 0
    texts = 0
    for signs in inscriptions:
        found = sum(1 for token in signs if _sign_id(token) == sign_id)
        occurrences += found
        if found:
            texts += 1
    denominator = token_totals(inscriptions)["nonzero_tokens"]
    percent = round(10000 * occurrences / denominator) / 100 if denominator else None
    return {"kind": "sign_frequency", "sign_id": sign_id,
            "occurrences": occurrences, "texts": texts,
            "denominator": "nonzero_tokens", "denominator_value": denominator,
            "percent": percent}
