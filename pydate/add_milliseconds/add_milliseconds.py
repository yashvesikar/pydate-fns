from datetime import datetime, timedelta


def add_milliseconds(date: datetime, amount: int) -> datetime:
    """
    Add the specified number of milliseconds to the given date.
    :return: datetime object
    """
    return date + timedelta(milliseconds=amount)
