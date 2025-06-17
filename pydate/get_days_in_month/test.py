
from datetime import datetime

from .get_days_in_month import get_days_in_month


def test_get_days_in_month_february_leap_year():
    """Returns 29 for February in leap year"""
    result = get_days_in_month(datetime(2000, 2, 1))  # 2000 is leap year
    assert result == 29


def test_get_days_in_month_february_non_leap_year():
    """Returns 28 for February in non-leap year"""
    result = get_days_in_month(datetime(2001, 2, 1))  # 2001 is not leap year
    assert result == 28


def test_get_days_in_month_31_day_months():
    """Returns 31 for months with 31 days"""
    months_31_days = [1, 3, 5, 7, 8, 10, 12]  # Jan, Mar, May, Jul, Aug, Oct, Dec
    
    for month in months_31_days:
        result = get_days_in_month(datetime(2021, month, 1))
        assert result == 31, f"Month {month} should have 31 days"


def test_get_days_in_month_30_day_months():
    """Returns 30 for months with 30 days"""
    months_30_days = [4, 6, 9, 11]  # Apr, Jun, Sep, Nov
    
    for month in months_30_days:
        result = get_days_in_month(datetime(2021, month, 1))
        assert result == 30, f"Month {month} should have 30 days"


def test_get_days_in_month_accepts_timestamp():
    """Accepts a timestamp"""
    timestamp = datetime(2000, 2, 1).timestamp()
    result = get_days_in_month(timestamp)
    assert result == 29


def test_get_days_in_month_different_days_same_month():
    """Returns same result regardless of day in month"""
    # Different days in February 2000 should all return 29
    days = [1, 15, 28, 29]
    
    for day in days:
        result = get_days_in_month(datetime(2000, 2, day))
        assert result == 29, f"Day {day} in Feb 2000 should return 29"


def test_get_days_in_month_leap_year_edge_cases():
    """Tests leap year edge cases"""
    # Century years divisible by 400 are leap years
    assert get_days_in_month(datetime(2000, 2, 1)) == 29  # 2000 is leap
    assert get_days_in_month(datetime(1600, 2, 1)) == 29  # 1600 is leap
    
    # Century years not divisible by 400 are not leap years
    assert get_days_in_month(datetime(1900, 2, 1)) == 28  # 1900 is not leap
    assert get_days_in_month(datetime(1800, 2, 1)) == 28  # 1800 is not leap
    
    # Regular divisible by 4 years are leap years
    assert get_days_in_month(datetime(2004, 2, 1)) == 29  # 2004 is leap
    assert get_days_in_month(datetime(2008, 2, 1)) == 29  # 2008 is leap
