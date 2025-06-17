from datetime import datetime, timedelta
from typing import Union
import math
from ..to_date import to_date


def set_seconds(date: Union[datetime, int, float], seconds: Union[int, float]) -> datetime:
    """
    Set the seconds to the given date.
    
    Set the seconds to the given date. Seconds overflow will adjust the minute/hour/date accordingly.
    
    Args:
        date: The date to be changed
        seconds: The seconds of the new date (0-59, but overflow is allowed)
        
    Returns:
        The new date with the seconds set
        
    Examples:
        >>> from datetime import datetime
        >>> # Set 30 seconds to 1 September 2014 11:30:15:
        >>> set_seconds(datetime(2014, 9, 1, 11, 30, 15), 30)
        datetime.datetime(2014, 9, 1, 11, 30, 30)
        >>> # Second 70 overflows to next minute:
        >>> set_seconds(datetime(2014, 9, 1, 11, 30, 15), 70)
        datetime.datetime(2014, 9, 1, 11, 31, 10)
    """
    # Handle NaN seconds
    if isinstance(seconds, float) and math.isnan(seconds):
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
    
    # Reset to start of minute, then add seconds (handles overflow like JavaScript)
    start_of_minute = dt.replace(second=0, microsecond=0)
    return start_of_minute + timedelta(seconds=int(seconds))