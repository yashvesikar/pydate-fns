
from datetime import datetime
from typing import Union
from ..to_date.to_date import to_date


def format_iso(date: Union[datetime, float, int]) -> str:
    """
    Format date to ISO 8601 string.
    
    Args:
        date: Date to format (datetime object or timestamp)
        
    Returns:
        str: ISO 8601 formatted date string
        
    Examples:
        >>> from datetime import datetime, timezone
        >>> format_iso(datetime(2014, 2, 11, 11, 30, 30))
        '2014-02-11T11:30:30'
        
        >>> format_iso(datetime(2014, 2, 11, 11, 30, 30, 768000))
        '2014-02-11T11:30:30.768'
        
        >>> format_iso(datetime(2014, 2, 11, 11, 30, 30, tzinfo=timezone.utc))
        '2014-02-11T11:30:30Z'
        
        >>> format_iso(1392123030.0)  # timestamp
        '2014-02-11T15:30:30Z'
    """
    dt = to_date(date)
    
    # Format the basic date and time components with consistent 4-digit year padding
    iso_string = f"{dt.year:04d}-{dt.month:02d}-{dt.day:02d}T{dt.hour:02d}:{dt.minute:02d}:{dt.second:02d}"
    
    # Add microseconds if present
    if dt.microsecond:
        # Format microseconds as fractional seconds
        # Start with 6 digits (microseconds), then strip trailing zeros
        fractional_str = f"{dt.microsecond:06d}".rstrip('0')
        iso_string += f".{fractional_str}"
    
    # Add timezone information
    if dt.tzinfo is not None:
        # Get timezone offset
        offset = dt.utcoffset()
        if offset is None:
            # Should not happen, but handle gracefully
            pass
        elif offset.total_seconds() == 0:
            # UTC timezone
            iso_string += 'Z'
        else:
            # Calculate offset hours and minutes
            total_seconds = int(offset.total_seconds())
            hours, remainder = divmod(abs(total_seconds), 3600)
            minutes = remainder // 60
            
            # Format the offset
            sign = '+' if total_seconds >= 0 else '-'
            iso_string += f"{sign}{hours:02d}:{minutes:02d}"
    
    return iso_string
