# Raster Rel Retry Grid Walkthrough

The fixture is intentionally compact, so the review starts with the cases that pull farthest apart.

| Case | Focus | Score | Lane |
| --- | --- | ---: | --- |
| baseline | budget pressure | 166 | ship |
| stress | failure width | 125 | watch |
| edge | recovery gap | 141 | ship |
| recovery | runbook drift | 208 | ship |
| stale | budget pressure | 157 | ship |

Start with `recovery` and `stress`. They create the widest contrast in this repository's fixture set, which makes them better review anchors than the middle cases.

The next useful expansion would be a malformed fixture around failure width and runbook drift.
