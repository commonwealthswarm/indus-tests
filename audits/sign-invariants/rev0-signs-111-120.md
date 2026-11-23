# Coverage audit: sign invariants, signs 111-120 (corpus revision 0)

Work key: indus-sign-invariants-v1|rev0|111..120
Source: indus-corpus-v1 (Mahadevan & RMRL 2021, IM77/IDF80), via the Night Shift query_data tool.

## Queries run (exactly 11)
- `query_data op=summary` (1)
- `query_data op=sign sign_id=N` for N = 111..120 (10)

## Summary
corpus_revision 0; all_tokens 14153; nonzero_tokens 13372; excluded_zero_tokens 781. 13372 + 781 = 14153: **pass**.

## Per-sign checks
Positions are stored order (S1 first), not reading direction. Expected percent = round(10000*occ/13372)/100.

| sign | occ | texts | first | middle | last | alone | f+m+l-a | percent (claim) | expected | occ>=1 | texts<=occ | positions | denom | percent |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 111 | 4 | 4 | 2 | 2 | 0 | 0 | 4 | 0.03 | 0.03 | pass | pass | pass | pass | pass |
| 112 | 70 | 70 | 16 | 54 | 0 | 0 | 70 | 0.52 | 0.52 | pass | pass | pass | pass | pass |
| 113 | 17 | 17 | 0 | 16 | 1 | 0 | 17 | 0.13 | 0.13 | pass | pass | pass | pass | pass |
| 114 | 7 | 7 | 3 | 4 | 0 | 0 | 7 | 0.05 | 0.05 | pass | pass | pass | pass | pass |
| 115 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 0.01 | 0.01 | pass | pass | pass | pass | pass |
| 116 | 2 | 2 | 1 | 1 | 0 | 0 | 2 | 0.01 | 0.01 | pass | pass | pass | pass | pass |
| 117 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 0.01 | 0.01 | pass | pass | pass | pass | pass |
| 118 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 0.01 | 0.01 | pass | pass | pass | pass | pass |
| 119 | 13 | 13 | 13 | 0 | 0 | 0 | 13 | 0.1 | 0.10 | pass | pass | pass | pass | pass |
| 120 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0.01 | 0.01 | pass | pass | pass | pass | pass |

All frequency_claim denominator_value fields equal 13372 (= summary nonzero_tokens).

## Unit checks
- Sum of occurrences over signs 111-120 = 118 <= 13372: **pass**.
- all_tokens = nonzero_tokens + excluded_zero_tokens: **pass**.

## Limits
- Arithmetic checked by hand on returned aggregates; no texts, source images or printed concordance were consulted.
- These checks showed no discrepancy; that is not proof about anything not queried, and a 10-sign unit cannot verify corpus-wide totals.
- Consistency check only; no claims about what any sign means.
