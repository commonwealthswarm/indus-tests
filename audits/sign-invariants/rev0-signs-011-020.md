# Sign invariants audit: signs 11-20, corpus revision 0

Work key: indus-sign-invariants-v1|rev0|11,12,13,14,15,16,17,18,19,20
Source: indus-corpus-v1 (via query_data)

## Queries run (exactly these, nothing else)

1. `summary`
2. `sign` for sign_id 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 (10 queries)

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
| 11 | 2 | 2 | 1 | 1 | 0 | 0 | 2 | 0.01 | 0.01 | PASS | PASS | PASS | PASS | PASS |
| 12 | 80 | 80 | 2 | 9 | 70 | 1 | 80 | 0.60 | 0.60 | PASS | PASS | PASS | PASS | PASS |
| 13 | 1 | 1 | 0 | 0 | 1 | 0 | 1 | 0.01 | 0.01 | PASS | PASS | PASS | PASS | PASS |
| 14 | 13 | 13 | 0 | 2 | 11 | 0 | 13 | 0.10 | 0.10 | PASS | PASS | PASS | PASS | PASS |
| 15 | 126 | 126 | 4 | 30 | 95 | 3 | 126 | 0.94 | 0.94 | PASS | PASS | PASS | PASS | PASS |
| 16 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 0.01 | 0.01 | PASS | PASS | PASS | PASS | PASS |
| 17 | 91 | 91 | 38 | 49 | 4 | 0 | 91 | 0.68 | 0.68 | PASS | PASS | PASS | PASS | PASS |
| 18 | 27 | 27 | 7 | 20 | 0 | 0 | 27 | 0.20 | 0.20 | PASS | PASS | PASS | PASS | PASS |
| 19 | 8 | 8 | 0 | 7 | 1 | 0 | 8 | 0.06 | 0.06 | PASS | PASS | PASS | PASS | PASS |
| 20 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 0.01 | 0.01 | PASS | PASS | PASS | PASS | PASS |

Expected percent = round(10000 * occ / 13372) / 100. Every frequency_claim denominator_value is 13372, which equals nonzero_tokens.

## Unit-level checks

- Sum of occurrences = 350 <= 13372 nonzero_tokens — PASS

## Limits

These checks found no discrepancy for signs 11-20 on revision 0. That is a consistency check of the server's aggregates against each other. It does not independently confirm the transcription and proves nothing about queries not run. Nothing here concerns what any sign means.
