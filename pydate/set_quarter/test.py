
import pytest
from datetime import datetime
import math
from .set_quarter import set_quarter


def test_set_quarter_basic():
    """Test setting the quarter of the year"""
    # July 2, 2014 (Q3) -> set to Q1 -> January 2, 2014
    result = set_quarter(datetime(2014, 7, 2), 1)
    assert result == datetime(2014, 1, 2)
    
    # July 1, 2014 (Q3) -> set to Q4 -> October 1, 2014
    result = set_quarter(datetime(2014, 7, 1), 4)
    assert result == datetime(2014, 10, 1)


def test_set_quarter_all_quarters():
    """Test setting to each quarter"""
    date = datetime(2014, 7, 15, 10, 30, 45)  # Q3
    
    # Set to Q1
    result = set_quarter(date, 1)
    assert result == datetime(2014, 1, 15, 10, 30, 45)
    
    # Set to Q2
    result = set_quarter(date, 2)
    assert result == datetime(2014, 4, 15, 10, 30, 45)
    
    # Set to Q3 (same quarter)
    result = set_quarter(date, 3)
    assert result == datetime(2014, 7, 15, 10, 30, 45)
    
    # Set to Q4
    result = set_quarter(date, 4)
    assert result == datetime(2014, 10, 15, 10, 30, 45)


def test_set_quarter_end_of_month():
    """Test when the day doesn't exist in target month"""
    # November 30, 2014 (Q4) -> set to Q1 -> February 28, 2014
    result = set_quarter(datetime(2014, 11, 30), 1)
    assert result == datetime(2014, 2, 28)
    
    # May 31, 2014 (Q2) -> set to Q1 -> February 28, 2014
    result = set_quarter(datetime(2014, 5, 31), 1)
    assert result == datetime(2014, 2, 28)
    
    # Leap year: May 31, 2016 -> set to Q1 -> February 29, 2016
    result = set_quarter(datetime(2016, 5, 31), 1)
    assert result == datetime(2016, 2, 29)


def test_set_quarter_with_timestamps():
    """Test with timestamp input"""
    timestamp = datetime(2014, 7, 1).timestamp()
    result = set_quarter(timestamp, 4)
    assert result == datetime(2014, 10, 1)


def test_set_quarter_preserves_time():
    """Test that time components are preserved"""
    date = datetime(2014, 7, 1, 15, 30, 45, 123456)
    result = set_quarter(date, 2)
    assert result == datetime(2014, 4, 1, 15, 30, 45, 123456)


def test_set_quarter_preserves_date_object():
    """Test that original date is not mutated"""
    date = datetime(2014, 7, 1)
    original = datetime(2014, 7, 1)
    set_quarter(date, 2)
    assert date == original


def test_set_quarter_nan_quarter():
    """Test with NaN quarter"""
    with pytest.raises(ValueError, match="Quarter cannot be NaN"):
        set_quarter(datetime(2014, 7, 2), float('nan'))


def test_set_quarter_edge_cases():
    """Test edge cases"""
    # Quarter values that need wrapping
    # Quarter 0 -> Q4 of previous year
    result = set_quarter(datetime(2014, 4, 15), 0)  # Q2 -> Q4 of previous year
    assert result == datetime(2013, 10, 15)
    
    # Quarter 5 -> Q1 of next year
    result = set_quarter(datetime(2014, 7, 15), 5)  # Q3 -> Q1 of next year
    assert result == datetime(2015, 1, 15)
