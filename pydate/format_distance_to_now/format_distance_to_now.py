
from datetime import datetime
from typing import Union, Optional, Dict
from ..format_distance import format_distance


def format_distance_to_now(
    date: Union[datetime, int, float],
    options: Optional[Dict[str, bool]] = None
) -> str:
    """
    Return the distance between the given date and now in words.
    
    This is a convenience wrapper around format_distance that always uses
    the current date/time as the base date.
    
    Args:
        date: The date to compare with now
        options: An object with options
            - includeSeconds: Distances less than a minute are more detailed
            - addSuffix: Add "X ago"/"in X" suffix
        
    Returns:
        The distance in words
        
    Raises:
        ValueError: If date is invalid
        
    Examples:
        >>> from datetime import datetime, timedelta
        >>> # Assuming now is 2015-01-01 00:00:00
        >>> past_date = datetime.now() - timedelta(days=3)
        >>> format_distance_to_now(past_date)
        '3 days'
        >>> format_distance_to_now(past_date, {'addSuffix': True})
        '3 days ago'
        >>> future_date = datetime.now() + timedelta(hours=2)
        >>> format_distance_to_now(future_date, {'addSuffix': True})
        'in about 2 hours'
    """
    return format_distance(date, datetime.now(), options)
