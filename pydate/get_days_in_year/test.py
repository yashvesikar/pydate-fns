
from datetime import datetime

from .get_days_in_year import get_days_in_year


def test_get_days_in_year_leap_year():
    """Returns 366 for leap year"""
    result = get_days_in_year(datetime(2012, 1, 1))  # 2012 is leap year
    assert result == 366


def test_get_days_in_year_non_leap_year():
    """Returns 365 for non-leap year"""
    result = get_days_in_year(datetime(2013, 1, 1))  # 2013 is not leap year
    assert result == 365


def test_get_days_in_year_century_leap_years():
    """Returns correct values for century leap years"""
    # Century years divisible by 400 are leap years
    assert get_days_in_year(datetime(2000, 6, 15)) == 366  # 2000 is leap
    assert get_days_in_year(datetime(1600, 6, 15)) == 366  # 1600 is leap


def test_get_days_in_year_century_non_leap_years():
    """Returns correct values for century non-leap years"""
    # Century years not divisible by 400 are not leap years
    assert get_days_in_year(datetime(1900, 6, 15)) == 365  # 1900 is not leap
    assert get_days_in_year(datetime(1800, 6, 15)) == 365  # 1800 is not leap


def test_get_days_in_year_accepts_timestamp():
    """Accepts a timestamp"""
    timestamp = datetime(2012, 1, 1).timestamp()
    result = get_days_in_year(timestamp)
    assert result == 366


def test_get_days_in_year_different_dates_same_year():
    """Returns same result for different dates in same year"""
    # Different dates in 2012 should all return 366
    dates = [
        datetime(2012, 1, 1),    # January 1st
        datetime(2012, 6, 15),   # Mid year
        datetime(2012, 12, 31),  # December 31st
    ]
    
    for date in dates:
        result = get_days_in_year(date)
        assert result == 366, f"Date {date} in 2012 should return 366"


def test_get_days_in_year_various_years():
    """Tests various years"""
    test_cases = [
        (2000, 366),  # Leap year (divisible by 400)
        (2001, 365),  # Non-leap year
        (2004, 366),  # Leap year (divisible by 4)
        (2100, 365),  # Non-leap year (divisible by 100 but not 400)
        (2020, 366),  # Recent leap year
        (2021, 365),  # Recent non-leap year
    ]
    
    for year, expected_days in test_cases:
        result = get_days_in_year(datetime(year, 7, 1))
        assert result == expected_days, f"Year {year} should have {expected_days} days"
