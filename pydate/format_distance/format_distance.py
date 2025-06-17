
from datetime import datetime
from typing import Union, Optional, Dict
from ..to_date import to_date
from ..compare_asc import compare_asc
from ..difference_in_seconds import difference_in_seconds
from ..difference_in_months import difference_in_months
from ..is_valid import is_valid
import math


def format_distance(
    date: Union[datetime, int, float], 
    base_date: Union[datetime, int, float],
    options: Optional[Dict[str, bool]] = None
) -> str:
    """
    Return the distance between the given dates in words.
    
    Distance rules:
    | Distance                                            | Result              |
    |-----------------------------------------------------|---------------------|
    | 0 ... 30 secs                                      | less than a minute  |
    | 30 secs ... 1 min 30 secs                          | 1 minute            |
    | 1 min 30 secs ... 44 mins 30 secs                  | [2..44] minutes     |
    | 44 mins ... 30 secs ... 89 mins 30 secs            | about 1 hour        |
    | 89 mins 30 secs ... 23 hrs 59 mins 30 secs         | about [2..24] hours |
    | 23 hrs 59 mins 30 secs ... 41 hrs 59 mins 30 secs  | 1 day               |
    | 41 hrs 59 mins 30 secs ... 29 days 23 hrs 59 mins 30 secs | [2..30] days |
    | 29 days 23 hrs 59 mins 30 secs ... 44 days 23 hrs 59 mins 30 secs | about 1 month |
    | 44 days 23 hrs 59 mins 30 secs ... 59 days 23 hrs 59 mins 30 secs | about 2 months |
    | 59 days 23 hrs 59 mins 30 secs ... 1 yr           | [2..12] months      |
    | 1 yr ... 1 yr 3 months                             | about 1 year        |
    | 1 yr 3 months ... 1 yr 9 months                    | over 1 year         |
    | 1 yr 9 months ... 2 yrs                            | almost 2 years      |
    | N yrs ... N yrs 3 months                           | about N years       |
    | N yrs 3 months ... N yrs 9 months                  | over N years        |
    | N yrs 9 months ... N+1 yrs                         | almost N+1 years    |
    
    With includeSeconds=True:
    | Distance            | Result               |
    |---------------------|----------------------|
    | 0 ... 5 secs        | less than 5 seconds  |
    | 5 ... 10 secs       | less than 10 seconds |
    | 10 ... 20 secs      | less than 20 seconds |
    | 20 ... 40 secs      | half a minute        |
    | 40 ... 60 secs      | less than a minute   |
    | 60 ... 90 secs      | 1 minute             |
    
    Args:
        date: The date
        base_date: The date to compare with
        options: An object with options
            - includeSeconds: Distances less than a minute are more detailed
            - addSuffix: Add "X ago"/"in X" suffix
        
    Returns:
        The distance in words
        
    Raises:
        ValueError: If date is invalid
        
    Examples:
        >>> from datetime import datetime
        >>> format_distance(datetime(2015, 1, 1), datetime(2014, 7, 2))
        '6 months'
        >>> format_distance(datetime(2015, 0, 1, 0, 0, 15), datetime(2015, 0, 1, 0, 0, 0), {'includeSeconds': True})
        'less than 20 seconds'
        >>> format_distance(datetime(2015, 1, 1), datetime(2016, 1, 1), {'addSuffix': True})
        'about 1 year ago'
    """
    if options is None:
        options = {}
    
    try:
        dt_date = to_date(date)
        dt_base = to_date(base_date)
    except ValueError:
        raise ValueError("Invalid time value")
    
    if not is_valid(dt_date) or not is_valid(dt_base):
        raise ValueError("Invalid time value")
    
    comparison = compare_asc(dt_date, dt_base)
    
    # Always calculate distance from earlier to later date
    if comparison > 0:
        earlier_date = dt_base
        later_date = dt_date
    else:
        earlier_date = dt_date
        later_date = dt_base
    
    seconds = abs(difference_in_seconds(later_date, earlier_date))
    minutes = round(seconds / 60)
    
    # Distance calculation
    distance_str = ""
    
    # 0 up to 2 mins
    if minutes < 2:
        if options.get('includeSeconds', False):
            if seconds < 5:
                distance_str = "less than 5 seconds"
            elif seconds < 10:
                distance_str = "less than 10 seconds"
            elif seconds < 20:
                distance_str = "less than 20 seconds"
            elif seconds < 40:
                distance_str = "half a minute"
            elif seconds < 60:
                distance_str = "less than a minute"
            else:
                distance_str = "1 minute"
        else:
            if minutes == 0:
                distance_str = "less than a minute"
            else:
                distance_str = f"{minutes} minute" if minutes == 1 else f"{minutes} minutes"
    
    # 2 mins up to 0.75 hrs
    elif minutes < 45:
        distance_str = f"{minutes} minutes"
    
    # 0.75 hrs up to 1.5 hrs
    elif minutes < 90:
        distance_str = "about 1 hour"
    
    # 1.5 hrs up to 24 hrs
    elif minutes < 1440:  # minutes in day
        hours = round(minutes / 60)
        distance_str = f"about {hours} hour" if hours == 1 else f"about {hours} hours"
    
    # 1 day up to 1.75 days
    elif minutes < 2520:  # minutes in almost 2 days
        distance_str = "1 day"
    
    # 1.75 days up to 30 days
    elif minutes < 43200:  # minutes in month (30 days)
        days = round(minutes / 1440)
        distance_str = f"{days} days"
    
    # 1 month up to 2 months
    elif minutes < 86400:  # minutes in 2 months
        distance_str = "about 1 month"
    
    else:
        months = difference_in_months(later_date, earlier_date)
        
        # 2 months up to 12 months
        if months < 12:
            nearest_month = round(minutes / 43200)  # minutes in month
            if nearest_month < 2:
                distance_str = "about 1 month"
            else:
                distance_str = f"{nearest_month} months"
        
        # 1 year and beyond
        else:
            months_since_start_of_year = months % 12
            years = months // 12
            
            # N years up to 1 years 3 months
            if months_since_start_of_year < 3:
                distance_str = f"about {years} year" if years == 1 else f"about {years} years"
            
            # N years 3 months up to N years 9 months
            elif months_since_start_of_year < 9:
                distance_str = f"over {years} year" if years == 1 else f"over {years} years"
            
            # N years 9 months up to N year 12 months
            else:
                next_years = years + 1
                distance_str = f"almost {next_years} year" if next_years == 1 else f"almost {next_years} years"
    
    # Add suffix if requested
    if options.get('addSuffix', False):
        if comparison > 0:
            distance_str = f"in {distance_str}"
        else:
            distance_str = f"{distance_str} ago"
    
    return distance_str
