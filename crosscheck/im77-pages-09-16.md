# IM77 frequency tables vs Night Shift corpus: physical pages 9-16

Source for corpus counts: indus-corpus-v1 (query_data). Printed totals were read from the private IM77 frequency tables PDF (hash-verified page images). No page images or long passages are reproduced here.

## Method

Pages 9-16 are all headed "Doublets frequencies greater than 0": each cell holds a printed sign pair a-b and a total. A single-sign `op sign` count measures something else, so each pair was compared with `op sequence` on the reversed pair [b, a], because the corpus stores signs in the reverse of the published display order. Difference = corpus_count minus printed_total. Full per-row CSVs (columns physical_page, sign_number [printed pair], printed_total, corpus_count, difference) are in the lab notes on task t_65fc4002, one note per page.

## Results

| Page | Pairs | Exact | <=5% (nonzero) | >5% |
|---|---|---|---|---|
| 9 | 24 | 22 | 0 | 2 |
| 10 | 24 | 24 | 0 | 0 |
| 11 | 24 | 23 | 0 | 1 |
| 12 | 24 | 24 | 0 | 0 |
| 13 | 24 | 23 | 0 | 1 |
| 14 | 24 | 24 | 0 | 0 |
| 15 | 24 | 23 | 0 | 1 |
| 16 | 24 | 22 | 0 | 2 |
| **Total** | **192** | **185** | **0** | **7** |

Because printed totals here are small (5-9), any nonzero difference is more than 5%.

## Differences larger than 5%

| Page | Printed pair | Printed | Corpus | Diff | Most likely cause |
|---|---|---|---|---|---|
| 9 | 244-87 | 9 | 11 | +2 | unknown |
| 9 | 99-162 | 8 | 9 | +1 | unknown |
| 11 | 328-328 | 7 | 10 (in 7 texts) | +3 | counting method: the corpus counts overlapping matches inside runs of 3+ repeated 328, while the print matches the number of texts (7). Not a data disagreement. |
| 13 | 211-176 | 6 | 8 | +2 | unknown |
| 15 | 403-87 | 5 | 6 | +1 | unknown |
| 16 | 249-99 | 5 | 6 | +1 | unknown |
| 16 | 94-409 | 5 | 6 | +1 | unknown |

All six unexplained differences go the same way: the corpus has more pairs than the print. That fits a different corpus edition (the corpus also draws on IDF80 material) or a later re-reading of a sign, but this audit did not check that, so the cause is recorded as unknown. A useful next step is to list the matching text numbers for each pair (`op find`) and see which texts are absent from IM77.

## Corrections

An earlier lab note listed page 12 "402-402, printed 6, corpus 0". Looking at the page again shows the cell reads 149-402, and corpus [402,149] = 6, which agrees exactly. That apparent discrepancy was a misread print.

## Provenance and caveats

- I viewed pages 12-16 with hash checks and queried every pair on them across two runs of this task. In this run I re-checked the whole of page 12 against its image.
- The page 9-11 rows come from the first run of this task (same agent). They were not looked at again in the final run.
- These are counts only. Nothing here says what any sign means.
