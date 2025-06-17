
import pytest
from datetime import datetime
import math
from .add_quarters import add_quarters


def test_add_quarters_positive():
    """Test adding positive quarters"""
    # Add 1 quarter to September 1, 2014
    result = add_quarters(datetime(2014, 9, 1), 1)
    assert result == datetime(2014, 12, 1, 0, 0)
    
    # Add 4 quarters (1 year)
    result = add_quarters(datetime(2014, 9, 1), 4)
    assert result == datetime(2015, 9, 1, 0, 0)


def test_add_quarters_negative():
    """Test subtracting quarters with negative amount"""
    # Subtract 1 quarter from December 1, 2014
    result = add_quarters(datetime(2014, 12, 1), -1)
    assert result == datetime(2014, 9, 1, 0, 0)


def test_add_quarters_with_timestamps():
    """Test with timestamp inputs"""
    timestamp = datetime(2014, 9, 1).timestamp()
    result = add_quarters(timestamp, 4)
    assert result == datetime(2015, 9, 1, 0, 0)


def test_add_quarters_end_of_month():
    """Test when desired month has fewer days"""
    # December 31, 2014 + 3 quarters = September 30, 2015
    # (September has 30 days, not 31)
    result = add_quarters(datetime(2014, 12, 31), 3)
    assert result == datetime(2015, 9, 30, 0, 0)
    
    # May 31 + 1 quarter = August 31
    result = add_quarters(datetime(2014, 5, 31), 1)
    assert result == datetime(2014, 8, 31, 0, 0)
    
    # November 30 + 1 quarter = February 28 (or 29 in leap year)
    result = add_quarters(datetime(2014, 11, 30), 1)
    assert result == datetime(2015, 2, 28, 0, 0)


def test_add_quarters_leap_year():
    """Test with leap year handling"""
    # November 30, 2015 + 1 quarter = February 29, 2016 (leap year)
    result = add_quarters(datetime(2015, 11, 30), 1)
    assert result == datetime(2016, 2, 29, 0, 0)


def test_add_quarters_preserves_time():
    """Test that time components are preserved"""
    dt = datetime(2014, 9, 1, 9, 30, 45, 123456)
    result = add_quarters(dt, 2)
    assert result == datetime(2015, 3, 1, 9, 30, 45, 123456)


def test_add_quarters_nan_amount():
    """Test with NaN amount"""
    with pytest.raises(ValueError):
        add_quarters(datetime(2014, 9, 1), float('nan'))


def test_add_quarters_zero():
    """Test adding zero quarters"""
    dt = datetime(2014, 9, 1, 9, 30, 45)
    result = add_quarters(dt, 0)
    assert result == dt
