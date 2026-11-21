# Corpus audit: top-10 sign frequency, position and denominator invariants

Source: query_data, `indus-corpus-v1` (Mahadevan & RMRL 2021, IM77/IDF80),
corpus_revision 0. Checked on 2026-10-27.

## Queries run (12)

1. `summary` (once)
2. `top_signs` with limit 10
3. `sign` for 342, 99, 59, 267, 87, 176, 328, 89, 67, 169

## Totals

- all_tokens 14153 = nonzero_tokens 13372 + excluded_zero_tokens 781: **pass**
- Sum of top-10 occurrences = 4677, which is <= 13372: **pass**

## Per sign

Checks: (A) top_signs n = sign occurrences; (B) first + middle + last - alone
= occurrences; (C) denominator_value = 13372; (D) percent =
round(10000 * occ / 13372) / 100.

| sign | occ | texts | first | middle | last | alone | percent | A | B | C | D |
|-----:|----:|------:|------:|-------:|-----:|------:|--------:|---|---|---|---|
| 342 | 1395 | 1378 | 4 | 420 | 974 | 3 | 10.43 | pass | pass | pass | pass |
| 99 | 649 | 648 | 2 | 625 | 22 | 0 | 4.85 | pass | pass | pass | pass |
| 59 | 381 | 370 | 54 | 309 | 36 | 18 | 2.85 | pass | pass | pass | pass |
| 267 | 376 | 374 | 299 | 62 | 16 | 1 | 2.81 | pass | pass | pass | pass |
| 87 | 365 | 352 | 148 | 199 | 19 | 1 | 2.73 | pass | pass | pass | pass |
| 176 | 355 | 343 | 1 | 38 | 317 | 1 | 2.65 | pass | pass | pass | pass |
| 328 | 323 | 313 | 20 | 29 | 275 | 1 | 2.42 | pass | pass | pass | pass |
| 89 | 314 | 306 | 141 | 159 | 15 | 1 | 2.35 | pass | pass | pass | pass |
| 67 | 279 | 279 | 70 | 209 | 2 | 2 | 2.09 | pass | pass | pass | pass |
| 169 | 240 | 226 | 4 | 106 | 131 | 1 | 1.79 | pass | pass | pass | pass |

## Limits

I did the arithmetic by hand from the returned values and ran no code. The
checks I ran showed no discrepancy. That says nothing about signs or
queries outside this list, or about other corpus snapshots. Positions are in
stored order, which is not reading direction. Nothing here concerns what any
sign means.
