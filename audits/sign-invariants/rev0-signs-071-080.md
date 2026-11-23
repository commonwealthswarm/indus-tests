# Coverage audit: sign invariants, signs 71-80 (corpus revision 0)

Work key: indus-sign-invariants-v1|rev0|71..80
Source: indus-corpus-v1 (Mahadevan & RMRL 2021, IM77/IDF80), via the Night Shift query_data tool.

## Queries run (exactly 11)
- `query_data op=summary` (1)
- `query_data op=sign sign_id=N` for N = 71..80 (10)

## Summary
corpus_revision 0; all_tokens 14153; nonzero_tokens 13372; excluded_zero_tokens 781. 13372 + 781 = 14153: **pass**.

## Per-sign checks
Positions are stored order (S1 first), not reading direction. Expected percent = round(10000*occ/13372)/100.

| sign | occ | texts | first | middle | last | alone | f+m+l-a | percent (claim) | expected | occ>=1 | texts<=occ | positions | denom | percent |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 71 | 7 | 7 | 0 | 2 | 5 | 0 | 7 | 0.05 | 0.05 | pass | pass | pass | pass | pass |
| 72 | 188 | 188 | 40 | 148 | 0 | 0 | 188 | 1.41 | 1.41 | pass | pass | pass | pass | pass |
| 73 | 8 | 8 | 5 | 0 | 4 | 1 | 8 | 0.06 | 0.06 | pass | pass | pass | pass | pass |
| 74 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | 0.01 | 0.01 | pass | pass | pass | pass | pass |
| 75 | 13 | 13 | 4 | 8 | 1 | 0 | 13 | 0.1 | 0.10 | pass | pass | pass | pass | pass |
| 76 | 15 | 14 | 10 | 5 | 0 | 0 | 15 | 0.11 | 0.11 | pass | pass | pass | pass | pass |
| 77 | 2 | 2 | 1 | 1 | 0 | 0 | 2 | 0.01 | 0.01 | pass | pass | pass | pass | pass |
| 78 | 8 | 8 | 1 | 7 | 0 | 0 | 8 | 0.06 | 0.06 | pass | pass | pass | pass | pass |
| 79 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 0.01 | 0.01 | pass | pass | pass | pass | pass |
| 80 | 4 | 4 | 3 | 1 | 0 | 0 | 4 | 0.03 | 0.03 | pass | pass | pass | pass | pass |

All frequency_claim denominator_value fields equal 13372 (= summary nonzero_tokens).

## Unit checks
- Sum of occurrences over signs 71-80 = 248 <= 13372: **pass**.
- all_tokens = nonzero_tokens + excluded_zero_tokens: **pass**.

## Limits
- Arithmetic checked by hand on returned aggregates; no texts, source images or printed concordance were consulted.
- These checks showed no discrepancy; that is not proof about anything not queried, and a 10-sign unit cannot verify corpus-wide totals.
- Consistency check only; no claims about what any sign means.
