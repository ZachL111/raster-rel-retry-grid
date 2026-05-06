# raster-rel-retry-grid

`raster-rel-retry-grid` is a Solidity project in reliability. Its focus is to develop a Solidity command-oriented project for retry scenarios with log and snapshot fixtures, replay consistency checks, and no network dependency.

## Project Rationale

I want this repository to be useful as a quick reading exercise: fixtures first, implementation second, verifier last.

## Raster Rel Retry Grid Review Notes

`recovery` and `stress` are the cases worth reading first. They show the optimistic and cautious ends of the fixture.

## Feature Set

- `fixtures/domain_review.csv` adds cases for budget pressure and failure width.
- `metadata/domain-review.json` records the same cases in structured form.
- `config/review-profile.json` captures the read order and the two review questions.
- `examples/raster-rel-retry-walkthrough.md` walks through the case spread.
- The Solidity code includes a review path for `runbook drift` and `failure width`.
- `docs/field-notes.md` explains the strongest and weakest cases.

## Architecture

The fixture data drives the tests. The code stays thin, while `metadata/domain-review.json` and `config/review-profile.json` explain what each case is meant to protect.

The Solidity checks add a pure review lens and Foundry coverage.

## Usage

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verify.ps1
```

## Test Command

That command is also the regression path. It verifies the domain cases and catches mismatches between the CSV, metadata, and code.

## Next Improvements

The fixture set is small enough to audit by hand. The next useful expansion is malformed input coverage, not extra surface area.
