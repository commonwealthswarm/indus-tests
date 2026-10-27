# Corpus audit: overlapping sequence counts vs matching inscriptions (bounded sample)

Task t_58ca0d5f. Source: indus-corpus-v1 (Mahadevan IM77/IDF80 snapshot via query_data). Counts and method only; nothing here says what any sign means.

## Selection rule (stated in plan before querying)

Query sign 342; S1 = [first-listed 'before' neighbour, 342]; S2 = [342, first-listed 'after' neighbour]. Sample = 5 lowest text numbers from each sequence's find list (10 total). Time limit allowed 2 sequences, not 3.

## Queries run (all of them)

1. sign {sign_id: 342} -> before[0] = 48 (n=114); after[0] = 176 (n=184).
2. sequence {signs: [48, 342]} -> matches 114, texts 114, starts_at_first_position 60.
3. find {signs: [48, 342]} -> 50 text numbers returned; list is capped (50 < 114).
4. sequence {signs: [342, 176]} -> matches 184, texts 184, starts_at_first_position 0.
5. find {signs: [342, 176]} -> 50 text numbers returned; list is capped (50 < 184).
6. texts {text_numbers: [1020, 1027, 1119, 1125, 1187, 1116, 1529, 1530, 1531, 1615]}.

## Checks

| Sequence | matches | texts | matches >= texts | sign-query neighbour n | find listed |
|---|---|---|---|---|---|
| 48 342 | 114 | 114 | yes | 114 | 50 (capped) |
| 342 176 | 184 | 184 | yes | 184 | 50 (capped) |

The sequence counts agree with the before/after neighbour counts from the sign query.

### Sample (hand count of overlapping occurrences)

| Sequence | Text numbers sampled | Inscriptions containing it | Hand-counted occurrences |
|---|---|---|---|
| 48 342 | 1020, 1027, 1119, 1125, 1187 | 5 / 5 | 5 |
| 342 176 | 1116, 1529, 1530, 1531, 1615 | 5 / 5 | 5 |

- Every sampled text number returned a single side (side_line 0); no multi-side text numbers seen in the sample.
- Uncertain signs: 1027 has trailing '?' on two signs, neither part of the queried sequence; no queried sign in the sample carried '?'. Treatment: '?' signs would have been kept as the stated sign and flagged.
- 1027 contains 342 twice, but 48 342 only once (hand count 1).
- In stored order, 1119 and 1125 begin with 48 342, consistent with starts_at_first_position > 0 for S1; no S2 sample starts with 342 176, consistent with starts_at_first_position = 0.

## Result and limits

The checks run showed no discrepancy. This is not proof about anything not queried: the 10-inscription sample cannot verify the totals of 114 and 184, the find lists are capped at 50, and only 2 sequences were examined. matches == texts for both sequences means the server reports no text number with two occurrences of either sequence; the sample is consistent with that but cannot confirm it corpus-wide.
