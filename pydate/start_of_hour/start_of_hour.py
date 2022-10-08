from datetime import datetime


def start_of_hour(date: datetime) -> datetime:
    """
    Return the start of the hour of the given date.
    :param date: The date to get the start of the hour of.
    :return: The start of the hour of the given date.
    """

    if not isinstance(date, datetime):
        raise TypeError("date must be of type datetime")

    return date.replace(minute=0, second=0, microsecond=0)
