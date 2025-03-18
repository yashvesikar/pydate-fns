from datetime import datetime
from typing import Union

from ..to_date import to_date


def get_time(date: Union[datetime, float, int]) -> float:
    """
    Get the milliseconds timestamp of the given date.

    :param date: The given date
    :return: The timestamp in milliseconds

    Example:
        >>> # Get the timestamp of 29 February 2012 11:45:05.123:
        >>> result = get_time(datetime(2012, 2, 29, 11, 45, 5, 123000))
        >>> # => 1330515905123.0
    """
    try:
        dt = to_date(date)
        return dt.timestamp() * 1000  # Convert seconds to milliseconds
    except (TypeError, ValueError):
        return float('nan')