from datetime import datetime, timedelta
from typing import Union
import math
from ..to_date import to_date


def set_minutes(date: Union[datetime, int, float], minutes: Union[int, float]) -> datetime:
    """
    Set the minutes to the given date.
    
    Set the minutes to the given date. Minutes overflow will adjust the hour/date accordingly.
    
    Args:
        date: The date to be changed
        minutes: The minutes of the new date (0-59, but overflow is allowed)
        
    Returns:
        The new date with the minutes set
        
    Examples:
        >>> from datetime import datetime
        >>> # Set 30 minutes to 1 September 2014 11:01:00:
        >>> set_minutes(datetime(2014, 9, 1, 11, 1), 30)
        datetime.datetime(2014, 9, 1, 11, 30)
        >>> # Minute 70 overflows to next hour:
        >>> set_minutes(datetime(2014, 9, 1, 11, 1), 70)
        datetime.datetime(2014, 9, 1, 12, 10)
    """
    # Handle NaN minutes
    if isinstance(minutes, float) and math.isnan(minutes):
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
    
    # Reset to start of hour, then add minutes (handles overflow like JavaScript)
    start_of_hour = dt.replace(minute=0, second=0, microsecond=0)
    return start_of_hour + timedelta(minutes=int(minutes))