from datetime import datetime, timedelta
from typing import Literal, Optional, TypedDict


# from ..sub

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

    date_with_months = add_months(
        date, (duration.get("years", 0) or 0) * 12 + (duration.get("months", 0) or 0)
    )

    duration.pop("years", None)
    duration.pop("months", None)

    return date_with_months + timedelta(**duration)
