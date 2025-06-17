
import pytest
from datetime import datetime
import math
from .start_of_quarter import start_of_quarter


def test_start_of_quarter_basic():
    """Test setting time to start of quarter"""
    # September 2, 2014 11:55:00 -> July 1, 2014 00:00:00
    date = datetime(2014, 9, 2, 11, 55, 0)
    result = start_of_quarter(date)
    assert result == datetime(2014, 7, 1, 0, 0, 0)


def test_start_of_quarter_all_quarters():
    """Test all four quarters"""
    # Q1: January, February, March -> January 1
    assert start_of_quarter(datetime(2014, 1, 15)) == datetime(2014, 1, 1)
    assert start_of_quarter(datetime(2014, 2, 20)) == datetime(2014, 1, 1)
    assert start_of_quarter(datetime(2014, 3, 31)) == datetime(2014, 1, 1)
    
    # Q2: April, May, June -> April 1
    assert start_of_quarter(datetime(2014, 4, 10)) == datetime(2014, 4, 1)
    assert start_of_quarter(datetime(2014, 5, 15)) == datetime(2014, 4, 1)
    assert start_of_quarter(datetime(2014, 6, 30)) == datetime(2014, 4, 1)
    
    # Q3: July, August, September -> July 1
    assert start_of_quarter(datetime(2014, 7, 5)) == datetime(2014, 7, 1)
    assert start_of_quarter(datetime(2014, 8, 20)) == datetime(2014, 7, 1)
    assert start_of_quarter(datetime(2014, 9, 30)) == datetime(2014, 7, 1)
    
    # Q4: October, November, December -> October 1
    assert start_of_quarter(datetime(2014, 10, 10)) == datetime(2014, 10, 1)
    assert start_of_quarter(datetime(2014, 11, 15)) == datetime(2014, 10, 1)
    assert start_of_quarter(datetime(2014, 12, 31)) == datetime(2014, 10, 1)


def test_start_of_quarter_with_timestamp():
    """Test with timestamp input"""
    timestamp = datetime(2014, 9, 2, 11, 55, 0).timestamp()
    result = start_of_quarter(timestamp)
    assert result == datetime(2014, 7, 1, 0, 0, 0)


def test_start_of_quarter_preserves_date_object():
    """Test that original date is not mutated"""
    date = datetime(2014, 9, 2, 11, 55, 0)
    original = datetime(2014, 9, 2, 11, 55, 0)
    start_of_quarter(date)
    assert date == original


def test_start_of_quarter_edge_cases():
    """Test edge cases"""
    # Already at start of quarter
    date = datetime(2014, 7, 1, 0, 0, 0)
    result = start_of_quarter(date)
    assert result == datetime(2014, 7, 1, 0, 0, 0)
    
    # End of year
    date = datetime(2014, 12, 31, 23, 59, 59, 999999)
    result = start_of_quarter(date)
    assert result == datetime(2014, 10, 1, 0, 0, 0)
    
    # Start of year
    date = datetime(2014, 1, 1, 0, 0, 0)
    result = start_of_quarter(date)
    assert result == datetime(2014, 1, 1, 0, 0, 0)
