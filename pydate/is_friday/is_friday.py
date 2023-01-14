from datetime import datetime


def is_friday(date: datetime) -> bool:
    """
    Is the given date a Friday?

    :param datetime date: datetime object
    :return bool: True if the given date is a Friday, False otherwise
    """
    if not isinstance(date, datetime):
        raise TypeError("date must be an instance of datetime")

    return date.weekday() == 4
