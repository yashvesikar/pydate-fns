
from datetime import datetime
from typing import Union
import math
from ..to_date import to_date
from ..difference_in_calendar_days import difference_in_calendar_days
from ..add_days import add_days
from ..is_same_day import is_same_day
from ..is_weekend import is_weekend


def difference_in_business_days(later_date: Union[datetime, int, float], earlier_date: Union[datetime, int, float]) -> int:
    """
    Get the number of business days between the given dates.
    
    Get the number of business day periods between the given dates.
    Business days being days that aren't in the weekend.
    Like `difference_in_calendar_days`, the function removes the times from
    the dates before calculating the difference.
    
    Args:
        later_date: The later date
        earlier_date: The earlier date
        
    Returns:
        The number of business days
        
    Examples:
        >>> from datetime import datetime
        >>> # How many business days are between 10 January 2014 and 20 July 2014?
        >>> difference_in_business_days(datetime(2014, 7, 20), datetime(2014, 1, 10))
        135
        >>> # How many business days are between 1 November 2021 and 1 December 2021?
        >>> difference_in_business_days(datetime(2021, 11, 1), datetime(2021, 12, 1))
        -22
    """
    later_dt = to_date(later_date)
    earlier_dt = to_date(earlier_date)
    
    # Return NaN if either date is invalid
    if math.isnan(later_dt.timestamp()) or math.isnan(earlier_dt.timestamp()):
        return float('nan')
    
    diff = difference_in_calendar_days(later_dt, earlier_dt)
    sign = -1 if diff < 0 else 1
    weeks = int(diff / 7)
    
    result = weeks * 5
    moving_date = add_days(earlier_dt, weeks * 7)
    
    # The loop below will run at most 6 times to account for the remaining days that don't make up a full week
    while not is_same_day(later_dt, moving_date):
        # Sign is used to account for both negative and positive differences
        result += 0 if is_weekend(moving_date) else sign
        moving_date = add_days(moving_date, sign)
    
    # Prevent negative zero
    return 0 if result == 0 else result
