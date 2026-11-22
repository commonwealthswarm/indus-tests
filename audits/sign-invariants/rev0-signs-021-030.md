# Sign invariants audit: signs 21-30, corpus revision 0

Work key: indus-sign-invariants-v1|rev0|21,22,23,24,25,26,27,28,29,30
Source: indus-corpus-v1 (via query_data)

## Queries run (exactly these, nothing else)

1. `summary`
2. `sign` for sign_id 21, 22, 23, 24, 25, 26, 27, 28, 29, 30 (10 queries)

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
| 21 | 2 | 1 | 0 | 2 | 0 | 0 | 2 | 0.01 | 0.01 | PASS | PASS | PASS | PASS | PASS |
| 22 | 3 | 3 | 1 | 2 | 0 | 0 | 3 | 0.02 | 0.02 | PASS | PASS | PASS | PASS | PASS |
| 23 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 0.01 | 0.01 | PASS | PASS | PASS | PASS | PASS |
| 24 | 2 | 2 | 0 | 1 | 1 | 0 | 2 | 0.01 | 0.01 | PASS | PASS | PASS | PASS | PASS |
| 25 | 53 | 53 | 10 | 38 | 5 | 0 | 53 | 0.40 | 0.40 | PASS | PASS | PASS | PASS | PASS |
| 26 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 0.01 | 0.01 | PASS | PASS | PASS | PASS | PASS |
| 27 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0.01 | 0.01 | PASS | PASS | PASS | PASS | PASS |
| 28 | 50 | 50 | 17 | 28 | 5 | 0 | 50 | 0.37 | 0.37 | PASS | PASS | PASS | PASS | PASS |
| 29 | 3 | 3 | 2 | 0 | 1 | 0 | 3 | 0.02 | 0.02 | PASS | PASS | PASS | PASS | PASS |
| 30 | 2 | 2 | 1 | 0 | 1 | 0 | 2 | 0.01 | 0.01 | PASS | PASS | PASS | PASS | PASS |

Expected percent = round(10000 * occ / 13372) / 100. Every frequency_claim denominator_value is 13372, which equals nonzero_tokens. Sign 21 has 2 occurrences in 1 text, consistent with texts <= occurrences.

## Unit-level checks

- Sum of occurrences = 119 <= 13372 nonzero_tokens — PASS

## Limits

These checks found no discrepancy for signs 21-30 on revision 0. That is a consistency check of the server's aggregates against each other. It does not independently confirm the transcription and proves nothing about queries not run. Nothing here concerns what any sign means.
