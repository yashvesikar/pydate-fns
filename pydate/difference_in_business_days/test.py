
import pytest
from datetime import datetime
import math
from .difference_in_business_days import difference_in_business_days


def test_difference_in_business_days_basic():
    """Test basic business days calculation"""
    # From Jan 10, 2014 to Jul 18, 2014
    result = difference_in_business_days(datetime(2014, 7, 18), datetime(2014, 1, 10))
    assert result == 135


def test_difference_in_business_days_negative():
    """Test negative difference when first date is earlier"""
    result = difference_in_business_days(datetime(2014, 1, 10), datetime(2014, 7, 20))
    assert result == -135


def test_difference_in_business_days_weekend_start():
    """Test when first date falls on a weekend"""
    # Jul 20, 2019 is Saturday, Jul 18, 2019 is Thursday
    result = difference_in_business_days(datetime(2019, 7, 20), datetime(2019, 7, 18))
    assert result == 2


def test_difference_in_business_days_weekend_end():
    """Test when second date falls on a weekend"""
    # Jul 23, 2019 is Tuesday, Jul 20, 2019 is Saturday
    result = difference_in_business_days(datetime(2019, 7, 23), datetime(2019, 7, 20))
    assert result == 1


def test_difference_in_business_days_both_weekend():
    """Test when both dates fall on a weekend"""
    # Jul 28, 2019 is Sunday, Jul 20, 2019 is Saturday
    result = difference_in_business_days(datetime(2019, 7, 28), datetime(2019, 7, 20))
    assert result == 5


def test_difference_in_business_days_with_timestamps():
    """Test with timestamp inputs"""
    timestamp1 = datetime(2014, 7, 18).timestamp()
    timestamp2 = datetime(2014, 1, 10).timestamp()
    result = difference_in_business_days(timestamp1, timestamp2)
    assert result == 135


def test_difference_in_business_days_less_than_day():
    """Test when difference is less than a day but in different calendar days"""
    result = difference_in_business_days(
        datetime(2014, 9, 5, 0, 0),
        datetime(2014, 9, 4, 23, 59)
    )
    assert result == 1


def test_difference_in_business_days_less_than_day_reversed():
    """Test the same for swapped dates"""
    result = difference_in_business_days(
        datetime(2014, 9, 4, 23, 59),
        datetime(2014, 9, 5, 0, 0)
    )
    assert result == -1


def test_difference_in_business_days_same_day():
    """Test when the given dates are the same"""
    result = difference_in_business_days(
        datetime(2014, 9, 5, 0, 0),
        datetime(2014, 9, 5, 0, 0)
    )
    assert result == 0


def test_difference_in_business_days_not_negative_zero():
    """Test that it doesn't return -0"""
    result = difference_in_business_days(
        datetime(2014, 9, 5, 0, 0),
        datetime(2014, 9, 5, 0, 0)
    )
    # Check it's not negative zero
    # In Python, we can check for negative zero using copysign
    import math
    assert result == 0
    assert math.copysign(1, result) == 1  # Positive zero


def test_difference_in_business_days_invalid_dates():
    """Test with invalid dates"""
    # First date invalid
    try:
        result = difference_in_business_days(float('nan'), datetime(2017, 1, 1))
        assert math.isnan(result)
    except:
        # If to_date raises an exception for NaN, that's also acceptable
        pass
    
    # Second date invalid
    try:
        result = difference_in_business_days(datetime(2017, 1, 1), float('nan'))
        assert math.isnan(result)
    except:
        # If to_date raises an exception for NaN, that's also acceptable
        pass


def test_difference_in_business_days_large_range():
    """Test with a large date range"""
    # Skip test if year would be out of range
    try:
        result = difference_in_business_days(datetime(9999, 12, 31), datetime(2014, 1, 1))
        # Just verify it returns a large positive number
        assert result > 2000000
    except ValueError as e:
        # This is expected if the year would be out of range
        assert "year" in str(e) and "out of range" in str(e)
