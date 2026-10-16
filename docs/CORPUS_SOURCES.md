# Corpus sources

Research notes only. No dataset, inscription or sign sequence is copied, converted or committed in this repository, whatever its licence.

Terms below are quoted only where a live page was read. Where no licence text was found, that is stated and the source must be treated as **all rights reserved** until its owner says otherwise.

## indusscript.in (Mahadevan 1977 numbering)
- URL: https://indusscript.in
- Page title read: "The Indus Script(IM77)".
- Sign numbering: Mahadevan 1977 (`M77`).
- Size: not stated on the page that could be read.
- Terms: no licence or terms-of-use text was visible on the page read. No terms to quote; treat as all rights reserved.

## Mahadevan 1977 concordance
- Citation: Iravatham Mahadevan, *The Indus Script: Texts, Concordance and Tables*, Memoirs of the Archaeological Survey of India No. 77, New Delhi, 1977.
- Sign numbering: defines the `M77` sign list.
- Size: not verified.
- Terms: publisher terms were not checked; treat as all rights reserved.

## Wells, Interactive Corpus of Indus Texts (ICIT)
- URL: https://www.user.tu-berlin.de/fuls/Homepage/indus/menueindus.htm
- Citation: Bryan K. Wells, *The Archaeology and Epigraphy of Indus Writing*, Archaeopress / Oxbow Books, ISBN 978-1-84217-994-9 (from a 2006 PhD).
- Sign numbering: Wells' own sign list (`W2015` in docs/CORPUS_FORMAT.md).
- Size: secondary sources report about 4537 inscribed objects and 19616 sign occurrences (unverified): https://wiki.digitalclassicist.org/Interactive_Corpus_of_Indus_Texts
- Terms: the page has no copyright or licence statement. Its only access instruction is: "Ask the administrator (email: andreas.fuls(at)tu-berlin.de) to get access to the database." The online tool was reported down as of 2021-06.

## Fuls, Corpus of Indus Inscriptions and Catalog of Indus Signs
- URL: https://www.user.tu-berlin.de/fuls/Homepage/indus/menueindus.htm
- Citation: Andreas Fuls, *Corpus of Indus Inscriptions* (2022) and *Catalog of Indus Signs* (2023).
- Sign numbering: Fuls' own catalogue numbering.
- Size: not verified.
- Terms: the print volumes carry copyright notices (reported in search results, not read first-hand); no open licence found.

## Running privately
Keep any real corpus outside this repository (or under git-ignored `data/`, or named `*.private.json`); see docs/PRIVATE_RUNS.md. To use your own copy, convert it locally to the docs/CORPUS_FORMAT.md format: one JSON file with `source`, `license`, `sign_list` and `inscriptions` (each with a unique `id`, `site`, and a non-empty `signs` list of sign ids in reading order, first sign rightmost). Run the conversion on your machine only; never commit, post or upload the result.
