
from datetime import datetime
from typing import Union
import math
from ..to_date import to_date
from ..difference_in_months import difference_in_months


def difference_in_quarters(later_date: Union[datetime, int, float], earlier_date: Union[datetime, int, float]) -> Union[int, float]:
    """
    Get the number of quarters between the given dates.
    
    Get the number of full quarters between the given dates.
    
    Args:
        later_date: The later date
        earlier_date: The earlier date
        
    Returns:
        The number of full quarters
        
    Examples:
        >>> from datetime import datetime
        >>> # How many full quarters are between 31 December 2013 and 2 July 2014?
        >>> difference_in_quarters(datetime(2014, 7, 2), datetime(2013, 12, 31))
        2
    """
    later_dt = to_date(later_date)
    earlier_dt = to_date(earlier_date)
    
    # Return NaN if either date is invalid
    try:
        if math.isnan(later_dt.timestamp()) or math.isnan(earlier_dt.timestamp()):
            return float('nan')
    except (ValueError, OSError):
        return float('nan')
    
    # Get the sign of the difference
    if later_dt < earlier_dt:
        sign = -1
        later_dt, earlier_dt = earlier_dt, later_dt
    else:
        sign = 1
    
    # Calculate the difference in calendar months
    months_diff = (later_dt.year - earlier_dt.year) * 12 + (later_dt.month - earlier_dt.month)
    
    # Check if we have a full number of months by comparing times
    # If the later date's time is earlier in the day than the earlier date's time,
    # we don't have a full last month
    if months_diff > 0:
        # Create a date that is exactly months_diff months after the earlier date
        year_add = months_diff // 12
        month_add = months_diff % 12
        
        new_year = earlier_dt.year + year_add
        new_month = earlier_dt.month + month_add
        
        if new_month > 12:
            new_year += 1
            new_month -= 12
            
        try:
            # Try to create the date with the same day
            test_date = datetime(new_year, new_month, earlier_dt.day, 
                               earlier_dt.hour, earlier_dt.minute, 
                               earlier_dt.second, earlier_dt.microsecond)
        except ValueError:
            # Day doesn't exist in target month (e.g., Jan 31 -> Feb 31)
            # Use the last day of the month
            if new_month == 12:
                next_month_first = datetime(new_year + 1, 1, 1)
            else:
                next_month_first = datetime(new_year, new_month + 1, 1)
            
            from datetime import timedelta
            last_day = next_month_first - timedelta(days=1)
            test_date = datetime(last_day.year, last_day.month, last_day.day,
                               earlier_dt.hour, earlier_dt.minute,
                               earlier_dt.second, earlier_dt.microsecond)
        
        # If test_date is after later_dt, we don't have a full months_diff months
        if test_date > later_dt:
            months_diff -= 1
    
    # Calculate quarters from months
    quarters = months_diff // 3
    
    # Apply sign and prevent negative zero
    result = sign * quarters
    return 0 if result == 0 else result
