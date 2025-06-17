
from datetime import datetime

from .get_quarter import get_quarter


def test_get_quarter_q1():
    """Returns 1 for first quarter months"""
    q1_months = [1, 2, 3]  # Jan, Feb, Mar
    
    for month in q1_months:
        result = get_quarter(datetime(2014, month, 15))
        assert result == 1, f"Month {month} should be in Q1"


def test_get_quarter_q2():
    """Returns 2 for second quarter months"""
    q2_months = [4, 5, 6]  # Apr, May, Jun
    
    for month in q2_months:
        result = get_quarter(datetime(2014, month, 15))
        assert result == 2, f"Month {month} should be in Q2"


def test_get_quarter_q3():
    """Returns 3 for third quarter months"""
    q3_months = [7, 8, 9]  # Jul, Aug, Sep
    
    for month in q3_months:
        result = get_quarter(datetime(2014, month, 15))
        assert result == 3, f"Month {month} should be in Q3"


def test_get_quarter_q4():
    """Returns 4 for fourth quarter months"""
    q4_months = [10, 11, 12]  # Oct, Nov, Dec
    
    for month in q4_months:
        result = get_quarter(datetime(2014, month, 15))
        assert result == 4, f"Month {month} should be in Q4"


def test_get_quarter_specific_example():
    """Returns 3 for July 2, 2014 (from date-fns example)"""
    result = get_quarter(datetime(2014, 7, 2))
    assert result == 3


def test_get_quarter_accepts_timestamp():
    """Accepts a timestamp"""
    timestamp = datetime(2014, 7, 2).timestamp()
    result = get_quarter(timestamp)
    assert result == 3


def test_get_quarter_different_years():
    """Works correctly across different years"""
    # Same month, different years should return same quarter
    years = [2010, 2015, 2020, 2025]
    
    for year in years:
        result = get_quarter(datetime(year, 7, 15))  # July = Q3
        assert result == 3, f"July {year} should be Q3"


def test_get_quarter_month_boundaries():
    """Tests month boundaries correctly"""
    test_cases = [
        (datetime(2014, 1, 1), 1),    # January 1st -> Q1
        (datetime(2014, 3, 31), 1),   # March 31st -> Q1
        (datetime(2014, 4, 1), 2),    # April 1st -> Q2
        (datetime(2014, 6, 30), 2),   # June 30th -> Q2
        (datetime(2014, 7, 1), 3),    # July 1st -> Q3
        (datetime(2014, 9, 30), 3),   # September 30th -> Q3
        (datetime(2014, 10, 1), 4),   # October 1st -> Q4
        (datetime(2014, 12, 31), 4),  # December 31st -> Q4
    ]
    
    for date, expected_quarter in test_cases:
        result = get_quarter(date)
        assert result == expected_quarter, f"Date {date} should be in Q{expected_quarter}"
