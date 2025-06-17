
from datetime import datetime

from .get_day_of_year import get_day_of_year


def test_get_day_of_year_returns_correct_day():
    """Returns the correct day of year"""
    # July 2nd, 2014 is the 183rd day of the year
    result = get_day_of_year(datetime(2014, 7, 2))
    assert result == 183


def test_get_day_of_year_january_first():
    """Returns 1 for January 1st"""
    result = get_day_of_year(datetime(2014, 1, 1))
    assert result == 1


def test_get_day_of_year_december_31st_non_leap():
    """Returns 365 for December 31st in non-leap year"""
    result = get_day_of_year(datetime(2014, 12, 31))
    assert result == 365


def test_get_day_of_year_december_31st_leap():
    """Returns 366 for December 31st in leap year"""
    result = get_day_of_year(datetime(2016, 12, 31))  # 2016 is leap year
    assert result == 366


def test_get_day_of_year_accepts_timestamp():
    """Accepts a timestamp"""
    timestamp = datetime(2014, 7, 2).timestamp()
    result = get_day_of_year(timestamp)
    assert result == 183


def test_get_day_of_year_leap_year_february():
    """Handles leap year February correctly"""
    # Feb 29, 2016 (leap year) should be day 60
    result = get_day_of_year(datetime(2016, 2, 29))
    assert result == 60
    
    # March 1, 2016 (leap year) should be day 61
    result = get_day_of_year(datetime(2016, 3, 1))
    assert result == 61


def test_get_day_of_year_various_dates():
    """Tests various dates throughout the year"""
    test_cases = [
        (datetime(2014, 1, 31), 31),    # End of January
        (datetime(2014, 2, 28), 59),    # End of February (non-leap)
        (datetime(2014, 3, 1), 60),     # March 1st (non-leap)
        (datetime(2014, 6, 15), 166),   # Mid June
        (datetime(2014, 9, 1), 244),    # September 1st
        (datetime(2014, 10, 31), 304),  # Halloween
        (datetime(2014, 12, 1), 335),   # December 1st
    ]
    
    for date, expected_day in test_cases:
        result = get_day_of_year(date)
        assert result == expected_day, f"Failed for {date}: expected {expected_day}, got {result}"


def test_get_day_of_year_different_years():
    """Works correctly across different years"""
    # Same date, different years
    for year in [2010, 2015, 2020, 2025]:
        result = get_day_of_year(datetime(year, 6, 15))
        # June 15th is always day 166 in non-leap years, 167 in leap years
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):  # Leap year
            assert result == 167
        else:
            assert result == 166
