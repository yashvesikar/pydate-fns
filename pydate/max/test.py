
from datetime import datetime
import pytest

from .max import max


def test_max_returns_latest_date():
    """Returns the latest date"""
    result = max([
        datetime(1989, 7, 10),
        datetime(1987, 2, 11),
    ])
    assert result == datetime(1989, 7, 10)


def test_max_accepts_array_with_more_than_2_entries():
    """Accepts array with more than 2 entries"""
    result = max([
        datetime(1987, 2, 11),
        datetime(1989, 7, 10),
        datetime(1995, 7, 2),
        datetime(1990, 1, 1),
    ])
    assert result == datetime(1995, 7, 2)


def test_max_accepts_timestamps():
    """Accepts timestamps"""
    result = max([
        datetime(1989, 7, 10).timestamp(),
        datetime(1987, 2, 11).timestamp(),
    ])
    assert result == datetime(1989, 7, 10)


def test_max_accepts_mixed_input_types():
    """Accepts mixed input types (datetime and timestamps)"""
    result = max([
        datetime(1989, 7, 10),
        datetime(1987, 2, 11).timestamp(),
        datetime(1995, 7, 2),
    ])
    assert result == datetime(1995, 7, 2)


def test_max_throws_error_for_empty_array():
    """Throws error for empty array"""
    with pytest.raises(ValueError, match="dates array must not be empty"):
        max([])


def test_max_throws_error_for_all_invalid_dates():
    """Throws error when all dates are invalid"""
    with pytest.raises(ValueError, match="All dates are invalid"):
        max([float('nan'), float('nan')])


def test_max_skips_invalid_dates():
    """Skips invalid dates and returns the maximum of valid ones"""
    result = max([
        datetime(1989, 7, 10),
        float('nan'),  # Invalid
        datetime(1995, 7, 2),
        float('nan'),  # Invalid
    ])
    assert result == datetime(1995, 7, 2)
