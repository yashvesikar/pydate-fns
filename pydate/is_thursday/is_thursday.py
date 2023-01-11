from datetime import datetime


def is_thursday(date: datetime) -> bool:
    """
    Is the given date a thursday?

    :param datetime date: datetime object
    :return bool: True if the given date is a thursday, False otherwise
    """
    if not isinstance(date, datetime):
        raise TypeError("date must be an instance of datetime")

    return date.weekday() == 3
