from datetime import datetime, timezone
from typing import Union

from ..start_of_day import start_of_day
from ..to_date import to_date


def difference_in_calendar_days(later_date: Union[datetime, float, int], earlier_date: Union[datetime, float, int]) -> float:
    """
    Get the number of calendar days between the given dates.

    This means that the times are removed from the dates and then the difference in days is calculated.

    :param later_date: The later date
    :param earlier_date: The earlier date
    :return: The number of calendar days between the dates. Returns NaN if either date is invalid.

    Example:
        >>> # How many calendar days are between
        >>> # 2 July 2011 23:00:00 and 2 July 2012 00:00:00?
        >>> result = difference_in_calendar_days(
        >>>     datetime(2012, 7, 2, 0, 0),
        >>>     datetime(2011, 7, 2, 23, 0)
        >>> )
        >>> # => 366

        >>> # How many calendar days are between
        >>> # 2 July 2011 23:59:00 and 3 July 2011 00:01:00?
        >>> result = difference_in_calendar_days(
        >>>     datetime(2011, 7, 3, 0, 1),
        >>>     datetime(2011, 7, 2, 23, 59)
        >>> )
        >>> # => 1
    """
    try:
        later = to_date(later_date)
        earlier = to_date(earlier_date)
    except (TypeError, ValueError):
        return float('nan')

    # Convert to UTC to avoid timezone offset issues
    later_start = start_of_day(later).astimezone(timezone.utc)
    earlier_start = start_of_day(earlier).astimezone(timezone.utc)

    # Calculate difference in milliseconds
    diff_ms = (later_start.timestamp() - earlier_start.timestamp()) * 1000

    # Round to handle DST transitions
    return round(diff_ms / (24 * 60 * 60 * 1000))  # milliseconds in a day