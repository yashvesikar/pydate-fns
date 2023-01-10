from datetime import datetime

def is_date(date: datetime) -> bool:
    """
    Returns true if the given value is an instance of datetime.
    
    :param datetime date: _description_
    :return bool: _description_
    """
    return isinstance(date, datetime)
