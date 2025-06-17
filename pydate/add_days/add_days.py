from datetime import datetime, timedelta


def add_days(date: datetime, amount: int) -> datetime:
    """
    Add the specified number of days to the given date.
    :param date: The date to add days to.
    :param amount: The number of days to add (can be negative).
    :return: The new date with the days added.
    """
    if not isinstance(date, datetime):
        raise TypeError("date must be of type datetime")
    if not isinstance(amount, int):
        raise TypeError("days must be of type int")

    return date + timedelta(days=amount)
