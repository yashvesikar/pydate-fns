import pytest
from datetime import datetime
import math
from .set_month import set_month


def test_set_month_basic():
    """Test basic month setting"""
    # Set February to September 1, 2014
    result = set_month(datetime(2014, 9, 1), 2)
    assert result == datetime(2014, 2, 1)
    
    # Set December
    result = set_month(datetime(2014, 9, 15, 11, 55, 0), 12)
    assert result == datetime(2014, 12, 15, 11, 55, 0)


def test_set_month_preserves_time():
    """Test that time components are preserved"""
    result = set_month(datetime(2014, 9, 1, 11, 55, 59), 3)
    assert result == datetime(2014, 3, 1, 11, 55, 59)


def test_set_month_with_timestamp():
    """Test set_month with timestamp input"""
    dt = datetime(2014, 8, 15)
    result = set_month(dt.timestamp(), 4)
    assert result == datetime(2014, 4, 15)


def test_set_month_day_overflow():
    """Test that days overflow when target month has fewer days (like JavaScript)"""
    # January 31 → February = March 3rd (31 - 28 = 3 extra days in non-leap year)
    result = set_month(datetime(2014, 1, 31), 2)
    assert result == datetime(2014, 3, 3)
    
    # January 31 → February = March 2nd (31 - 29 = 2 extra days in leap year)
    result = set_month(datetime(2016, 1, 31), 2)
    assert result == datetime(2016, 3, 2)
    
    # January 31 → April = May 1st (31 - 30 = 1 extra day)
    result = set_month(datetime(2014, 1, 31), 4)
    assert result == datetime(2014, 5, 1)
    
    # May 31 → February = March 3rd (31 - 28 = 3 extra days)
    result = set_month(datetime(2014, 5, 31), 2)
    assert result == datetime(2014, 3, 3)


def test_set_month_no_overflow_needed():
    """Test when no day overflow is needed"""
    # January 15 → February 15 (valid day)
    result = set_month(datetime(2014, 1, 15), 2)
    assert result == datetime(2014, 2, 15)
    
    # December 1 → March 1
    result = set_month(datetime(2014, 12, 1), 3)
    assert result == datetime(2014, 3, 1)


def test_set_month_overflow():
    """Test month overflow to next year"""
    # Month 13 becomes January of next year
    result = set_month(datetime(2014, 6, 15), 13)
    assert result == datetime(2015, 1, 15)
    
    # Month 14 becomes February of next year
    result = set_month(datetime(2014, 6, 15), 14)
    assert result == datetime(2015, 2, 15)
    
    # Month 24 becomes December of next year
    result = set_month(datetime(2014, 6, 15), 24)
    assert result == datetime(2015, 12, 15)
    
    # Month 25 becomes January of year after next
    result = set_month(datetime(2014, 6, 15), 25)
    assert result == datetime(2016, 1, 15)


def test_set_month_underflow():
    """Test month underflow to previous year"""
    # Month 0 becomes December of previous year
    result = set_month(datetime(2014, 6, 15), 0)
    assert result == datetime(2013, 12, 15)
    
    # Month -1 becomes November of previous year
    result = set_month(datetime(2014, 6, 15), -1)
    assert result == datetime(2013, 11, 15)
    
    # Month -12 becomes December of year before previous
    result = set_month(datetime(2014, 6, 15), -12)
    assert result == datetime(2012, 12, 15)


def test_set_month_edge_cases_with_overflow():
    """Test edge cases where month overflow/underflow combines with day overflow"""
    # January 31 with month 14 (Feb next year) = March 3rd next year (day overflow)
    result = set_month(datetime(2014, 1, 31), 14)
    assert result == datetime(2015, 3, 3)
    
    # May 31 with month 0 (Dec previous year) = Dec 31 previous year (no day overflow)
    result = set_month(datetime(2014, 5, 31), 0)
    assert result == datetime(2013, 12, 31)


def test_set_month_nan_month():
    """Test with NaN month returns invalid date"""
    result = set_month(datetime(2014, 9, 1), float('nan'))
    assert math.isnan(result.timestamp())


def test_set_month_invalid_input():
    """Test with invalid date input"""
    with pytest.raises(ValueError):
        set_month(float('nan'), 6)


def test_set_month_does_not_mutate():
    """Test that the original date is not mutated"""
    date = datetime(2014, 9, 1)
    set_month(date, 3)
    assert date == datetime(2014, 9, 1)


def test_set_month_all_months():
    """Test setting all valid months"""
    base_date = datetime(2014, 6, 15)
    
    for month in range(1, 13):
        result = set_month(base_date, month)
        assert result.month == month
        assert result.year == 2014
        assert result.day == 15


def test_set_month_javascript_equivalence():
    """Test that behavior matches JavaScript Date.setMonth() exactly"""
    # These test cases match the JavaScript behavior we verified
    
    # July 15, 2014 (month 6 in JS, month 7 in Python) -> January (month 0 in JS, month 1 in Python)
    result = set_month(datetime(2014, 7, 15), 1)
    assert result == datetime(2014, 1, 15)
    
    # July 15, 2014 -> month -1 (should be December of previous year)
    result = set_month(datetime(2014, 7, 15), 0)
    assert result == datetime(2013, 12, 15)
    
    # July 15, 2014 -> month -2 (should be November of previous year)
    result = set_month(datetime(2014, 7, 15), -1)
    assert result == datetime(2013, 11, 15)
    
    # July 15, 2014 -> month 12 (should be January of next year)
    result = set_month(datetime(2014, 7, 15), 13)
    assert result == datetime(2015, 1, 15)
    
    # July 15, 2014 -> month 13 (should be February of next year)
    result = set_month(datetime(2014, 7, 15), 14)
    assert result == datetime(2015, 2, 15)