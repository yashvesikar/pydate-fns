from datetime import datetime
from typing import Union
from ..to_date import to_date

class InvalidDate(datetime):
    """A datetime subclass that represents an invalid date."""
    def __getattribute__(self, name):
        raise ValueError("Invalid Date")

def start_of_year(date: Union[datetime, float, int]) -> datetime:
    """Return the start of a year for the given date.

    The result will be in the local timezone.

    Args:
        date: The original date

    Returns:
        The start of a year.
        Returns Invalid Date if the given date is invalid.

    Example:
        >>> from datetime import datetime
        >>> date = datetime(2014, 9, 2, 11, 55, 0)
        >>> start_of_year(date)
        datetime(2014, 1, 1, 0, 0)
    """
    try:
        date = to_date(date)
        return datetime(
            date.year,
            1,  # month
            1,  # day
            0,  # hour
            0,  # minute
            0,  # second
            0   # microsecond
        )
    except (TypeError, ValueError):
        # Return an invalid date that will raise ValueError when accessed
        return InvalidDate.fromtimestamp(0)