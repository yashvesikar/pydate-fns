from datetime import datetime, timedelta
from typing import Literal, Optional, TypedDict

from ..sub_months import sub_months


class Duration(TypedDict):
    years: Optional[int]
    months: Optional[int]
    weeks: Optional[int]
    days: Optional[int]
    hours: Optional[int]
    minutes: Optional[int]
    seconds: Optional[int]


def sub(date: datetime, duration: Duration) -> datetime:
    """
    subtracts the given duration from date
    :param date: datetime object
    :param duration: TypedDict
    :return: datetime object
    """

    if not isinstance(date, datetime):
        raise TypeError("date must be of type datetime")
    if not isinstance(duration, Duration):
        raise TypeError("duration must be of type dict")
    if not any(duration.values()):
        # all values are None or False-y
        return date

    date_without_months = subMonths(date, (duration.get("years", 0) or 0) * 12 + (duration.get("months", 0) or 0))

    duration.pop("years", None)
    duration.pop("months", None)

    return date_with_months + timedelta(**duration)


def _sub(date, duration):
    years = duration.get("years", 0)
    months = duration.get("months", 0)
    weeks = duration.get("weeks", 0)
    days = duration.get("days", 0)
    hours = duration.get("hours", 0)
    minutes = duration.get("minutes", 0)
    seconds = duration.get("seconds", 0)

    # Subtract years and months
    date_without_months = sub_months(date, months + years * 12)

    # Subtract weeks and days
    date_without_days = sub_days(date_without_months, days + weeks * 7)

    # Subtract hours, minutes and seconds
    minutes_to_sub = minutes + hours * 60
    seconds_to_sub = seconds + minutes_to_sub * 60
    ms_to_sub = seconds_to_sub * 1000
    final_date = construct_from(date, date_without_days.get_time() - ms_to_sub)

    return final_date
