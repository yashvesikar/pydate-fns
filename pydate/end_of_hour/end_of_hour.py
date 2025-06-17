
from datetime import datetime
from typing import Union

from ..to_date.to_date import to_date


def end_of_hour(date: Union[datetime, int, float]) -> datetime:
    """
    Return the end of an hour for the given date.
    
    The result will be in the local timezone with time set to XX:59:59.999999.

    :param date: The original date
    :return datetime: The end of an hour
    
    Examples:
        >>> from datetime import datetime
        >>> result = end_of_hour(datetime(2014, 9, 2, 11, 55, 0))
        >>> result == datetime(2014, 9, 2, 11, 59, 59, 999999)
        True
        
        >>> # Accepts timestamps
        >>> result = end_of_hour(datetime(2014, 9, 2, 11, 55, 0).timestamp())
        >>> result == datetime(2014, 9, 2, 11, 59, 59, 999999)
        True
    """
    _date = to_date(date)
    # Set to end of hour: XX:59:59.999999 (max microseconds in Python)
    return _date.replace(minute=59, second=59, microsecond=999999)
