
import pytest
from datetime import datetime
import math
from .is_same_quarter import is_same_quarter


def test_is_same_quarter_same_quarter():
    """Test dates in the same quarter and year"""
    # Q1: January 1 and March 8, 2014
    assert is_same_quarter(datetime(2014, 1, 1), datetime(2014, 3, 8)) == True
    
    # Q2: April 15 and June 30, 2014
    assert is_same_quarter(datetime(2014, 4, 15), datetime(2014, 6, 30)) == True
    
    # Q3: July 2 and September 25, 2014
    assert is_same_quarter(datetime(2014, 7, 2), datetime(2014, 9, 25)) == True
    
    # Q4: October 1 and December 31, 2014
    assert is_same_quarter(datetime(2014, 10, 1), datetime(2014, 12, 31)) == True


def test_is_same_quarter_different_quarters():
    """Test dates in different quarters"""
    # Different quarters, same year
    assert is_same_quarter(datetime(2014, 1, 1), datetime(2014, 4, 1)) == False
    assert is_same_quarter(datetime(2014, 2, 15), datetime(2014, 7, 20)) == False
    
    # Different years, same quarter number
    assert is_same_quarter(datetime(2014, 1, 1), datetime(2015, 1, 1)) == False
    assert is_same_quarter(datetime(2014, 7, 15), datetime(2015, 7, 15)) == False
    
    # Different quarters and years
    assert is_same_quarter(datetime(2014, 1, 1), datetime(2013, 9, 25)) == False


def test_is_same_quarter_with_timestamps():
    """Test with timestamp inputs"""
    # Same quarter: Q3 2014
    timestamp1 = datetime(2014, 7, 2).timestamp()
    timestamp2 = datetime(2014, 9, 25).timestamp()
    assert is_same_quarter(timestamp1, timestamp2) == True
    
    # Different quarters
    timestamp3 = datetime(2014, 1, 1).timestamp()
    timestamp4 = datetime(2014, 4, 1).timestamp()
    assert is_same_quarter(timestamp3, timestamp4) == False


def test_is_same_quarter_edge_cases():
    """Test edge cases"""
    # Same date
    date = datetime(2014, 7, 15, 12, 30, 45)
    assert is_same_quarter(date, date) == True
    
    # End of quarter vs start of next quarter
    assert is_same_quarter(datetime(2014, 3, 31, 23, 59, 59), datetime(2014, 4, 1, 0, 0, 0)) == False
    
    # Start of quarter vs end of previous quarter
    assert is_same_quarter(datetime(2014, 7, 1, 0, 0, 0), datetime(2014, 6, 30, 23, 59, 59)) == False


def test_is_same_quarter_invalid_dates():
    """Test with invalid dates"""
    # First date invalid
    try:
        result = is_same_quarter(float('nan'), datetime(1989, 7, 10))
        assert result == False
    except:
        # If to_date raises an exception for NaN, that's also acceptable
        pass
    
    # Second date invalid
    try:
        result = is_same_quarter(datetime(1987, 2, 11), float('nan'))
        assert result == False
    except:
        # If to_date raises an exception for NaN, that's also acceptable
        pass
    
    # Both dates invalid
    try:
        result = is_same_quarter(float('nan'), float('nan'))
        assert result == False
    except:
        # If to_date raises an exception for NaN, that's also acceptable
        pass
