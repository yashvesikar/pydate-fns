
import pytest
from datetime import datetime
from .is_weekend import is_weekend


def test_is_weekend_saturday():
    """Test that Saturday is identified as weekend"""
    # October 4, 2014 is a Saturday
    assert is_weekend(datetime(2014, 10, 4)) is True


def test_is_weekend_sunday():
    """Test that Sunday is identified as weekend"""
    # October 5, 2014 is a Sunday
    assert is_weekend(datetime(2014, 10, 5)) is True


def test_is_weekend_weekdays():
    """Test that weekdays are not identified as weekend"""
    # Monday
    assert is_weekend(datetime(2014, 10, 6)) is False
    # Tuesday
    assert is_weekend(datetime(2014, 10, 7)) is False
    # Wednesday
    assert is_weekend(datetime(2014, 10, 8)) is False
    # Thursday
    assert is_weekend(datetime(2014, 10, 9)) is False
    # Friday
    assert is_weekend(datetime(2014, 10, 10)) is False


def test_is_weekend_with_timestamps():
    """Test is_weekend with timestamp inputs"""
    # Create timestamps from known weekend/weekday dates
    saturday = datetime(2014, 10, 4)  # Saturday
    monday = datetime(2014, 10, 6)    # Monday
    
    saturday_timestamp = saturday.timestamp()
    monday_timestamp = monday.timestamp()
    
    assert is_weekend(saturday_timestamp) is True
    assert is_weekend(monday_timestamp) is False


def test_is_weekend_edge_cases():
    """Test edge cases"""
    # Test start of Saturday
    assert is_weekend(datetime(2014, 10, 4, 0, 0, 0)) is True
    
    # Test end of Sunday
    assert is_weekend(datetime(2014, 10, 5, 23, 59, 59)) is True
    
    # Test Friday night
    assert is_weekend(datetime(2014, 10, 3, 23, 59, 59)) is False
    
    # Test Monday morning
    assert is_weekend(datetime(2014, 10, 6, 0, 0, 0)) is False


def test_is_weekend_various_years():
    """Test weekends across different years"""
    # Saturday January 1, 2000
    assert is_weekend(datetime(2000, 1, 1)) is True
    
    # Sunday December 31, 2023
    assert is_weekend(datetime(2023, 12, 31)) is True
    
    # Wednesday February 29, 2024 (leap year)
    assert is_weekend(datetime(2024, 2, 29)) is False
