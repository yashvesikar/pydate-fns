from math import trunc

SECONDS_IN_HOUR = 3600


def seconds_to_hours(seconds: float) -> int:
    """
    Convert seconds to hours.

    :param seconds: The number of seconds to be converted
    :return: The number of seconds converted in hours

    Example:
        >>> seconds_to_hours(7200)
        2
    """
    return trunc(seconds / SECONDS_IN_HOUR)