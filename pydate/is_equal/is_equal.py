from datetime import datetime


def is_equal(date: datetime, to_compare: datetime) -> bool:
    """
    Returns True if the given dates are equal.

    :param datetime date: datetime object
    :param datetime to_compare: datetime object to compare
    :return bool: True if the given dates are equal, False otherwise
    """
    if not isinstance(date, datetime):
        raise TypeError("date must be an instance of datetime")
    if not isinstance(to_compare, datetime):
        raise TypeError("to_compare must be an instance of datetime")

    return date == to_compare
