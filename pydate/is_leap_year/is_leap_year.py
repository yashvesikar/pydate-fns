from datetime import datetime


def is_leap_year(date: datetime) -> bool:
    """
    Is the given date in the leap year?

    :param datetime date: datetime object
    :return bool: True if the date is in the leap year, False otherwise
    """
    if not isinstance(date, datetime):
        raise TypeError("date must be a datetime object")

    return date.year % 4 == 0 and (date.year % 100 != 0 or date.year % 400 == 0)
