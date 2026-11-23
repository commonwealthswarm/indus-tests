# Coverage audit: sign invariants, signs 101-110 (corpus revision 0)

Work key: indus-sign-invariants-v1|rev0|101..110
Source: indus-corpus-v1 (Mahadevan & RMRL 2021, IM77/IDF80), via the Night Shift query_data tool.

## Queries run (exactly 11)
- `query_data op=summary` (1)
- `query_data op=sign sign_id=N` for N = 101..110 (10)

## Summary
corpus_revision 0; all_tokens 14153; nonzero_tokens 13372; excluded_zero_tokens 781. 13372 + 781 = 14153: **pass**.

## Per-sign checks
Positions are stored order (S1 first), not reading direction. Expected percent = round(10000*occ/13372)/100.

| sign | occ | texts | first | middle | last | alone | f+m+l-a | percent (claim) | expected | occ>=1 | texts<=occ | positions | denom | percent |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 101 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 0.01 | 0.01 | pass | pass | pass | pass | pass |
| 102 | 151 | 151 | 78 | 70 | 10 | 7 | 151 | 1.13 | 1.13 | pass | pass | pass | pass | pass |
| 103 | 30 | 30 | 24 | 6 | 2 | 2 | 30 | 0.22 | 0.22 | pass | pass | pass | pass | pass |
| 104 | 70 | 69 | 32 | 35 | 4 | 1 | 70 | 0.52 | 0.52 | pass | pass | pass | pass | pass |
| 105 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | 0.01 | 0.01 | pass | pass | pass | pass | pass |
| 106 | 38 | 38 | 19 | 18 | 2 | 1 | 38 | 0.28 | 0.28 | pass | pass | pass | pass | pass |
| 107 | 6 | 6 | 2 | 1 | 3 | 0 | 6 | 0.04 | 0.04 | pass | pass | pass | pass | pass |
| 108 | 3 | 3 | 2 | 1 | 0 | 0 | 3 | 0.02 | 0.02 | pass | pass | pass | pass | pass |
| 109 | 38 | 38 | 21 | 17 | 1 | 1 | 38 | 0.28 | 0.28 | pass | pass | pass | pass | pass |
| 110 | 6 | 6 | 2 | 3 | 3 | 2 | 6 | 0.04 | 0.04 | pass | pass | pass | pass | pass |

All frequency_claim denominator_value fields equal 13372 (= summary nonzero_tokens).

## Unit checks
- Sum of occurrences over signs 101-110 = 345 <= 13372: **pass**.
- all_tokens = nonzero_tokens + excluded_zero_tokens: **pass**.

## Limits
- Arithmetic checked by hand on returned aggregates; no texts, source images or printed concordance were consulted.
- These checks showed no discrepancy; that is not proof about anything not queried, and a 10-sign unit cannot verify corpus-wide totals.
- Consistency check only; no claims about what any sign means.
