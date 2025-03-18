from math import trunc

SECONDS_IN_MINUTE = 60


def seconds_to_minutes(seconds: float) -> int:
    """
    Convert seconds to minutes.

    :param seconds: The number of seconds to be converted
    :return: The number of seconds converted in minutes

    Example:
        >>> seconds_to_minutes(120)
        2
    """
    return trunc(seconds / SECONDS_IN_MINUTE)