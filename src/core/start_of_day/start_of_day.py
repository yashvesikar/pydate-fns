from datetime import datetime


def start_of_day(date: datetime) -> datetime:
    """
    Return the start of the day of the given date.
    :param date: The date to get the start of the day of.
    :return: The start of the day of the given date.
    """

    if not isinstance(date, datetime):
        raise TypeError("date must be of type datetime")

    return date.replace(hour=0, minute=0, second=0, microsecond=0)
