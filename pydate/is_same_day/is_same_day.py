from datetime import datetime

from ..to_naive import to_naive


def is_same_day(date: datetime, to_compare: datetime) -> bool:
    """
    Is the given date the same day as the to_compare date?
    converts both dates to naive utc datetime objects before comparing

    :param datetime date: datetime object
    :param datetime to_compare: datetime object
    :return bool: True if the given date is the same day (and year and month) as the to_compare date, False otherwise
    """

    if not isinstance(date, datetime):
        raise TypeError("date must be an instance of datetime")

    if not isinstance(to_compare, datetime):
        raise TypeError("to_compare must be an instance of datetime")

    left = to_naive(date)
    right = to_naive(to_compare)

    return left.year == right.year and left.month == right.month and left.day == right.day
