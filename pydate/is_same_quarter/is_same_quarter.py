
from datetime import datetime
from typing import Union
import math
from ..to_date import to_date
from ..start_of_quarter import start_of_quarter


def is_same_quarter(date_left: Union[datetime, int, float], date_right: Union[datetime, int, float]) -> bool:
    """
    Are the given dates in the same quarter (and year)?
    
    Are the given dates in the same quarter (and year)?
    
    Args:
        date_left: The first date to check
        date_right: The second date to check
        
    Returns:
        The dates are in the same quarter (and year)
        
    Examples:
        >>> from datetime import datetime
        >>> # Are 1 January 2014 and 8 March 2014 in the same quarter?
        >>> is_same_quarter(datetime(2014, 1, 1), datetime(2014, 3, 8))
        True
        >>> # Are 1 January 2014 and 1 January 2015 in the same quarter?
        >>> is_same_quarter(datetime(2014, 1, 1), datetime(2015, 1, 1))
        False
    """
    try:
        dt_left = to_date(date_left)
        dt_right = to_date(date_right)
        
        # Return False if either date is invalid
        if math.isnan(dt_left.timestamp()) or math.isnan(dt_right.timestamp()):
            return False
            
        # Compare the start of quarter for both dates
        return start_of_quarter(dt_left) == start_of_quarter(dt_right)
        
    except (ValueError, OSError, OverflowError):
        # Handle invalid dates
        return False
