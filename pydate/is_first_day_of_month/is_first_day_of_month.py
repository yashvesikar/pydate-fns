from datetime import datetime


def is_first_day_of_month(date: datetime) -> bool:
    """
    Is the given date the first day of a month?

    :param datetime date: datetime object
    :return bool: True if the given date is the first day of a month, False otherwise
    """
    if not isinstance(date, datetime):
        raise TypeError("date must be an instance of datetime")

    return date.day == 1
