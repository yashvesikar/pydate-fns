
from datetime import datetime
import pytest

from .min import min


def test_min_returns_earliest_date():
    """Returns the earliest date"""
    result = min([
        datetime(1989, 7, 10),
        datetime(1987, 2, 11),
    ])
    assert result == datetime(1987, 2, 11)


def test_min_accepts_array_with_more_than_2_entries():
    """Accepts array with more than 2 entries"""
    result = min([
        datetime(1987, 2, 11),
        datetime(1989, 7, 10),
        datetime(1995, 7, 2),
        datetime(1990, 1, 1),
    ])
    assert result == datetime(1987, 2, 11)


def test_min_accepts_timestamps():
    """Accepts timestamps"""
    result = min([
        datetime(1989, 7, 10).timestamp(),
        datetime(1987, 2, 11).timestamp(),
    ])
    assert result == datetime(1987, 2, 11)


def test_min_accepts_mixed_input_types():
    """Accepts mixed input types (datetime and timestamps)"""
    result = min([
        datetime(1989, 7, 10),
        datetime(1987, 2, 11).timestamp(),
        datetime(1995, 7, 2),
    ])
    assert result == datetime(1987, 2, 11)


def test_min_throws_error_for_empty_array():
    """Throws error for empty array"""
    with pytest.raises(ValueError, match="dates array must not be empty"):
        min([])


def test_min_throws_error_for_all_invalid_dates():
    """Throws error when all dates are invalid"""
    with pytest.raises(ValueError, match="All dates are invalid"):
        min([float('nan'), float('nan')])


def test_min_skips_invalid_dates():
    """Skips invalid dates and returns the minimum of valid ones"""
    result = min([
        datetime(1989, 7, 10),
        float('nan'),  # Invalid
        datetime(1987, 2, 11),
        float('nan'),  # Invalid
    ])
    assert result == datetime(1987, 2, 11)
