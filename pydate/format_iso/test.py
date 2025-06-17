
import pytest
from datetime import datetime, timezone, timedelta
from .format_iso import format_iso


def test_basic_iso_format():
    """Test basic ISO 8601 date formatting."""
    result = format_iso(datetime(2014, 2, 11, 11, 30, 30))
    expected = '2014-02-11T11:30:30'
    assert result == expected


def test_iso_with_microseconds():
    """Test ISO formatting with microseconds."""
    result = format_iso(datetime(2014, 2, 11, 11, 30, 30, 768000))
    expected = '2014-02-11T11:30:30.768'
    assert result == expected
    
    # Test with different microsecond values
    result = format_iso(datetime(2014, 2, 11, 11, 30, 30, 123000))
    expected = '2014-02-11T11:30:30.123'
    assert result == expected
    
    # Test with microseconds that have trailing zeros
    result = format_iso(datetime(2014, 2, 11, 11, 30, 30, 500000))
    expected = '2014-02-11T11:30:30.5'
    assert result == expected


def test_iso_with_utc_timezone():
    """Test ISO formatting with UTC timezone."""
    result = format_iso(datetime(2014, 2, 11, 11, 30, 30, tzinfo=timezone.utc))
    expected = '2014-02-11T11:30:30Z'
    assert result == expected


def test_iso_with_timezone_offset():
    """Test ISO formatting with timezone offset."""
    # Positive offset
    tz_plus = timezone(timedelta(hours=7))
    result = format_iso(datetime(2014, 2, 11, 11, 30, 30, tzinfo=tz_plus))
    expected = '2014-02-11T11:30:30+07:00'
    assert result == expected
    
    # Negative offset
    tz_minus = timezone(timedelta(hours=-5))
    result = format_iso(datetime(2014, 2, 11, 11, 30, 30, tzinfo=tz_minus))
    expected = '2014-02-11T11:30:30-05:00'
    assert result == expected
    
    # Offset with minutes
    tz_minutes = timezone(timedelta(hours=5, minutes=30))
    result = format_iso(datetime(2014, 2, 11, 11, 30, 30, tzinfo=tz_minutes))
    expected = '2014-02-11T11:30:30+05:30'
    assert result == expected


def test_iso_with_timestamp_input():
    """Test ISO formatting with timestamp input."""
    # Timestamp is interpreted as local time (without timezone info)
    timestamp = 1392123030.0
    result = format_iso(timestamp)
    # Note: Result depends on system timezone, this is local time representation
    # On this system, timestamp 1392123030 is 2014-02-11 04:50:30 local time
    assert result.startswith('2014-02-11T')
    assert 'Z' not in result  # Should not have timezone since it's treated as local time
    
    # Integer timestamp
    result = format_iso(1392123030)
    assert result.startswith('2014-02-11T')
    assert 'Z' not in result


def test_iso_edge_cases():
    """Test edge cases for ISO formatting."""
    # Start of year
    result = format_iso(datetime(2014, 1, 1, 0, 0, 0))
    expected = '2014-01-01T00:00:00'
    assert result == expected
    
    # End of year
    result = format_iso(datetime(2014, 12, 31, 23, 59, 59))
    expected = '2014-12-31T23:59:59'
    assert result == expected
    
    # Leap year date
    result = format_iso(datetime(2016, 2, 29, 12, 0, 0))
    expected = '2016-02-29T12:00:00'
    assert result == expected


def test_iso_with_small_microseconds():
    """Test ISO formatting with small microsecond values."""
    # Single digit microseconds
    result = format_iso(datetime(2014, 2, 11, 11, 30, 30, 1000))
    expected = '2014-02-11T11:30:30.001'
    assert result == expected
    
    # Two digit microseconds
    result = format_iso(datetime(2014, 2, 11, 11, 30, 30, 10000))
    expected = '2014-02-11T11:30:30.01'
    assert result == expected
    
    # Very small microseconds
    result = format_iso(datetime(2014, 2, 11, 11, 30, 30, 100))
    expected = '2014-02-11T11:30:30.0001'
    assert result == expected


def test_iso_compatibility_with_parse_iso():
    """Test that format_iso output can be parsed by parse_iso."""
    from ..parse_iso.parse_iso import parse_iso
    
    # Test various datetime objects
    test_dates = [
        datetime(2014, 2, 11, 11, 30, 30),
        datetime(2014, 2, 11, 11, 30, 30, 768000),
        datetime(2014, 2, 11, 11, 30, 30, tzinfo=timezone.utc),
        datetime(2014, 2, 11, 11, 30, 30, tzinfo=timezone(timedelta(hours=7))),
        datetime(2014, 2, 11, 11, 30, 30, tzinfo=timezone(timedelta(hours=-5))),
    ]
    
    for dt in test_dates:
        iso_string = format_iso(dt)
        parsed_dt = parse_iso(iso_string)
        
        # Should be equal (accounting for potential timezone differences)
        if dt.tzinfo is None:
            # Original has no timezone, parsed should also have no timezone
            assert parsed_dt.tzinfo is None
            assert parsed_dt == dt
        else:
            # Both should have timezone info and represent the same moment
            assert parsed_dt.tzinfo is not None
            # Convert both to UTC for comparison
            dt_utc = dt.utctimetuple()
            parsed_utc = parsed_dt.utctimetuple()
            assert dt_utc == parsed_utc
            assert dt.microsecond == parsed_dt.microsecond


def test_year_formatting():
    """Test various year formats."""
    # Single digit year (padded to 4 digits)
    result = format_iso(datetime(1, 1, 1, 0, 0, 0))
    expected = '0001-01-01T00:00:00'
    assert result == expected
    
    # Three digit year
    result = format_iso(datetime(100, 1, 1, 0, 0, 0))
    expected = '0100-01-01T00:00:00'
    assert result == expected
    
    # Four digit year  
    result = format_iso(datetime(2000, 1, 1, 0, 0, 0))
    expected = '2000-01-01T00:00:00'
    assert result == expected


def test_month_and_day_formatting():
    """Test month and day formatting with leading zeros."""
    # Single digit month and day
    result = format_iso(datetime(2014, 1, 1, 0, 0, 0))
    expected = '2014-01-01T00:00:00'
    assert result == expected
    
    # Two digit month and day
    result = format_iso(datetime(2014, 12, 31, 0, 0, 0))
    expected = '2014-12-31T00:00:00'
    assert result == expected


def test_time_formatting():
    """Test time component formatting."""
    # Single digit hours, minutes, seconds
    result = format_iso(datetime(2014, 1, 1, 1, 1, 1))
    expected = '2014-01-01T01:01:01'
    assert result == expected
    
    # Two digit hours, minutes, seconds
    result = format_iso(datetime(2014, 1, 1, 23, 59, 59))
    expected = '2014-01-01T23:59:59'
    assert result == expected
