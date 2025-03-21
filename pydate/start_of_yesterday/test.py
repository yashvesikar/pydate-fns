from datetime import datetime
from unittest.mock import patch
from .start_of_yesterday import start_of_yesterday

def test_returns_start_of_yesterday():
    with patch('pydate.start_of_yesterday.start_of_yesterday.datetime') as mock_datetime:
        # Mock datetime.now() to return a specific date
        mock_datetime.now.return_value = datetime(2014, 9, 25, 14, 30, 45, 500)
        mock_datetime.side_effect = datetime
        
        result = start_of_yesterday()
        assert result == datetime(2014, 9, 24, 0, 0, 0, 0)

def test_handles_dates_before_100_ad():
    with patch('pydate.start_of_yesterday.start_of_yesterday.datetime') as mock_datetime:
        # Mock datetime.now() to return a date before 100 AD
        mock_datetime.now.return_value = datetime(14, 9, 25, 0, 0, 0, 0)
        mock_datetime.side_effect = datetime
        
        result = start_of_yesterday()
        assert result == datetime(14, 9, 24, 0, 0, 0, 0)

def test_returns_datetime_instance():
    result = start_of_yesterday()
    assert isinstance(result, datetime)