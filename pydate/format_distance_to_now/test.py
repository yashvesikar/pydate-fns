
import pytest
from datetime import datetime, timedelta
from .format_distance_to_now import format_distance_to_now


def test_format_distance_to_now_past_dates():
    """Test distance formatting for past dates"""
    # Note: Since we're comparing to "now", we need to use relative dates
    past_3_days = datetime.now() - timedelta(days=3)
    past_2_hours = datetime.now() - timedelta(hours=2)
    past_45_seconds = datetime.now() - timedelta(seconds=45)
    
    # Basic distance
    assert "3 days" in format_distance_to_now(past_3_days)
    assert "about 2 hours" in format_distance_to_now(past_2_hours)
    assert "1 minute" in format_distance_to_now(past_45_seconds)
    
    # With suffix
    assert "3 days ago" in format_distance_to_now(past_3_days, {'addSuffix': True})
    assert "about 2 hours ago" in format_distance_to_now(past_2_hours, {'addSuffix': True})


def test_format_distance_to_now_future_dates():
    """Test distance formatting for future dates"""
    future_3_days = datetime.now() + timedelta(days=3)
    future_2_hours = datetime.now() + timedelta(hours=2)
    
    # Basic distance
    assert "3 days" in format_distance_to_now(future_3_days)
    assert "about 2 hours" in format_distance_to_now(future_2_hours)
    
    # With suffix
    assert "in 3 days" in format_distance_to_now(future_3_days, {'addSuffix': True})
    assert "in about 2 hours" in format_distance_to_now(future_2_hours, {'addSuffix': True})


def test_format_distance_to_now_seconds_option():
    """Test includeSeconds option"""
    past_15_seconds = datetime.now() - timedelta(seconds=15)
    past_25_seconds = datetime.now() - timedelta(seconds=25)
    
    # Without includeSeconds
    assert "less than a minute" in format_distance_to_now(past_15_seconds)
    
    # With includeSeconds
    assert "less than 20 seconds" in format_distance_to_now(past_15_seconds, {'includeSeconds': True})
    assert "half a minute" in format_distance_to_now(past_25_seconds, {'includeSeconds': True})


def test_format_distance_to_now_edge_cases():
    """Test edge cases"""
    # Very close to now
    assert "less than a minute" in format_distance_to_now(datetime.now())
    
    # Just now with includeSeconds
    assert "less than 5 seconds" in format_distance_to_now(datetime.now(), {'includeSeconds': True})


def test_format_distance_to_now_with_timestamps():
    """Test with timestamp inputs"""
    # 1 hour ago
    past_timestamp = datetime.now().timestamp() - 3600
    result = format_distance_to_now(past_timestamp)
    assert "about 1 hour" in result


def test_format_distance_to_now_invalid_dates():
    """Test with invalid dates"""
    with pytest.raises(ValueError, match="Invalid time value"):
        format_distance_to_now(float('nan'))
