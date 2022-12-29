from datetime import datetime, timedelta

from ..add_days import add_days


def sub_days(date: datetime, amount: int) -> datetime:
    """
    Sub months to a date.
    :param date: The date to subtract days from.
    :param amount: The number of days to subtract.
    :return:
    """
    if not isinstance(date, datetime):
        raise TypeError("date must be of type datetime")
    if not isinstance(amount, int):
        raise TypeError("days must be of type int")
    if amount < 0:
        raise ValueError("days must be greater than 0")

    return add_days(date, -amount)
