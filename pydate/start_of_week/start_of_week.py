from datetime import datetime, timedelta
from typing import Union

from ..to_date import to_date


def start_of_week(date: Union[datetime, float, int], week_starts_on: int = 0) -> datetime:
    """
    Return the start of a week for the given date.
    The result will be in the local timezone.

    :param date: The original date
    :param week_starts_on: The index of the first day of the week (0 - Sunday)
    :return: The start of the week
    """
    try:
        dt = to_date(date)
        current_day = dt.weekday()  # Monday is 0, Sunday is 6
        
        # Convert to Sunday = 0 format if needed
        if current_day == 6:
            current_day = 0
        else:
            current_day += 1

        # Calculate days to subtract to reach start of week
        days_to_subtract = (current_day - week_starts_on + 7) % 7
        
        # Get start of week by subtracting days and clearing time
        result = dt - timedelta(days=days_to_subtract)
        return datetime(
            year=result.year,
            month=result.month,
            day=result.day,
            tzinfo=result.tzinfo
        )
    except (TypeError, ValueError):
        return datetime(year=1, month=1, day=1)