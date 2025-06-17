
import pytest
from datetime import datetime
import math
from .format import format


def test_format_basic_patterns():
    """Test basic format patterns"""
    date = datetime(2014, 2, 11, 15, 30, 45, 123456)
    
    # Year patterns
    assert format(date, 'yyyy') == '2014'
    assert format(date, 'yy') == '14'
    assert format(date, 'y') == '2014'
    
    # Month patterns
    assert format(date, 'MMMM') == 'February'
    assert format(date, 'MMM') == 'Feb'
    assert format(date, 'MM') == '02'
    assert format(date, 'M') == '2'
    
    # Day patterns
    assert format(date, 'dd') == '11'
    assert format(date, 'd') == '11'


def test_format_time_patterns():
    """Test time format patterns"""
    date = datetime(2014, 2, 11, 15, 30, 45, 123456)
    
    # Hour patterns (24-hour)
    assert format(date, 'HH') == '15'
    assert format(date, 'H') == '15'
    
    # Hour patterns (12-hour)
    assert format(date, 'hh') == '03'
    assert format(date, 'h') == '3'
    
    # Minute patterns
    assert format(date, 'mm') == '30'
    assert format(date, 'm') == '30'
    
    # Second patterns
    assert format(date, 'ss') == '45'
    assert format(date, 's') == '45'
    
    # AM/PM
    assert format(date, 'a') == 'PM'


def test_format_midnight_and_noon():
    """Test midnight and noon cases"""
    midnight = datetime(2014, 2, 11, 0, 0, 0)
    noon = datetime(2014, 2, 11, 12, 0, 0)
    
    # Midnight (12-hour format)
    assert format(midnight, 'h') == '12'
    assert format(midnight, 'hh') == '12'
    assert format(midnight, 'a') == 'AM'
    
    # Noon (12-hour format)
    assert format(noon, 'h') == '12'
    assert format(noon, 'hh') == '12'
    assert format(noon, 'a') == 'PM'


def test_format_milliseconds():
    """Test millisecond patterns"""
    date = datetime(2014, 2, 11, 15, 30, 45, 123456)
    
    assert format(date, 'SSS') == '123'
    assert format(date, 'SS') == '12'
    assert format(date, 'S') == '1'
    
    # Test with smaller microsecond values
    date_small = datetime(2014, 2, 11, 15, 30, 45, 1000)
    assert format(date_small, 'SSS') == '001'
    assert format(date_small, 'SS') == '00'
    assert format(date_small, 'S') == '0'


def test_format_combined_patterns():
    """Test combined format patterns"""
    date = datetime(2014, 2, 11, 15, 30, 45)
    
    # Standard date format
    assert format(date, 'MM/dd/yyyy') == '02/11/2014'
    
    # ISO-like format
    assert format(date, 'yyyy-MM-dd HH:mm:ss') == '2014-02-11 15:30:45'
    
    # 12-hour format with AM/PM
    assert format(date, 'h:mm a') == '3:30 PM'
    
    # Complex format
    assert format(date, 'MMMM d, yyyy') == 'February 11, 2014'


def test_format_quoted_strings():
    """Test quoted strings in format patterns"""
    date = datetime(2014, 7, 2, 15, 0, 0)
    
    # Single quoted text
    assert format(date, "h 'o''clock'") == "3 o'clock"
    
    # Simple quoted text
    assert format(date, "'Today is' MMMM d") == "Today is July 2"
    
    # Double quotes to produce single quote
    assert format(date, "''") == "'"


def test_format_edge_cases():
    """Test edge cases"""
    # Single digit values
    date = datetime(2001, 1, 1, 1, 1, 1)
    assert format(date, 'M/d/yyyy H:m:s') == '1/1/2001 1:1:1'
    assert format(date, 'MM/dd/yyyy HH:mm:ss') == '01/01/2001 01:01:01'
    
    # Year edge cases
    old_date = datetime(44, 1, 1)
    assert format(old_date, 'yyyy') == '0044'
    assert format(old_date, 'yy') == '44'
    assert format(old_date, 'y') == '44'


def test_format_with_timestamps():
    """Test format with timestamp inputs"""
    # Unix timestamp for 2014-02-11 15:30:45 UTC
    timestamp = 1392135045
    
    result = format(timestamp, 'yyyy-MM-dd HH:mm:ss')
    # Note: This will be in local timezone, so we just check the format structure
    assert len(result) == 19
    assert '-' in result
    assert ':' in result
    assert ' ' in result


def test_format_invalid_date():
    """Test format with invalid date"""
    with pytest.raises(ValueError, match="Invalid time value"):
        format(float('nan'), 'yyyy-MM-dd')


def test_format_unrecognized_tokens():
    """Test format with unrecognized tokens"""
    date = datetime(2014, 2, 11, 15, 30, 45)
    
    # Unrecognized tokens should be passed through unchanged
    assert format(date, 'yyyy-MM-dd X') == '2014-02-11 X'
    assert format(date, 'yyyy-MM-dd [Z]') == '2014-02-11 [Z]'
    
    # Note: Individual letters that match format tokens (H, d, etc.) will be replaced
    # This is expected behavior - use quotes to escape them if literal text is needed
    assert format(date, "'Hello world'") == 'Hello world'
