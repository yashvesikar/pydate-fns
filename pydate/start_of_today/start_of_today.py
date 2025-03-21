from datetime import datetime
from ..start_of_day.start_of_day import start_of_day

def start_of_today() -> datetime:
    """Return the start of today.

    Returns:
        The start of today.

    Example:
        >>> from datetime import datetime
        >>> # If today is 6 October 2014:
        >>> start_of_today()
        datetime(2014, 10, 6, 0, 0)
    """
    return start_of_day(datetime.now())