import pytest
from datetime import datetime, timedelta
from .is_future import is_future


def test_is_future_true():
    """Test with future dates"""
    # Create a date 1 hour in the future
    future_date = datetime.now() + timedelta(hours=1)
    assert is_future(future_date) == True
    
    # Test with timestamp
    assert is_future(future_date.timestamp()) == True


def test_is_future_false():
    """Test with past dates"""
    # Create a date 1 hour in the past
    past_date = datetime.now() - timedelta(hours=1)
    assert is_future(past_date) == False
    
    # Test with timestamp
    assert is_future(past_date.timestamp()) == False


def test_is_future_invalid_date():
    """Test with invalid dates"""
    assert is_future(float('nan')) == False
    assert is_future('invalid') == False


def test_is_future_current_time():
    """Test with current time (should be False since it's not in the future)"""
    # Current time should not be in the future
    now = datetime.now()
    assert is_future(now) == False