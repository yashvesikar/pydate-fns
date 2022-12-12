from datetime import datetime, timedelta


def add_days(date: datetime, amount: int) -> datetime:
    """
    Add months to a date.
    :param date: The date to add days to.
    :param amount: The number of days to add.
    :return:
    """
    if not isinstance(date, datetime):
        raise TypeError("date must be of type datetime")
    if not isinstance(amount, int):
        raise TypeError("days must be of type int")
    if amount < 0:
        raise ValueError("days must be greater than 0")

    return date + timedelta(days=amount)
