from datetime import datetime


def is_saturday(date: datetime) -> bool:
    """
    Is the given date a Saturday?

    :param datetime date: datetime object
    :return bool: True if the given date is a saturday, False otherwise
    """
    if not isinstance(date, datetime):
        raise TypeError("date must be an instance of datetime")

    return date.weekday() == 5
