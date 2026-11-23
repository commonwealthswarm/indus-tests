# Coverage audit: sign invariants, signs 81-90 (corpus revision 0)

Work key: indus-sign-invariants-v1|rev0|81..90
Source: indus-corpus-v1 (Mahadevan & RMRL 2021, IM77/IDF80), via the Night Shift query_data tool.

## Queries run (exactly 11)
- `query_data op=summary` (1)
- `query_data op=sign sign_id=N` for N = 81..90 (10)

## Summary
corpus_revision 0; all_tokens 14153; nonzero_tokens 13372; excluded_zero_tokens 781. 13372 + 781 = 14153: **pass**.

## Per-sign checks
Positions are stored order (S1 first), not reading direction. Expected percent = round(10000*occ/13372)/100.

| sign | occ | texts | first | middle | last | alone | f+m+l-a | percent (claim) | expected | occ>=1 | texts<=occ | positions | denom | percent |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 81 | 24 | 24 | 0 | 19 | 5 | 0 | 24 | 0.18 | 0.18 | pass | pass | pass | pass | pass |
| 82 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | 0.01 | 0.01 | pass | pass | pass | pass | pass |
| 83 | 4 | 4 | 1 | 2 | 1 | 0 | 4 | 0.03 | 0.03 | pass | pass | pass | pass | pass |
| 84 | 8 | 8 | 5 | 3 | 0 | 0 | 8 | 0.06 | 0.06 | pass | pass | pass | pass | pass |
| 85 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 0.01 | 0.01 | pass | pass | pass | pass | pass |
| 86 | 149 | 148 | 68 | 70 | 12 | 1 | 149 | 1.11 | 1.11 | pass | pass | pass | pass | pass |
| 87 | 365 | 352 | 148 | 199 | 19 | 1 | 365 | 2.73 | 2.73 | pass | pass | pass | pass | pass |
| 88 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 0.01 | 0.01 | pass | pass | pass | pass | pass |
| 89 | 314 | 306 | 141 | 159 | 15 | 1 | 314 | 2.35 | 2.35 | pass | pass | pass | pass | pass |
| 90 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0.01 | 0.01 | pass | pass | pass | pass | pass |

All frequency_claim denominator_value fields equal 13372 (= summary nonzero_tokens).

## Unit checks
- Sum of occurrences over signs 81-90 = 869 <= 13372: **pass**.
- all_tokens = nonzero_tokens + excluded_zero_tokens: **pass**.

## Limits
- Arithmetic checked by hand on returned aggregates; no texts, source images or printed concordance were consulted.
- These checks showed no discrepancy; that is not proof about anything not queried, and a 10-sign unit cannot verify corpus-wide totals.
- Consistency check only; no claims about what any sign means.
