import pytest
from datetime import datetime, timedelta
from .is_past import is_past


def test_is_past_true():
    """Test with past dates"""
    # Create a date 1 hour in the past
    past_date = datetime.now() - timedelta(hours=1)
    assert is_past(past_date) == True
    
    # Test with timestamp
    assert is_past(past_date.timestamp()) == True


def test_is_past_false():
    """Test with future dates"""
    # Create a date 1 hour in the future
    future_date = datetime.now() + timedelta(hours=1)
    assert is_past(future_date) == False
    
    # Test with timestamp
    assert is_past(future_date.timestamp()) == False


def test_is_past_invalid_date():
    """Test with invalid dates"""
    assert is_past(float('nan')) == False
    assert is_past('invalid') == False


def test_is_past_current_time():
    """Test with current time (should be False since it's not in the past)"""
    # Current time plus small buffer should not be in the past
    now = datetime.now() + timedelta(milliseconds=100)
    assert is_past(now) == False