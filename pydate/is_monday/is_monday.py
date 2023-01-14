from datetime import datetime


def is_monday(date: datetime) -> bool:
    """
    Is the given date a Monday?

    :param datetime date: datetime object
    :return bool: True if the given date is a Monday, False otherwise
    """
    if not isinstance(date, datetime):
        raise TypeError("date must be an instance of datetime")

    return date.weekday() == 0
