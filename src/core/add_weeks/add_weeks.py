from datetime import datetime, timedelta


def add_weeks(date: datetime, weeks: int) -> datetime:
    """
    Add weeks to a date.
    :param date: The date to add weeks to.
    :param weeks: The number of weeks to add.
    :return:
    """
    if type(date) != datetime:
        raise TypeError("date must be of type datetime")
    if type(weeks) != int:
        raise TypeError("weeks must be of type int")
    if weeks < 0:
        raise ValueError("weeks must be greater than 0")

    return date + timedelta(weeks=weeks)
