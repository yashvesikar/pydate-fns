from datetime import datetime, timezone
from typing import Union

from ..start_of_week import start_of_week
from ..to_date import to_date


def difference_in_calendar_weeks(
    later_date: Union[datetime, float, int],
    earlier_date: Union[datetime, float, int],
    week_starts_on: int = 0
) -> float:
    """
    Get the number of calendar weeks between the given dates.

    :param later_date: The later date
    :param earlier_date: The earlier date
    :param week_starts_on: The index of the first day of the week (0 - Sunday)
    :return: The number of calendar weeks between the dates. Returns NaN if either date is invalid.

    Example:
        >>> # How many calendar weeks are between 5 July 2014 and 20 July 2014?
        >>> result = difference_in_calendar_weeks(
        >>>     datetime(2014, 7, 20),  # Jul 20 2014
        >>>     datetime(2014, 7, 5)    # Jul 5 2014
        >>> )
        >>> # => 3

        >>> # If the week starts on Monday,
        >>> # how many calendar weeks are between 5 July 2014 and 20 July 2014?
        >>> result = difference_in_calendar_weeks(
        >>>     datetime(2014, 7, 20),  # Jul 20 2014
        >>>     datetime(2014, 7, 5),   # Jul 5 2014
        >>>     week_starts_on=1
        >>> )
        >>> # => 2
    """
    try:
        later = to_date(later_date)
        earlier = to_date(earlier_date)
    except (TypeError, ValueError):
        return float('nan')

    # Convert to UTC to avoid timezone offset issues
    later_start = start_of_week(later, week_starts_on).astimezone(timezone.utc)
    earlier_start = start_of_week(earlier, week_starts_on).astimezone(timezone.utc)

    # Calculate difference in milliseconds
    diff_ms = (later_start.timestamp() - earlier_start.timestamp()) * 1000

    # Round to handle DST transitions
    return round(diff_ms / (7 * 24 * 60 * 60 * 1000))  # milliseconds in a week