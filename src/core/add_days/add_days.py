from datetime import datetime, timedelta


def add_days(date: datetime, days: int) -> datetime:
    """
    Add months to a date.
    :param date: The date to add months to.
    :param days: The number of months to add.
    :return:
    """
    if type(date) != datetime:
        raise TypeError("date must be of type datetime")
    if type(days) != int:
        raise TypeError("months must be of type int")
    if days < 0:
        raise ValueError("months must be greater than 0")

    return date + timedelta(days=days)
