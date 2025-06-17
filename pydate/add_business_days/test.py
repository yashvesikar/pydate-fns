
import pytest
from datetime import datetime
import math
from .add_business_days import add_business_days


def test_add_business_days_positive():
    """Test adding positive business days"""
    # Add 10 business days to Monday Sep 1, 2014
    result = add_business_days(datetime(2014, 9, 1), 10)
    assert result == datetime(2014, 9, 15, 0, 0)
    
    # Add 1 business day to Friday
    result = add_business_days(datetime(2014, 9, 5), 1)
    assert result == datetime(2014, 9, 8, 0, 0)  # Monday


def test_add_business_days_negative():
    """Test subtracting business days"""
    # Subtract 10 business days from Monday Sep 15, 2014
    result = add_business_days(datetime(2014, 9, 15), -10)
    assert result == datetime(2014, 9, 1, 0, 0)
    
    # Subtract 1 business day from Monday
    result = add_business_days(datetime(2014, 9, 8), -1)
    assert result == datetime(2014, 9, 5, 0, 0)  # Friday


def test_add_business_days_zero():
    """Test adding zero business days"""
    # On a weekday
    result = add_business_days(datetime(2014, 9, 1), 0)
    assert result == datetime(2014, 9, 1, 0, 0)
    
    # On a weekend
    result = add_business_days(datetime(2014, 9, 6), 0)
    assert result == datetime(2014, 9, 6, 0, 0)


def test_add_business_days_from_weekend():
    """Test adding business days from weekend"""
    # Add from Saturday
    result = add_business_days(datetime(2014, 9, 6), 5)
    assert result == datetime(2014, 9, 12, 0, 0)  # Friday
    
    # Add from Sunday
    result = add_business_days(datetime(2014, 9, 7), 5)
    assert result == datetime(2014, 9, 12, 0, 0)  # Friday
    
    # Subtract from Saturday (should land on Monday due to special weekend handling)
    result = add_business_days(datetime(2014, 9, 6), -5)
    assert result == datetime(2014, 9, 1, 0, 0)  # Monday
    
    # Subtract from Sunday (should also land on Monday)
    result = add_business_days(datetime(2014, 9, 7), -5)
    assert result == datetime(2014, 9, 1, 0, 0)  # Monday


def test_add_business_days_multiple_weeks():
    """Test adding business days across multiple weeks"""
    # Add 20 business days (4 weeks)
    result = add_business_days(datetime(2014, 9, 1), 20)
    assert result == datetime(2014, 9, 29, 0, 0)
    
    # Add 25 business days (5 weeks)
    result = add_business_days(datetime(2014, 9, 1), 25)
    assert result == datetime(2014, 10, 6, 0, 0)


def test_add_business_days_preserves_time():
    """Test that time components are preserved"""
    dt = datetime(2014, 9, 1, 9, 30, 45, 123456)
    result = add_business_days(dt, 5)
    assert result == datetime(2014, 9, 8, 9, 30, 45, 123456)


def test_add_business_days_with_timestamps():
    """Test with timestamp inputs"""
    # Monday Sep 1, 2014
    timestamp = datetime(2014, 9, 1).timestamp()
    result = add_business_days(timestamp, 10)
    assert result == datetime(2014, 9, 15, 0, 0)


def test_add_business_days_nan_amount():
    """Test with NaN amount"""
    with pytest.raises(ValueError, match="Amount cannot be NaN"):
        add_business_days(datetime(2014, 9, 1), float('nan'))


def test_add_business_days_edge_cases():
    """Test edge cases"""
    # Large positive amount (100 business days = 20 weeks)
    result = add_business_days(datetime(2014, 9, 1), 100)
    assert result == datetime(2015, 1, 19, 0, 0)
    
    # Large negative amount
    result = add_business_days(datetime(2014, 9, 1), -100)
    assert result == datetime(2014, 4, 14, 0, 0)
