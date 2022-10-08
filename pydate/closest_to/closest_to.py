from datetime import datetime


def closest_to(date: datetime, dates_list: list[datetime]):
    """
    Find the closest date in a list of dates.
    :param date: The date to find the closest date to.
    :param dates_list: The list of dates to find the closest date to.
    :return: The closest date.
    """
    if not isinstance(date, datetime):
        raise TypeError("date must be of type datetime")
    if not isinstance(dates_list, list):
        raise TypeError("dates_list must be of type list[datetime]")
    if len(dates_list) == 0:
        raise ValueError("dates_list must not be empty")

    closest_date = dates_list[0]
    for d in dates_list:
        if abs(d - date) < abs(closest_date - date):
            closest_date = d

    return closest_date
