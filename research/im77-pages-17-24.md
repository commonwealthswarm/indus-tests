# IM77 physical pages 17–24: doublet count comparison

The eight SHA-verified source pages contain doublet frequencies, not individual-sign frequencies. Each page has 24 entries. Independently reading all 192 entries in this run and comparing the corresponding corpus sequences gives **188 exact matches, 0 nonzero differences of 5% or less, and 4 differences greater than 5%**. Exact matches are excluded from the nonzero difference category; including them, 188 entries are within 5%.

| Physical page | Exact | Nonzero difference <=5% | Difference >5% |
|---|---:|---:|---:|
| 17 | 23 | 0 | 1 |
| 18 | 24 | 0 | 0 |
| 19 | 24 | 0 | 0 |
| 20 | 23 | 0 | 1 |
| 21 | 24 | 0 | 0 |
| 22 | 24 | 0 | 0 |
| 23 | 24 | 0 | 0 |
| 24 | 22 | 0 | 2 |
| Total | 188 | 0 | 4 |

## Method

The task's proposed singleton sign query does not measure the statistic printed on these pages. The heading is “Doublets frequencies greater than 0”. The CSV sign_number field therefore identifies a displayed left-to-right pair A-B. Query op sequence uses signs [B,A], because query_data explicitly states that stored order reverses the published display. A control on page 21 returned 4 matches for [328,307] versus 0 for [307,328], matching displayed 307-328, printed 4. Stored order does not establish reading direction.

Every count was queried under this held task after acknowledged plan_event_id 1407. Corpus source ID: indus-corpus-v1. Pair counts are occurrences returned as the sequence match count, not percentages of singleton tokens or counts of individual signs. Difference is corpus_count minus printed_total. Relative differences use the printed total as denominator: abs(corpus_count - printed_total) / printed_total * 100. No singleton frequency claim is made.

The CSV contains derived comparisons, not bulk corpus text rows. All eight page CSVs were posted to task lab notes. No source page images are included. Earlier provisional page-22 and page-24 transcriptions were explicitly superseded in corrected notes after private enlargement: page 22 right column seventh row is 17-244 (3 versus 3); page 24 first column sixth row is 387-59 (3 versus 4). The provisional labels are not findings.

## All larger differences

| Physical page | Displayed pair | Printed | Corpus | Difference | Relative difference | Cause |
|---|---|---:|---:|---:|---:|---|
| 17 | 67-389 | 4 | 5 | +1 | 25% | Unknown |
| 20 | 51-59 | 4 | 5 | +1 | 25% | Unknown |
| 24 | 261-87 | 3 | 4 | +1 | 33.33% | Unknown |
| 24 | 387-59 | 3 | 4 | +1 | 33.33% | Unknown |

Source-label inspection supports these printed readings. The available evidence does not distinguish different corpus edition, split or merge, or another corpus/source discrepancy. Do not attribute a cause without reconciliation of underlying source records.

## Source provenance

Private source: Supplied IM77 Frequency Tables PDF, SHA-256 ce3f5e3c5be88a7735b5790036bb6ac5874d00640cf3c03ba289cabb896dfe94.
Physical page image hashes:
- 17: 4195b6d61a6dcfafe936dfc4f56b85e52ddf63d9f51c7cc4737a38521c9df7de
- 18: 36fb1facc2c1fe37d56b50db172e2f08dba5865fe85e073b9953bb35faa16677
- 19: 1891b15fd8158939439d0ff85a8af151271068d87c015e49177b839eaa4cb9f5
- 20: 79c82f93143a0e7eb6cff03dfc1221667e71c33107d2b6e82ad5ae0c026d9b41
- 21: c3267b462de574105bd7eb436d37aa41b2aa0591391016889a558d52bdee983d
- 22: d02358002a2d75b386ea61c40818da9a2efc35d3e3d1517a1273e7ce0bc64749
- 23: ce724e5d501556378b3ab2d22828746eb4149f97c8f0ff5baf751ff0e1ae034f
- 24: 90a37703ad5679b3e7e4618b90918fc398f2b9f5d753204660ccd7e323029ecf

## Validation and limits

Validated in memory: eight distinct pages, 24 successful comparisons per page, 192 rows; finite corpus counts for every entry; aggregate categories sum to 192; all CSV differences computed from the two counts. Source labels and totals read directly; no inherited transcription used in final counts. No executable project code was run. All findings concern counts only: neither matching frequency nor a discrepancy establishes sign meaning, language, or decipherment.
