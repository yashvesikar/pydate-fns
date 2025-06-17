
import math
from datetime import datetime

from .is_valid import is_valid


def test_is_valid_returns_true_for_valid_date():
    """Returns true if the given date is valid"""
    result = is_valid(datetime.now())
    assert result is True


def test_is_valid_returns_false_for_invalid_date():
    """Returns false if the given date is invalid"""
    result = is_valid(float('nan'))
    assert result is False


def test_is_valid_accepts_timestamp():
    """Accepts a timestamp"""
    # Valid timestamp
    valid_timestamp = datetime(2014, 2, 11).timestamp()
    assert is_valid(valid_timestamp) is True
    
    # Invalid timestamp (NaN)
    assert is_valid(float('nan')) is False


def test_is_valid_treats_none_as_invalid():
    """Treats None as an invalid date"""
    result = is_valid(None)
    assert result is False


def test_is_valid_treats_strings_as_invalid():
    """Treats strings as invalid dates"""
    assert is_valid("") is False
    assert is_valid("invalid") is False
    assert is_valid("2014-02-11") is False  # Even valid date strings are not accepted


def test_is_valid_with_valid_datetime():
    """Returns true for valid datetime objects"""
    assert is_valid(datetime(2014, 2, 11)) is True
    assert is_valid(datetime(2020, 12, 31, 23, 59, 59)) is True


def test_is_valid_with_valid_timestamps():
    """Returns true for valid timestamps"""
    assert is_valid(0) is True  # Unix epoch
    assert is_valid(1609459200) is True  # 2021-01-01 00:00:00 UTC
    assert is_valid(1609459200.5) is True  # With fractional seconds


def test_is_valid_with_edge_cases():
    """Handles edge cases correctly"""
    # Very large timestamp (should still be valid if within range)
    assert is_valid(2147483647) is True  # Max 32-bit signed int
    
    # Zero timestamp (Unix epoch)
    assert is_valid(0) is True
    
    # Negative timestamp (before Unix epoch)
    assert is_valid(-86400) is True  # One day before epoch
