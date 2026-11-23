# Coverage audit: sign invariants, signs 51-60 (corpus revision 0)

Work key: indus-sign-invariants-v1|rev0|51..60
Source: indus-corpus-v1 (Mahadevan & RMRL 2021, IM77/IDF80), via the Night Shift query_data tool.

## Queries run (exactly 11)
- `query_data op=summary` (1)
- `query_data op=sign sign_id=N` for N = 51..60 (10)

## Summary
corpus_revision 0; all_tokens 14153; nonzero_tokens 13372; excluded_zero_tokens 781. 13372 + 781 = 14153: **pass**.

## Per-sign checks
Positions are stored order (S1 first), not reading direction. Expected percent = round(10000*occ/13372)/100.

| sign | occ | texts | first | middle | last | alone | f+m+l-a | percent (claim) | expected | occ>=1 | texts<=occ | positions | denom | percent |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 51 | 105 | 105 | 26 | 75 | 5 | 1 | 105 | 0.79 | 0.79 | pass | pass | pass | pass | pass |
| 52 | 1 | 1 | 0 | 0 | 1 | 0 | 1 | 0.01 | 0.01 | pass | pass | pass | pass | pass |
| 53 | 130 | 130 | 32 | 96 | 2 | 0 | 130 | 0.97 | 0.97 | pass | pass | pass | pass | pass |
| 54 | 19 | 17 | 9 | 9 | 1 | 0 | 19 | 0.14 | 0.14 | pass | pass | pass | pass | pass |
| 55 | 4 | 4 | 1 | 3 | 0 | 0 | 4 | 0.03 | 0.03 | pass | pass | pass | pass | pass |
| 56 | 8 | 8 | 2 | 4 | 2 | 0 | 8 | 0.06 | 0.06 | pass | pass | pass | pass | pass |
| 57 | 7 | 7 | 2 | 4 | 1 | 0 | 7 | 0.05 | 0.05 | pass | pass | pass | pass | pass |
| 58 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | 0.05 | 0.05 | pass | pass | pass | pass | pass |
| 59 | 381 | 370 | 54 | 309 | 36 | 18 | 381 | 2.85 | 2.85 | pass | pass | pass | pass | pass |
| 60 | 29 | 29 | 3 | 5 | 22 | 1 | 29 | 0.22 | 0.22 | pass | pass | pass | pass | pass |

All frequency_claim denominator_value fields equal 13372 (= summary nonzero_tokens).

## Unit checks
- Sum of occurrences over signs 51-60 = 691 <= 13372: **pass**.
- all_tokens = nonzero_tokens + excluded_zero_tokens: **pass**.

## Limits
- Arithmetic checked by hand on returned aggregates; no texts, source images or printed concordance were consulted.
- These checks showed no discrepancy; that is not proof about anything not queried, and a 10-sign unit cannot verify corpus-wide totals.
- Consistency check only; no claims about what any sign means.
