# Coverage audit: sign invariants, signs 91-100 (corpus revision 0)

Work key: indus-sign-invariants-v1|rev0|91..100
Source: indus-corpus-v1 (Mahadevan & RMRL 2021, IM77/IDF80), via the Night Shift query_data tool.

## Queries run (exactly 11)
- `query_data op=summary` (1)
- `query_data op=sign sign_id=N` for N = 91..100 (10)

## Summary
corpus_revision 0; all_tokens 14153; nonzero_tokens 13372; excluded_zero_tokens 781. 13372 + 781 = 14153: **pass**.

## Per-sign checks
Positions are stored order (S1 first), not reading direction. Expected percent = round(10000*occ/13372)/100.

| sign | occ | texts | first | middle | last | alone | f+m+l-a | percent (claim) | expected | occ>=1 | texts<=occ | positions | denom | percent |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 91 | 2 | 2 | 0 | 0 | 2 | 0 | 2 | 0.01 | 0.01 | pass | pass | pass | pass | pass |
| 92 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 0.01 | 0.01 | pass | pass | pass | pass | pass |
| 93 | 11 | 11 | 5 | 1 | 10 | 5 | 11 | 0.08 | 0.08 | pass | pass | pass | pass | pass |
| 94 | 11 | 11 | 2 | 7 | 2 | 0 | 11 | 0.08 | 0.08 | pass | pass | pass | pass | pass |
| 95 | 64 | 64 | 59 | 5 | 0 | 0 | 64 | 0.48 | 0.48 | pass | pass | pass | pass | pass |
| 96 | 22 | 22 | 3 | 13 | 7 | 1 | 22 | 0.16 | 0.16 | pass | pass | pass | pass | pass |
| 97 | 91 | 86 | 1 | 87 | 3 | 0 | 91 | 0.68 | 0.68 | pass | pass | pass | pass | pass |
| 98 | 88 | 88 | 4 | 72 | 12 | 0 | 88 | 0.66 | 0.66 | pass | pass | pass | pass | pass |
| 99 | 649 | 648 | 2 | 625 | 22 | 0 | 649 | 4.85 | 4.85 | pass | pass | pass | pass | pass |
| 100 | 29 | 29 | 13 | 16 | 1 | 1 | 29 | 0.22 | 0.22 | pass | pass | pass | pass | pass |

All frequency_claim denominator_value fields equal 13372 (= summary nonzero_tokens).

## Unit checks
- Sum of occurrences over signs 91-100 = 968 <= 13372: **pass**.
- all_tokens = nonzero_tokens + excluded_zero_tokens: **pass**.

## Limits
- Arithmetic checked by hand on returned aggregates; no texts, source images or printed concordance were consulted.
- These checks showed no discrepancy; that is not proof about anything not queried, and a 10-sign unit cannot verify corpus-wide totals.
- Consistency check only; no claims about what any sign means.
