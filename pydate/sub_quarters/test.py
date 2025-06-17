
import pytest
from datetime import datetime
import math
from .sub_quarters import sub_quarters


def test_sub_quarters_positive():
    """Test subtracting positive quarters"""
    # Subtract 1 quarter from December 1, 2014
    result = sub_quarters(datetime(2014, 12, 1), 1)
    assert result == datetime(2014, 9, 1, 0, 0)
    
    # Subtract 4 quarters (1 year)
    result = sub_quarters(datetime(2015, 9, 1), 4)
    assert result == datetime(2014, 9, 1, 0, 0)


def test_sub_quarters_negative():
    """Test adding quarters with negative amount"""
    # Negative amount should add quarters
    result = sub_quarters(datetime(2014, 9, 1), -1)
    assert result == datetime(2014, 12, 1, 0, 0)


def test_sub_quarters_with_timestamps():
    """Test with timestamp inputs"""
    timestamp = datetime(2015, 9, 1).timestamp()
    result = sub_quarters(timestamp, 4)
    assert result == datetime(2014, 9, 1, 0, 0)


def test_sub_quarters_end_of_month():
    """Test when desired month has fewer days"""
    # September 30, 2015 - 3 quarters = December 31, 2014
    result = sub_quarters(datetime(2015, 9, 30), 3)
    assert result == datetime(2014, 12, 30, 0, 0)
    
    # May 31 - 1 quarter = February 28/29
    result = sub_quarters(datetime(2014, 5, 31), 1)
    assert result == datetime(2014, 2, 28, 0, 0)  # Not leap year
    
    # May 31, 2016 - 1 quarter = February 29, 2016 (leap year)
    result = sub_quarters(datetime(2016, 5, 31), 1)
    assert result == datetime(2016, 2, 29, 0, 0)


def test_sub_quarters_preserves_time():
    """Test that time components are preserved"""
    dt = datetime(2015, 3, 1, 9, 30, 45, 123456)
    result = sub_quarters(dt, 2)
    assert result == datetime(2014, 9, 1, 9, 30, 45, 123456)


def test_sub_quarters_nan_amount():
    """Test with NaN amount"""
    with pytest.raises(ValueError):
        sub_quarters(datetime(2014, 9, 1), float('nan'))


def test_sub_quarters_zero():
    """Test subtracting zero quarters"""
    dt = datetime(2014, 9, 1, 9, 30, 45)
    result = sub_quarters(dt, 0)
    assert result == dt
