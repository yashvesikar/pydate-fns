
from datetime import datetime
from typing import Union

from ..to_date.to_date import to_date


def get_day_of_year(date: Union[datetime, int, float]) -> int:
    """
    Get the day of the year of the given date.

    :param date: The given date
    :return int: The day of year (1-366)
    
    Examples:
        >>> from datetime import datetime
        >>> # Which day of the year is 2 July 2014?
        >>> result = get_day_of_year(datetime(2014, 7, 2))
        >>> result
        183
        
        >>> # January 1st is day 1
        >>> result = get_day_of_year(datetime(2014, 1, 1))
        >>> result
        1
        
        >>> # Accepts timestamps
        >>> result = get_day_of_year(datetime(2014, 7, 2).timestamp())
        >>> result
        183
    """
    _date = to_date(date)
    # Python's timetuple().tm_yday gives us the day of year directly
    return _date.timetuple().tm_yday
