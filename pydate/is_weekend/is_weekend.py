
from datetime import datetime
from typing import Union
from ..to_date import to_date


def is_weekend(date: Union[datetime, int, float]) -> bool:
    """
    Does the given date fall on a weekend?
    
    A weekend is either Saturday (5) or Sunday (6) in Python's weekday system,
    or Saturday (6) or Sunday (0) in JavaScript's getDay system.
    
    Args:
        date: The date to check
        
    Returns:
        True if the date falls on a weekend, False otherwise
        
    Examples:
        >>> from datetime import datetime
        >>> is_weekend(datetime(2014, 10, 5))  # Sunday
        True
        >>> is_weekend(datetime(2014, 10, 6))  # Monday
        False
        >>> is_weekend(datetime(2014, 10, 4))  # Saturday
        True
    """
    dt = to_date(date)
    
    # In Python, weekday() returns: Monday=0, Tuesday=1, ..., Saturday=5, Sunday=6
    # For weekend check, we want Saturday=5 or Sunday=6
    weekday = dt.weekday()
    return weekday == 5 or weekday == 6
