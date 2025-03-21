from datetime import datetime
import math
from typing import Union, Optional
from ..difference_in_milliseconds import difference_in_milliseconds

MILLISECONDS_IN_MINUTE = 60000

def get_rounding_method(method: Optional[str] = None):
    """Helper function to get the rounding method"""
    if method == "ceil":
        return lambda x: int(-(-x // 1))  # Ceiling for both positive and negative
    elif method == "floor":
        return lambda x: int(x // 1)  # Floor for both positive and negative
    elif method == "round":
        return round
    else:  # "trunc" is default
        return int  # Truncates towards zero

def difference_in_minutes(
    date_left: Union[datetime, float, int],
    date_right: Union[datetime, float, int],
    *,
    rounding_method: Optional[str] = None
) -> Union[int, float]:
    """Get the number of minutes between the given dates.

    Args:
        date_left: The later date
        date_right: The earlier date
        rounding_method: Optional rounding method ('ceil', 'floor', 'round', 'trunc'). Default is 'trunc'.

    Returns:
        The number of minutes between the given dates.
        Returns NaN if either date is invalid.

    Example:
        >>> from datetime import datetime
        >>> date1 = datetime(2014, 7, 2, 12, 20, 0)
        >>> date2 = datetime(2014, 7, 2, 12, 7, 59)
        >>> difference_in_minutes(date1, date2)
        12
    """
    diff = difference_in_milliseconds(date_left, date_right) / MILLISECONDS_IN_MINUTE
    
    # Handle NaN cases
    if isinstance(diff, float) and math.isnan(diff):
        return float('nan')
        
    return get_rounding_method(rounding_method)(diff)