# Sign invariants audit: signs 1-10, corpus revision 0

Work key: indus-sign-invariants-v1|rev0|1,2,3,4,5,6,7,8,9,10
Source: indus-corpus-v1 (via query_data)

## Queries run (exactly these, nothing else)

1. `summary`
2. `sign` for sign_id 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 (10 queries)

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
| 1 | 134 | 120 | 15 | 33 | 89 | 3 | 134 | 1.00 | 1.00 | PASS | PASS | PASS | PASS | PASS |
| 2 | 21 | 21 | 7 | 14 | 0 | 0 | 21 | 0.16 | 0.16 | PASS | PASS | PASS | PASS | PASS |
| 3 | 6 | 6 | 2 | 3 | 1 | 0 | 6 | 0.04 | 0.04 | PASS | PASS | PASS | PASS | PASS |
| 4 | 2 | 2 | 1 | 0 | 1 | 0 | 2 | 0.01 | 0.01 | PASS | PASS | PASS | PASS | PASS |
| 5 | 2 | 2 | 0 | 0 | 2 | 0 | 2 | 0.01 | 0.01 | PASS | PASS | PASS | PASS | PASS |
| 6 | 5 | 5 | 4 | 1 | 0 | 0 | 5 | 0.04 | 0.04 | PASS | PASS | PASS | PASS | PASS |
| 7 | 8 | 8 | 6 | 1 | 4 | 3 | 8 | 0.06 | 0.06 | PASS | PASS | PASS | PASS | PASS |
| 8 | 105 | 105 | 2 | 103 | 0 | 0 | 105 | 0.79 | 0.79 | PASS | PASS | PASS | PASS | PASS |
| 9 | 12 | 12 | 2 | 10 | 0 | 0 | 12 | 0.09 | 0.09 | PASS | PASS | PASS | PASS | PASS |
| 10 | 6 | 5 | 0 | 5 | 1 | 0 | 6 | 0.04 | 0.04 | PASS | PASS | PASS | PASS | PASS |

Expected percent = round(10000 * occ / 13372) / 100. Every frequency_claim denominator_value is 13372, which equals nonzero_tokens.

## Unit-level checks

- Sum of occurrences = 301 <= 13372 nonzero_tokens — PASS

## Limits

These checks found no discrepancy for signs 1-10 on revision 0. That is a consistency check of the server's aggregates against each other. It does not independently confirm the transcription and proves nothing about queries not run. Nothing here concerns what any sign means.
