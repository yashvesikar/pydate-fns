
import math
from datetime import datetime
from typing import List, Union

from ..to_date.to_date import to_date


def min(dates: List[Union[datetime, int, float]]) -> datetime:
    """
    Returns the earliest of the given dates.

    :param dates: The dates to compare
    :return datetime: The earliest of the dates
    
    Examples:
        >>> from datetime import datetime
        >>> result = min([
        ...     datetime(1989, 7, 10),
        ...     datetime(1987, 2, 11),
        ...     datetime(1995, 7, 2),
        ...     datetime(1990, 1, 1)
        ... ])
        >>> result == datetime(1987, 2, 11)
        True
        
        >>> # Accepts timestamps
        >>> result = min([
        ...     datetime(1989, 7, 10).timestamp(),
        ...     datetime(1987, 2, 11).timestamp()
        ... ])
        >>> result == datetime(1987, 2, 11)
        True
    """
    if not dates:
        raise ValueError("dates array must not be empty")
    
    result = None
    
    for date_input in dates:
        try:
            date_obj = to_date(date_input)
            
            # Handle NaN case - if any date is invalid (NaN), skip it
            timestamp = date_obj.timestamp()
            if math.isnan(timestamp):
                continue
                
            if result is None or date_obj < result:
                result = date_obj
        except (TypeError, ValueError, OSError):
            # Skip invalid dates
            continue
    
    if result is None:
        raise ValueError("All dates are invalid")
    
    return result
