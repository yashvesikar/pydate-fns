from datetime import datetime
from typing import Union
import time
from ..to_date import to_date


def is_future(date: Union[datetime, int, float]) -> bool:
    """
    Is the given date in the future?
    
    Is the given date in the future?
    
    Args:
        date: The date to check
        
    Returns:
        The date is in the future
        
    Examples:
        >>> from datetime import datetime
        >>> # If today is 6 October 2014, is 31 December 2014 in the future?
        >>> is_future(datetime(2014, 12, 31))  # Assuming current time is before this
        True
    """
    try:
        dt = to_date(date)
        return dt.timestamp() > time.time()
    except (ValueError, TypeError, OSError):
        return False