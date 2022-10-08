from datetime import datetime, timedelta
from typing import Literal, Optional

from ..add_months import add_months


def add(
    date: datetime,
    duration: dict[
        Literal["years", "months", "weeks", "days", "hours", "minutes", "seconds"],
        Optional[int],
    ],
) -> datetime:
    """
    adds the given duration to a date
    :param date: datetime object
    :param duration: dict with keys "years", "months", "weeks", "days", "hours", "minutes", "seconds"
    :return: datetime object
    """
    if not isinstance(date, datetime):
        raise TypeError("date must be of type datetime")
    if not isinstance(duration, dict):
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
