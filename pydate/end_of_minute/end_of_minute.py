from datetime import datetime
from typing import Union
from ..to_date import to_date

class InvalidDate(datetime):
    """A datetime subclass that represents an invalid date."""
    def __getattribute__(self, name):
        raise ValueError("Invalid Date")

def end_of_minute(date: Union[datetime, float, int]) -> datetime:
    """Return the end of a minute for the given date.

    The result will be in the local timezone.

    Args:
        date: The original date

    Returns:
        The end of a minute.
        Returns Invalid Date if the given date is invalid.

    Example:
        >>> from datetime import datetime
        >>> date = datetime(2014, 12, 1, 22, 15)
        >>> end_of_minute(date)
        datetime(2014, 12, 1, 22, 15, 59, 999999)
    """
    try:
        date = to_date(date)
        return datetime(
            date.year,
            date.month,
            date.day,
            date.hour,
            date.minute,
            59,  # second
            999999  # microsecond (Python uses microseconds instead of milliseconds)
        )
    except (TypeError, ValueError):
        # Return an invalid date that will raise ValueError when accessed
        return InvalidDate.fromtimestamp(0)