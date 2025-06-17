
from datetime import datetime

from .end_of_day import end_of_day


def test_end_of_day_returns_end_of_day():
    """Returns the end of a day for the given date"""
    result = end_of_day(datetime(2014, 9, 2, 11, 55, 0))
    assert result == datetime(2014, 9, 2, 23, 59, 59, 999999)


def test_end_of_day_accepts_timestamp():
    """Accepts a timestamp"""
    timestamp = datetime(2014, 9, 2, 11, 55, 0).timestamp()
    result = end_of_day(timestamp)
    assert result == datetime(2014, 9, 2, 23, 59, 59, 999999)


def test_end_of_day_does_not_mutate_original_date():
    """Does not mutate the original date"""
    original_date = datetime(2014, 9, 2, 11, 55, 0)
    original_time = original_date.time()
    
    end_of_day(original_date)
    
    # Original date should remain unchanged
    assert original_date.time() == original_time


def test_end_of_day_with_different_times():
    """Returns consistent end of day regardless of input time"""
    # Different times on the same day should all return the same end of day
    dates = [
        datetime(2014, 9, 2, 0, 0, 0),      # Start of day
        datetime(2014, 9, 2, 12, 30, 45),   # Middle of day  
        datetime(2014, 9, 2, 23, 0, 0),     # Near end of day
    ]
    
    expected = datetime(2014, 9, 2, 23, 59, 59, 999999)
    
    for date in dates:
        result = end_of_day(date)
        assert result == expected


def test_end_of_day_preserves_date():
    """Preserves the date part while setting time to end of day"""
    test_dates = [
        datetime(2020, 1, 1, 10, 20, 30),
        datetime(2020, 12, 31, 5, 45, 12),
        datetime(2021, 6, 15, 18, 30, 0),
    ]
    
    for date in test_dates:
        result = end_of_day(date)
        # Date should be preserved
        assert result.date() == date.date()
        # Time should be end of day
        assert result.hour == 23
        assert result.minute == 59
        assert result.second == 59
        assert result.microsecond == 999999
