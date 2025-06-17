
import pytest
from datetime import datetime
import math
from .is_same_week import is_same_week


def test_is_same_week_basic():
    """Test basic same week functionality"""
    # August 31, 2014 (Sunday) and September 4, 2014 (Thursday) are in the same week
    # when week starts on Sunday (default)
    assert is_same_week(datetime(2014, 8, 31), datetime(2014, 9, 4)) == True
    
    # August 30, 2014 (Saturday) and September 4, 2014 (Thursday) are in different weeks
    assert is_same_week(datetime(2014, 8, 30), datetime(2014, 9, 4)) == False


def test_is_same_week_different_week_starts_on():
    """Test with different week start days"""
    # With Monday as first day of week (week_starts_on=1)
    # August 31, 2014 (Sunday) and September 4, 2014 (Thursday) are in different weeks
    assert is_same_week(datetime(2014, 8, 31), datetime(2014, 9, 4), week_starts_on=1) == False
    
    # But September 1, 2014 (Monday) and September 4, 2014 (Thursday) are in the same week
    assert is_same_week(datetime(2014, 9, 1), datetime(2014, 9, 4), week_starts_on=1) == True


def test_is_same_week_same_date():
    """Test with same date"""
    date = datetime(2014, 8, 31, 12, 30, 45)
    assert is_same_week(date, date) == True


def test_is_same_week_with_timestamps():
    """Test with timestamp inputs"""
    timestamp1 = datetime(2014, 8, 31).timestamp()
    timestamp2 = datetime(2014, 9, 4).timestamp()
    assert is_same_week(timestamp1, timestamp2) == True
