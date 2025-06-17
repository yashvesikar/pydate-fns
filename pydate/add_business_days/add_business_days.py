
from datetime import datetime, timedelta
from typing import Union
import math
from ..to_date import to_date
from ..is_weekend import is_weekend
from ..is_saturday import is_saturday
from ..is_sunday import is_sunday


def add_business_days(date: Union[datetime, int, float], amount: int) -> datetime:
    """
    Add the specified number of business days (Mon - Fri) to the given date.
    
    Add the specified number of business days to the given date, ignoring weekends.
    Positive amounts will add business days, negative amounts will subtract them.
    
    Args:
        date: The date to be changed
        amount: The amount of business days to be added (can be negative)
        
    Returns:
        The new date with the business days added
        
    Raises:
        ValueError: If amount is NaN
        
    Examples:
        >>> from datetime import datetime
        >>> # Add 10 business days to Monday September 1, 2014:
        >>> add_business_days(datetime(2014, 9, 1), 10)
        datetime.datetime(2014, 9, 15, 0, 0)
        >>> # Subtract 10 business days from Monday September 15, 2014:
        >>> add_business_days(datetime(2014, 9, 15), -10)
        datetime.datetime(2014, 9, 1, 0, 0)
    """
    dt = to_date(date)
    
    if isinstance(amount, float) and math.isnan(amount):
        raise ValueError("Amount cannot be NaN")
    
    # Store original hour to restore after date operations (for DST handling)
    hours = dt.hour
    
    started_on_weekend = is_weekend(dt)
    
    sign = -1 if amount < 0 else 1
    full_weeks = math.trunc(amount / 5)
    
    # Add full weeks (each full week is 7 calendar days)
    dt = dt + timedelta(days=full_weeks * 7)
    
    # Get remaining days not part of a full week
    rest_days = abs(amount) % 5
    
    # Loop over remaining days
    while rest_days > 0:
        dt = dt + timedelta(days=sign)
        if not is_weekend(dt):
            rest_days -= 1
    
    # If we started on a weekend and ended on a weekend after moving by a multiple of 5,
    # we need to adjust to land on a business day
    if started_on_weekend and is_weekend(dt) and amount != 0:
        if is_saturday(dt):
            # If reducing days and on Saturday, add 2 days to get to Monday
            # If adding days and on Saturday, subtract 1 day to get to Friday
            dt = dt + timedelta(days=2 if sign < 0 else -1)
        elif is_sunday(dt):
            # If reducing days and on Sunday, add 1 day to get to Monday
            # If adding days and on Sunday, subtract 2 days to get to Friday
            dt = dt + timedelta(days=1 if sign < 0 else -2)
    
    # Restore the original hour to handle DST changes
    dt = dt.replace(hour=hours)
    
    return dt
