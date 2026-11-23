# Coverage audit: token and uncertainty accounting, texts 1022-1041 (corpus revision 0)

Work key: indus-text-accounting-v1|rev0|1022..1041 (20 text numbers)
Source: indus-corpus-v1 (Mahadevan & RMRL 2021, IM77/IDF80), via query_data.

## Queries run (exactly two)
1. `query_data op=summary` (once)
2. `query_data op=texts text_numbers=[1022..1041]` (once, 20 numbers)

No sign, sequence or other queries were run.

## Summary check
| Field | Value |
|---|---|
| corpus_revision | 0 |
| all_tokens | 14153 |
| nonzero_tokens | 13372 |
| excluded_zero_tokens | 781 |
| all_tokens = nonzero + excluded_zero | 13372 + 781 = 14153, PASS |

## Unit aggregates
| Measure | Value |
|---|---|
| Text numbers requested | 20 |
| Text numbers returned | 20 (none missing) |
| Sides returned | 20 (one side, side_line 0, per text number) |
| Total tokens | 109 |
| Zero tokens (sign 0) | 3 (in 3 texts) |
| Nonzero tokens | 106 |
| Uncertain nonzero tokens (trailing ?) | 6 (in 4 texts) |
| total = zero + nonzero | 109 = 3 + 106, PASS |
| Sum of per-side token counts = total | 109, PASS |

Per-side token counts (ascending text number): 5, 8, 7, 2, 7, 8, 6, 5, 6, 5, 7, 7, 3, 5, 5, 4, 3, 6, 4, 6 (sum 109).

All 20 returned sides are object_type Seals; direction field reads Right to left for all.

## Result
The checks run showed no discrepancy. This is not a proof about anything not queried.

## Limits
- Covers only these 20 text numbers in corpus revision 0; it cannot verify corpus-wide totals (summary values were checked only for internal arithmetic consistency).
- Counts follow the database snapshot; no comparison against source images or printed concordance was made.
- Token counts depend on the stored tokenisation (space-separated signs, `?` marking uncertainty, 0 marking lost/illegible).
- Counts and method only; nothing here concerns what any sign means.
