from datetime import datetime, timedelta


def add_hours(date: datetime, amount : int) -> datetime:
    """
    Add the specified number of hours to the given date.
    """

    if not isinstance(date, datetime):
        raise TypeError("date must be of type datetime")
    if not isinstance(amount, int):
        raise TypeError("weeks must be of type int")
    
    return date + timedelta(hours=amount)
    