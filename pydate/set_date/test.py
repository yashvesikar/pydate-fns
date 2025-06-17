import pytest
from datetime import datetime
import math
from .set_date import set_date


def test_set_date_basic():
    """Test basic day setting"""
    result = set_date(datetime(2014, 9, 1), 30)
    assert result == datetime(2014, 9, 30)
    
    result = set_date(datetime(2014, 9, 2, 11, 55, 0), 18)
    assert result == datetime(2014, 9, 18, 11, 55, 0)


def test_set_date_preserves_time():
    """Test that time components are preserved"""
    result = set_date(datetime(2014, 9, 1, 11, 55, 59), 25)
    assert result == datetime(2014, 9, 25, 11, 55, 59)


def test_set_date_with_timestamp():
    """Test set_date with timestamp input"""
    dt = datetime(2014, 8, 1)
    result = set_date(dt.timestamp(), 15)
    assert result == datetime(2014, 8, 15)


def test_set_date_first_day():
    """Test setting to first day of month"""
    result = set_date(datetime(2014, 9, 15), 1)
    assert result == datetime(2014, 9, 1)


def test_set_date_last_valid_day():
    """Test setting to last valid day of various months"""
    # September has 30 days
    result = set_date(datetime(2014, 9, 1), 30)
    assert result == datetime(2014, 9, 30)
    
    # February has 28 days in non-leap year
    result = set_date(datetime(2014, 2, 1), 28)
    assert result == datetime(2014, 2, 28)
    
    # February has 29 days in leap year
    result = set_date(datetime(2016, 2, 1), 29)
    assert result == datetime(2016, 2, 29)


def test_set_date_overflow():
    """Test that setting invalid days causes month/year overflow"""
    # September only has 30 days, day 31 rolls to October 1
    result = set_date(datetime(2014, 9, 1), 31)
    assert result == datetime(2014, 10, 1)
    
    # September day 32 rolls to October 2
    result = set_date(datetime(2014, 9, 1), 32)
    assert result == datetime(2014, 10, 2)
    
    # February doesn't have 30 days, rolls to March
    result = set_date(datetime(2014, 2, 1), 30)
    assert result == datetime(2014, 3, 2)  # Feb has 28 days, so 30 = March 2
    
    # February doesn't have 29 days in non-leap year
    result = set_date(datetime(2015, 2, 1), 29)
    assert result == datetime(2015, 3, 1)
    
    # December 32 rolls to next year
    result = set_date(datetime(2014, 12, 1), 32)
    assert result == datetime(2015, 1, 1)


def test_set_date_underflow():
    """Test that setting zero or negative days causes month/year underflow"""
    # Setting day 0 goes to last day of previous month
    result = set_date(datetime(2014, 9, 15), 0)
    assert result == datetime(2014, 8, 31)
    
    # Setting negative day continues backwards
    result = set_date(datetime(2014, 9, 15), -1)
    assert result == datetime(2014, 8, 30)
    
    # January 0 goes to December 31 of previous year
    result = set_date(datetime(2014, 1, 15), 0)
    assert result == datetime(2013, 12, 31)
    
    # Multiple months backwards (March 1 with day -30 = January 29)
    result = set_date(datetime(2014, 3, 1), -30)
    assert result == datetime(2014, 1, 29)


def test_set_date_nan_day():
    """Test with NaN day returns invalid date"""
    result = set_date(datetime(2014, 9, 1), float('nan'))
    assert math.isnan(result.timestamp())


def test_set_date_invalid_input():
    """Test with invalid date input"""
    # Using NaN timestamp should raise ValueError
    with pytest.raises(ValueError):
        set_date(float('nan'), 15)


def test_set_date_does_not_mutate():
    """Test that the original date is not mutated"""
    date = datetime(2014, 9, 1)
    set_date(date, 20)
    assert date == datetime(2014, 9, 1)