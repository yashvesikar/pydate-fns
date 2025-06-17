from datetime import datetime, timedelta
from typing import Union
import math
from ..to_date import to_date


def set_milliseconds(date: Union[datetime, int, float], milliseconds: Union[int, float]) -> datetime:
    """
    Set the milliseconds to the given date.
    
    Set the milliseconds to the given date. Milliseconds overflow will adjust the second/minute/hour/date accordingly.
    
    Args:
        date: The date to be changed
        milliseconds: The milliseconds of the new date (0-999, but overflow is allowed)
        
    Returns:
        The new date with the milliseconds set
        
    Examples:
        >>> from datetime import datetime
        >>> # Set 500 milliseconds to 1 September 2014 11:30:15.123:
        >>> set_milliseconds(datetime(2014, 9, 1, 11, 30, 15, 123000), 500)
        datetime.datetime(2014, 9, 1, 11, 30, 15, 500000)
        >>> # Millisecond 1500 overflows to next second:
        >>> set_milliseconds(datetime(2014, 9, 1, 11, 30, 15, 123000), 1500)
        datetime.datetime(2014, 9, 1, 11, 30, 16, 500000)
    """
    # Handle NaN milliseconds
    if isinstance(milliseconds, float) and math.isnan(milliseconds):
        class InvalidDateTime(datetime):
            def timestamp(self):
                return float('nan')
        return InvalidDateTime(1970, 1, 1)
    
    dt = to_date(date)
    
    # Handle NaN input date
    try:
        if math.isnan(dt.timestamp()):
            return dt
    except (ValueError, OSError):
        return dt
    
    # Reset to start of second, then add milliseconds (handles overflow like JavaScript)
    start_of_second = dt.replace(microsecond=0)
    return start_of_second + timedelta(milliseconds=int(milliseconds))