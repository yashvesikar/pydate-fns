from datetime import datetime
from typing import Union

from ..to_date import to_date


def difference_in_milliseconds(later_date: Union[datetime, float, int], earlier_date: Union[datetime, float, int]) -> float:
    """
    Get the number of milliseconds between the given dates.

    :param later_date: The later date
    :param earlier_date: The earlier date
    :return: The number of milliseconds

    Example:
        >>> # How many milliseconds are between
        >>> # 2 July 2014 12:30:20.600 and 2 July 2014 12:30:21.700?
        >>> result = difference_in_milliseconds(
        >>>     datetime(2014, 7, 2, 12, 30, 21, 700000),  # Note: microseconds in Python
        >>>     datetime(2014, 7, 2, 12, 30, 20, 600000)
        >>> )
        >>> # => 1100.0
    """
    try:
        later = to_date(later_date)
        earlier = to_date(earlier_date)
        # Convert seconds to milliseconds and round to match JavaScript behavior
        return round((later.timestamp() - earlier.timestamp()) * 1000)
    except (TypeError, ValueError):
        return float('nan')