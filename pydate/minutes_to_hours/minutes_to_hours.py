from math import trunc

MINUTES_IN_HOUR = 60


def minutes_to_hours(minutes: float) -> int:
    """
    Convert minutes to hours.

    :param minutes: The number of minutes to be converted
    :return: The number of minutes converted in hours

    Example:
        >>> minutes_to_hours(120)
        2
    """
    return trunc(minutes / MINUTES_IN_HOUR)