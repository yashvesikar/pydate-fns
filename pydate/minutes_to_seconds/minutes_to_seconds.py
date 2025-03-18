from math import trunc

SECONDS_IN_MINUTE = 60


def minutes_to_seconds(minutes: float) -> int:
    """
    Convert minutes to seconds.

    :param minutes: The number of minutes to be converted
    :return: The number of minutes converted in seconds

    Example:
        >>> minutes_to_seconds(2)
        120
    """
    return trunc(minutes * SECONDS_IN_MINUTE)