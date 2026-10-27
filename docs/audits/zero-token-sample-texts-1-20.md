# Corpus audit: zero/illegible-token exclusion, text numbers 1-20

Source: indus-corpus-v1 (Mahadevan IM77/IDF80 snapshot, corpus_revision 0), via query_data.

## Queries run (all with the held project/task)

1. `summary`
2. `texts` with text_numbers 1..20 (one call)
3. `sign` sign_id 0
4. `sign` sign_id 342 (substitute, see limits)

## Results

| check | result |
|---|---|
| summary all_tokens | 14153 |
| summary nonzero_tokens (= tokens) | 13372 |
| summary excluded_zero_tokens | 781 |
| all_tokens = nonzero_tokens + excluded_zero_tokens | pass (13372 + 781 = 14153) |
| sign 0 occurrences | 781 (matches excluded_zero_tokens) |
| sign 0 returns no frequency_claim | pass |
| texts 1-20 returned | **none (empty result)** |
| sample token counts (all / zero / uncertain `?` / nonzero) | not computed: empty sample |
| sample sign occurrences >= sample count | not computed: empty sample |
| frequency_claim percent uses nonzero_tokens (sign 342) | pass: 1395 / 13372 = 10.43%; all_tokens would give 9.86% |

## Discrepancy

The `texts` query for text numbers 1-20 returned an empty list, so no
inscriptions were sampled. Summary reports 2906 distinct text numbers for
3916 texts; this audit did not query which numbers exist. No cause is
assumed here.

## Limits

- The planned 20-inscription sample checks were not done. A follow-up should
  use text numbers that are known to exist.
- Sign 342 was not one of the three most frequent signs in a sample, because
  there was no sample. It was picked from the sign-0 neighbour lists only to
  check the denominator once.
- These checks found no discrepancy in the totals or the denominator, apart
  from the empty sample. That is not proof about anything not queried.
- Nothing here says what any sign means.
