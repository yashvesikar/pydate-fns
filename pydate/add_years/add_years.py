from datetime import datetime, timedelta


def add_years(date: datetime, amount: int) -> datetime:
    """
    Add years to a date.
    :param date: The date to add weeks to.
    :param years: The number of weeks to add.
    :return:
    """
    if not isinstance(date, datetime):
        raise TypeError("date must be of type datetime")
    if not isinstance(amount, int):
        raise TypeError("years must be of type int")
    if amount < 0:
        raise ValueError("years must be greater than 0")

    return date.replace(year=date.year + amount)
