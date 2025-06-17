
import math
from datetime import datetime
from typing import Union

from ..to_date.to_date import to_date


def get_quarter(date: Union[datetime, int, float]) -> int:
    """
    Get the year quarter of the given date.

    :param date: The given date
    :return int: The quarter (1, 2, 3, or 4)
    
    Examples:
        >>> from datetime import datetime
        >>> # Which quarter is 2 July 2014?
        >>> result = get_quarter(datetime(2014, 7, 2))
        >>> result
        3
        
        >>> # January is in Q1
        >>> result = get_quarter(datetime(2014, 1, 15))
        >>> result
        1
        
        >>> # December is in Q4
        >>> result = get_quarter(datetime(2014, 12, 25))
        >>> result
        4
        
        >>> # Accepts timestamps
        >>> result = get_quarter(datetime(2014, 7, 2).timestamp())
        >>> result
        3
    """
    _date = to_date(date)
    # Calculate quarter: January=1, February=2, etc. -> Q1=1-3, Q2=4-6, Q3=7-9, Q4=10-12
    # Using math.trunc to match JavaScript Math.trunc behavior
    return math.trunc((_date.month - 1) / 3) + 1
