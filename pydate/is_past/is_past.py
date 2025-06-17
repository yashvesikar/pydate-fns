from datetime import datetime
from typing import Union
import time
from ..to_date import to_date


def is_past(date: Union[datetime, int, float]) -> bool:
    """
    Is the given date in the past?
    
    Is the given date in the past?
    
    Args:
        date: The date to check
        
    Returns:
        The date is in the past
        
    Examples:
        >>> from datetime import datetime
        >>> # If today is 6 October 2014, is 2 July 2014 in the past?
        >>> is_past(datetime(2014, 7, 2))  # Assuming current time is after this
        True
    """
    try:
        dt = to_date(date)
        return dt.timestamp() < time.time()
    except (ValueError, TypeError, OSError):
        return False