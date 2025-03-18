from datetime import datetime
from typing import Union

from ..difference_in_milliseconds import difference_in_milliseconds


def difference_in_seconds(later_date: Union[datetime, float, int], earlier_date: Union[datetime, float, int]) -> float:
    """
    Get the number of seconds between the given dates.

    :param later_date: The later date
    :param earlier_date: The earlier date
    :return: The number of seconds

    Example:
        >>> # How many seconds are between
        >>> # 2 July 2014 12:30:07.999 and 2 July 2014 12:30:20.000?
        >>> result = difference_in_seconds(
        >>>     datetime(2014, 7, 2, 12, 30, 20, 0),
        >>>     datetime(2014, 7, 2, 12, 30, 7, 999000)
        >>> )
        >>> # => 12
    """
    try:
        # Get milliseconds difference and convert to seconds, rounding to match JS behavior
        return round(difference_in_milliseconds(later_date, earlier_date) / 1000)
    except (TypeError, ValueError):
        return float('nan')