from datetime import datetime, timedelta

from ..add_days import add_days


def sub_days(date: datetime, amount: int) -> datetime:
    """
    Subtract the specified number of days from the given date.
    :param date: The date to subtract days from.
    :param amount: The number of days to subtract.
    :return: The new date with the days subtracted.
    """
    if not isinstance(date, datetime):
        raise TypeError("date must be of type datetime")
    if not isinstance(amount, int):
        raise TypeError("days must be of type int")

    return add_days(date, -amount)
