# Sign invariants audit: signs 31-40, corpus revision 0

Work key: indus-sign-invariants-v1|rev0|31,32,33,34,35,36,37,38,39,40
Source: indus-corpus-v1 (via query_data)

## Queries run (exactly these, nothing else)

1. `summary`
2. `sign` for sign_id 31, 32, 33, 34, 35, 36, 37, 38, 39, 40 (10 queries)

## Summary values

- corpus_revision: 0
- all_tokens: 14153
- nonzero_tokens: 13372
- excluded_zero_tokens: 781
- Check all_tokens = nonzero + excluded_zero: 13372 + 781 = 14153 — PASS

## Per-sign results

Positions are in stored order, which is not reading direction.

| sign | occ | texts | first | middle | last | alone | f+m+l-alone | percent | expected % | occ>=1 | texts<=occ | positions | denom | percent |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 31 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0.01 | 0.01 | PASS | PASS | PASS | PASS | PASS |
| 32 | 11 | 11 | 2 | 8 | 1 | 0 | 11 | 0.08 | 0.08 | PASS | PASS | PASS | PASS | PASS |
| 33 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | 0.01 | 0.01 | PASS | PASS | PASS | PASS | PASS |
| 34 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0.01 | 0.01 | PASS | PASS | PASS | PASS | PASS |
| 35 | 4 | 4 | 3 | 1 | 0 | 0 | 4 | 0.03 | 0.03 | PASS | PASS | PASS | PASS | PASS |
| 36 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | 0.01 | 0.01 | PASS | PASS | PASS | PASS | PASS |
| 37 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 0.01 | 0.01 | PASS | PASS | PASS | PASS | PASS |
| 38 | 6 | 6 | 2 | 3 | 2 | 1 | 6 | 0.04 | 0.04 | PASS | PASS | PASS | PASS | PASS |
| 39 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | 0.01 | 0.01 | PASS | PASS | PASS | PASS | PASS |
| 40 | 14 | 14 | 8 | 2 | 7 | 3 | 14 | 0.10 | 0.10 | PASS | PASS | PASS | PASS | PASS |

Expected percent = round(10000 * occ / 13372) / 100. Every frequency_claim denominator_value is 13372, which equals nonzero_tokens.

## Unit-level checks

- Sum of occurrences = 44 <= 13372 nonzero_tokens — PASS

## Limits

These checks found no discrepancy for signs 31-40 on revision 0. That is a consistency check of the server's aggregates against each other. It does not independently confirm the transcription and proves nothing about queries not run. Nothing here concerns what any sign means.
