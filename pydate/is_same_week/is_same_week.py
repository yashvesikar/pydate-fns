
from datetime import datetime
from typing import Union, Optional
import math
from ..to_date import to_date
from ..start_of_week import start_of_week


def is_same_week(date_left: Union[datetime, int, float], date_right: Union[datetime, int, float], week_starts_on: Optional[int] = None) -> bool:
    """
    Are the given dates in the same week (and month and year)?
    
    Are the given dates in the same week (and month and year)?
    
    Args:
        date_left: The first date to check
        date_right: The second date to check
        week_starts_on: Which day of the week is the first day of the week (0=Sunday, 1=Monday, etc.)
        
    Returns:
        The dates are in the same week (and month and year)
        
    Examples:
        >>> from datetime import datetime
        >>> # Are 31 August 2014 and 4 September 2014 in the same week?
        >>> is_same_week(datetime(2014, 8, 31), datetime(2014, 9, 4))
        True
        >>> # If week starts with Monday, are 31 August 2014 and 4 September 2014 in the same week?
        >>> is_same_week(datetime(2014, 8, 31), datetime(2014, 9, 4), week_starts_on=1)
        False
    """
    try:
        dt_left = to_date(date_left)
        dt_right = to_date(date_right)
        
        # Return False if either date is invalid
        if math.isnan(dt_left.timestamp()) or math.isnan(dt_right.timestamp()):
            return False
        
        # Handle None case for week_starts_on
        if week_starts_on is None:
            week_starts_on = 0
            
        # Compare the start of week for both dates
        return start_of_week(dt_left, week_starts_on) == start_of_week(dt_right, week_starts_on)
        
    except (ValueError, OSError, OverflowError):
        # Handle invalid dates
        return False
