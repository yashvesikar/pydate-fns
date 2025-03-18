from datetime import datetime
from typing import Union

from ..to_date import to_date


def get_unix_time(date: Union[datetime, float, int]) -> int:
    """
    Get the seconds timestamp of the given date.

    :param date: The given date
    :return: The Unix timestamp (seconds since epoch)

    Example:
        >>> # Get the timestamp of 29 February 2012 11:45:05 UTC:
        >>> result = get_unix_time(datetime(2012, 2, 29, 11, 45, 5))
        >>> # => 1330515905
    """
    try:
        dt = to_date(date)
        return int(dt.timestamp())  # Convert to integer seconds
    except (TypeError, ValueError):
        return float('nan')