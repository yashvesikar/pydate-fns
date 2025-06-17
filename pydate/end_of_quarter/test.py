
import pytest
from datetime import datetime
import math
from .end_of_quarter import end_of_quarter


def test_end_of_quarter_basic():
    """Test setting time to end of quarter"""
    # September 2, 2014 11:55:00 -> September 30, 2014 23:59:59.999999
    date = datetime(2014, 9, 2, 11, 55, 0)
    result = end_of_quarter(date)
    assert result == datetime(2014, 9, 30, 23, 59, 59, 999999)


def test_end_of_quarter_all_quarters():
    """Test all four quarters"""
    # Q1: January, February, March -> March 31
    assert end_of_quarter(datetime(2014, 1, 15)) == datetime(2014, 3, 31, 23, 59, 59, 999999)
    assert end_of_quarter(datetime(2014, 2, 20)) == datetime(2014, 3, 31, 23, 59, 59, 999999)
    assert end_of_quarter(datetime(2014, 3, 31)) == datetime(2014, 3, 31, 23, 59, 59, 999999)
    
    # Q2: April, May, June -> June 30
    assert end_of_quarter(datetime(2014, 4, 10)) == datetime(2014, 6, 30, 23, 59, 59, 999999)
    assert end_of_quarter(datetime(2014, 5, 15)) == datetime(2014, 6, 30, 23, 59, 59, 999999)
    assert end_of_quarter(datetime(2014, 6, 30)) == datetime(2014, 6, 30, 23, 59, 59, 999999)
    
    # Q3: July, August, September -> September 30
    assert end_of_quarter(datetime(2014, 7, 5)) == datetime(2014, 9, 30, 23, 59, 59, 999999)
    assert end_of_quarter(datetime(2014, 8, 20)) == datetime(2014, 9, 30, 23, 59, 59, 999999)
    assert end_of_quarter(datetime(2014, 9, 30)) == datetime(2014, 9, 30, 23, 59, 59, 999999)
    
    # Q4: October, November, December -> December 31
    assert end_of_quarter(datetime(2014, 10, 10)) == datetime(2014, 12, 31, 23, 59, 59, 999999)
    assert end_of_quarter(datetime(2014, 11, 15)) == datetime(2014, 12, 31, 23, 59, 59, 999999)
    assert end_of_quarter(datetime(2014, 12, 31)) == datetime(2014, 12, 31, 23, 59, 59, 999999)


def test_end_of_quarter_with_timestamp():
    """Test with timestamp input"""
    timestamp = datetime(2014, 9, 2, 11, 55, 0).timestamp()
    result = end_of_quarter(timestamp)
    assert result == datetime(2014, 9, 30, 23, 59, 59, 999999)


def test_end_of_quarter_preserves_date_object():
    """Test that original date is not mutated"""
    date = datetime(2014, 9, 2, 11, 55, 0)
    original = datetime(2014, 9, 2, 11, 55, 0)
    end_of_quarter(date)
    assert date == original


def test_end_of_quarter_edge_cases():
    """Test edge cases"""
    # Already at end of quarter
    date = datetime(2014, 9, 30, 23, 59, 59, 999999)
    result = end_of_quarter(date)
    assert result == datetime(2014, 9, 30, 23, 59, 59, 999999)
    
    # Start of year
    date = datetime(2014, 1, 1, 0, 0, 0)
    result = end_of_quarter(date)
    assert result == datetime(2014, 3, 31, 23, 59, 59, 999999)
    
    # End of year
    date = datetime(2014, 12, 31, 0, 0, 0)
    result = end_of_quarter(date)
    assert result == datetime(2014, 12, 31, 23, 59, 59, 999999)
    
    # Leap year February
    date = datetime(2016, 2, 15)  # 2016 is a leap year
    result = end_of_quarter(date)
    assert result == datetime(2016, 3, 31, 23, 59, 59, 999999)
