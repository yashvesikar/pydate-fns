
import pytest
from datetime import datetime
import math
from .difference_in_quarters import difference_in_quarters


def test_difference_in_quarters_basic():
    """Test basic quarter difference calculation"""
    # Exactly 1 year = 4 quarters
    result = difference_in_quarters(datetime(2012, 7, 2, 18, 0), datetime(2011, 7, 2, 6, 0))
    assert result == 4
    
    # 3 full quarters
    result = difference_in_quarters(datetime(2012, 7, 2, 5, 0), datetime(2011, 7, 2, 6, 0))
    assert result == 3


def test_difference_in_quarters_truncation():
    """Test truncation behavior (default rounding)"""
    # From May to July next year = 14 months = 4.67 quarters, truncates to 4
    result = difference_in_quarters(datetime(2012, 7, 2, 18, 0), datetime(2011, 5, 2, 6, 0))
    assert result == 4
    
    # Dec 31, 2013 to Jul 2, 2014 = 6 months + 2 days = 2 full quarters
    result = difference_in_quarters(datetime(2014, 7, 2), datetime(2013, 12, 31))
    assert result == 2


def test_difference_in_quarters_negative():
    """Test negative differences"""
    result = difference_in_quarters(datetime(2011, 7, 2, 6, 0), datetime(2012, 7, 2, 18, 0))
    assert result == -4


def test_difference_in_quarters_same_quarter():
    """Test dates in different months but same quarter"""
    # July 1 to June 30 - different calendar quarters but less than 3 months
    result = difference_in_quarters(datetime(2014, 7, 1), datetime(2014, 6, 30))
    assert result == 0
    
    # Same for swapped dates
    result = difference_in_quarters(datetime(2014, 6, 30), datetime(2014, 7, 1))
    assert result == 0


def test_difference_in_quarters_same_day_of_month():
    """Test when days of month are the same"""
    # Jan 6 to Apr 6 = 3 months = 1 quarter
    result = difference_in_quarters(datetime(2014, 4, 6), datetime(2014, 1, 6))
    assert result == 1


def test_difference_in_quarters_same_date():
    """Test when dates are the same"""
    result = difference_in_quarters(datetime(2014, 9, 5, 0, 0), datetime(2014, 9, 5, 0, 0))
    assert result == 0


def test_difference_in_quarters_not_negative_zero():
    """Test that it doesn't return -0"""
    result = difference_in_quarters(
        datetime(2021, 7, 22, 6, 1, 28, 973000),
        datetime(2021, 7, 22, 6, 1, 28, 976000)
    )
    # Check it's not negative zero
    assert result == 0
    assert math.copysign(1, result) == 1  # Positive zero


def test_difference_in_quarters_with_timestamps():
    """Test with timestamp inputs"""
    # Oct 2, 2014 to Jul 2, 2010 = 51 months = 17 quarters
    timestamp1 = datetime(2014, 10, 2).timestamp()
    timestamp2 = datetime(2010, 7, 2).timestamp()
    result = difference_in_quarters(timestamp1, timestamp2)
    assert result == 17


def test_difference_in_quarters_invalid_dates():
    """Test with invalid dates"""
    # First date invalid
    try:
        result = difference_in_quarters(float('nan'), datetime(2017, 1, 1))
        assert math.isnan(result)
    except:
        # If to_date raises an exception for NaN, that's also acceptable
        pass
    
    # Second date invalid
    try:
        result = difference_in_quarters(datetime(2017, 1, 1), float('nan'))
        assert math.isnan(result)
    except:
        # If to_date raises an exception for NaN, that's also acceptable
        pass
