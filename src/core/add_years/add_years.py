from datetime import datetime, timedelta


def add_years(date: datetime, years: int) -> datetime:
    """
    Add years to a date.
    :param date: The date to add weeks to.
    :param years: The number of weeks to add.
    :return:
    """
    if type(date) != datetime:
        raise TypeError("date must be of type datetime")
    if type(years) != int:
        raise TypeError("years must be of type int")
    if years < 0:
        raise ValueError("years must be greater than 0")

    return date.replace(year=date.year + years)
