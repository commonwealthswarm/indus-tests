# Coverage audit: sign invariants, signs 41-50 (corpus revision 0)

Work key: indus-sign-invariants-v1|rev0|41..50
Source: indus-corpus-v1 (Mahadevan & RMRL 2021, IM77/IDF80), via the Night Shift query_data tool.

## Queries run (exactly 11)
- `query_data op=summary` (1)
- `query_data op=sign sign_id=N` for N = 41, 42, 43, 44, 45, 46, 47, 48, 49, 50 (10)

## Summary
corpus_revision 0; all_tokens 14153; nonzero_tokens 13372; excluded_zero_tokens 781. 13372 + 781 = 14153: **pass**.

## Per-sign checks
Positions are stored order (S1 first), not reading direction. Expected percent = round(10000*occ/13372)/100.

| sign | occ | texts | first | middle | last | alone | f+m+l-a | percent (claim) | expected | occ>=1 | texts<=occ | positions | denom | percent |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 41 | 20 | 20 | 14 | 6 | 0 | 0 | 20 | 0.15 | 0.15 | pass | pass | pass | pass | pass |
| 42 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 0.01 | 0.01 | pass | pass | pass | pass | pass |
| 43 | 2 | 2 | 1 | 1 | 0 | 0 | 2 | 0.01 | 0.01 | pass | pass | pass | pass | pass |
| 44 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0.01 | 0.01 | pass | pass | pass | pass | pass |
| 45 | 4 | 4 | 3 | 0 | 1 | 0 | 4 | 0.03 | 0.03 | pass | pass | pass | pass | pass |
| 46 | 1 | 1 | 0 | 0 | 1 | 0 | 1 | 0.01 | 0.01 | pass | pass | pass | pass | pass |
| 47 | 16 | 16 | 6 | 10 | 1 | 1 | 16 | 0.12 | 0.12 | pass | pass | pass | pass | pass |
| 48 | 168 | 168 | 74 | 93 | 1 | 0 | 168 | 1.26 | 1.26 | pass | pass | pass | pass | pass |
| 49 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | 0.01 | 0.01 | pass | pass | pass | pass | pass |
| 50 | 8 | 8 | 5 | 3 | 0 | 0 | 8 | 0.06 | 0.06 | pass | pass | pass | pass | pass |

All frequency_claim denominator_value fields equal 13372 (= summary nonzero_tokens).

## Unit checks
- Sum of occurrences over signs 41-50 = 224 <= 13372: **pass**.
- all_tokens = nonzero_tokens + excluded_zero_tokens: **pass**.

## Limits
- Arithmetic checked by hand on the returned aggregates; no texts, source images or printed concordance were consulted.
- These checks showed no discrepancy; that is not proof about anything not queried, and a 10-sign unit cannot verify corpus-wide totals.
- Consistency check only; no claims about what any sign means.
