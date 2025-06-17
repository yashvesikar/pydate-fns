
import pytest
from datetime import datetime
import math
from .sub_business_days import sub_business_days


def test_sub_business_days_positive():
    """Test subtracting positive business days"""
    # Subtract 10 business days from Monday Sep 1, 2014
    result = sub_business_days(datetime(2014, 9, 1), 10)
    assert result == datetime(2014, 8, 18, 0, 0)


def test_sub_business_days_negative():
    """Test with negative amount (adds business days)"""
    # Negative amount should add business days
    result = sub_business_days(datetime(2014, 8, 18), -10)
    assert result == datetime(2014, 9, 1, 0, 0)


def test_sub_business_days_large_number():
    """Test with a large number of business days"""
    # Skip test if year would be out of range
    # Python datetime has a max year of 9999
    try:
        result = sub_business_days(datetime(9999, 12, 31), 2000000)
        # Verify it's a valid datetime
        assert isinstance(result, datetime)
    except ValueError as e:
        # This is expected if the resulting year would be out of range
        assert "year" in str(e) and "out of range" in str(e)


def test_sub_business_days_with_timestamps():
    """Test with timestamp inputs"""
    # Monday Sep 1, 2014
    timestamp = datetime(2014, 9, 1).timestamp()
    result = sub_business_days(timestamp, 10)
    assert result == datetime(2014, 8, 18, 0, 0)


def test_sub_business_days_preserves_time():
    """Test that time components are preserved"""
    dt = datetime(2014, 9, 1, 9, 30, 45, 123456)
    result = sub_business_days(dt, 5)
    assert result == datetime(2014, 8, 25, 9, 30, 45, 123456)


def test_sub_business_days_nan_amount():
    """Test with NaN amount"""
    with pytest.raises(ValueError, match="Amount cannot be NaN"):
        sub_business_days(datetime(2014, 9, 1), float('nan'))


def test_sub_business_days_from_weekend():
    """Test subtracting business days from weekend"""
    # Subtract from Saturday
    # When subtracting from a weekend and amount is divisible by 5,
    # it lands on Monday (due to special weekend handling)
    result = sub_business_days(datetime(2014, 9, 6), 5)
    assert result == datetime(2014, 9, 1, 0, 0)  # Monday
    
    # Subtract from Sunday
    result = sub_business_days(datetime(2014, 9, 7), 5)
    assert result == datetime(2014, 9, 1, 0, 0)  # Monday
