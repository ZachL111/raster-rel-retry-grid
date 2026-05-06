"""Executable checks for the raster-rel-retry-grid casebook."""

from __future__ import annotations

from collections import Counter

from . import raster_rel_retry_grid_segment_00
from . import raster_rel_retry_grid_segment_01
from . import raster_rel_retry_grid_segment_02
from . import raster_rel_retry_grid_segment_03
from . import raster_rel_retry_grid_segment_04
from . import raster_rel_retry_grid_segment_05
from . import raster_rel_retry_grid_segment_06
from . import raster_rel_retry_grid_segment_07
from . import raster_rel_retry_grid_segment_08
from . import raster_rel_retry_grid_segment_09
from .expected import EXPECTED
from .model import validate_case


def iter_cases():
    yield from raster_rel_retry_grid_segment_00.iter_raster_rel_retry_grid_00()
    yield from raster_rel_retry_grid_segment_01.iter_raster_rel_retry_grid_01()
    yield from raster_rel_retry_grid_segment_02.iter_raster_rel_retry_grid_02()
    yield from raster_rel_retry_grid_segment_03.iter_raster_rel_retry_grid_03()
    yield from raster_rel_retry_grid_segment_04.iter_raster_rel_retry_grid_04()
    yield from raster_rel_retry_grid_segment_05.iter_raster_rel_retry_grid_05()
    yield from raster_rel_retry_grid_segment_06.iter_raster_rel_retry_grid_06()
    yield from raster_rel_retry_grid_segment_07.iter_raster_rel_retry_grid_07()
    yield from raster_rel_retry_grid_segment_08.iter_raster_rel_retry_grid_08()
    yield from raster_rel_retry_grid_segment_09.iter_raster_rel_retry_grid_09()


def summarize_cases() -> dict:
    rows = list(iter_cases())
    for row in rows:
        validate_case(row)
    lanes = Counter(row.expected_lane for row in rows)
    focus = Counter(row.focus for row in rows)
    return {
        "case_count": len(rows),
        "score_min": min(row.expected_score for row in rows),
        "score_max": max(row.expected_score for row in rows),
        "lane_counts": dict(sorted(lanes.items())),
        "focus_counts": dict(sorted(focus.items())),
        "score_checksum": sum((index + 1) * row.expected_score for index, row in enumerate(rows)),
        "pressure_checksum": sum((index % 17 + 1) * row.pressure for index, row in enumerate(rows)),
    }


def assert_expected() -> dict:
    summary = summarize_cases()
    if summary != EXPECTED:
        raise AssertionError(f"casebook summary mismatch: {summary!r} != {EXPECTED!r}")
    return summary


def raster_rel_retry_grid_summary() -> dict:
    return assert_expected()
