# Coverage audit: sign invariants, signs 61-70 (corpus revision 0)

Work key: indus-sign-invariants-v1|rev0|61..70
Source: indus-corpus-v1 (Mahadevan & RMRL 2021, IM77/IDF80), via the Night Shift query_data tool.

## Queries run (exactly 11)
- `query_data op=summary` (1)
- `query_data op=sign sign_id=N` for N = 61..70 (10)

## Summary
corpus_revision 0; all_tokens 14153; nonzero_tokens 13372; excluded_zero_tokens 781. 13372 + 781 = 14153: **pass**.

## Per-sign checks
Positions are stored order (S1 first), not reading direction. Expected percent = round(10000*occ/13372)/100.

| sign | occ | texts | first | middle | last | alone | f+m+l-a | percent (claim) | expected | occ>=1 | texts<=occ | positions | denom | percent |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 61 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | 0.01 | 0.01 | pass | pass | pass | pass | pass |
| 62 | 13 | 13 | 0 | 13 | 0 | 0 | 13 | 0.1 | 0.10 | pass | pass | pass | pass | pass |
| 63 | 10 | 10 | 8 | 2 | 8 | 8 | 10 | 0.07 | 0.07 | pass | pass | pass | pass | pass |
| 64 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | 0.01 | 0.01 | pass | pass | pass | pass | pass |
| 65 | 216 | 216 | 78 | 137 | 2 | 1 | 216 | 1.62 | 1.62 | pass | pass | pass | pass | pass |
| 66 | 19 | 19 | 4 | 5 | 11 | 1 | 19 | 0.14 | 0.14 | pass | pass | pass | pass | pass |
| 67 | 279 | 279 | 70 | 209 | 2 | 2 | 279 | 2.09 | 2.09 | pass | pass | pass | pass | pass |
| 68 | 9 | 9 | 0 | 2 | 7 | 0 | 9 | 0.07 | 0.07 | pass | pass | pass | pass | pass |
| 69 | 4 | 4 | 3 | 1 | 2 | 2 | 4 | 0.03 | 0.03 | pass | pass | pass | pass | pass |
| 70 | 73 | 73 | 17 | 55 | 1 | 0 | 73 | 0.55 | 0.55 | pass | pass | pass | pass | pass |

All frequency_claim denominator_value fields equal 13372 (= summary nonzero_tokens).

## Unit checks
- Sum of occurrences over signs 61-70 = 626 <= 13372: **pass**.
- all_tokens = nonzero_tokens + excluded_zero_tokens: **pass**.

## Limits
- Arithmetic checked by hand on returned aggregates; no texts, source images or printed concordance were consulted.
- These checks showed no discrepancy; that is not proof about anything not queried, and a 10-sign unit cannot verify corpus-wide totals.
- Consistency check only; no claims about what any sign means.
