from datetime import datetime
from unittest.mock import patch
from .start_of_today import start_of_today

def test_returns_start_of_today():
    with patch('pydate.start_of_today.start_of_today.datetime') as mock_datetime:
        # Mock datetime.now() to return a specific date
        mock_datetime.now.return_value = datetime(2014, 9, 25, 14, 30, 45, 500)
        mock_datetime.side_effect = datetime
        
        result = start_of_today()
        assert result == datetime(2014, 9, 25, 0, 0, 0, 0)

def test_returns_datetime_instance():
    result = start_of_today()
    assert isinstance(result, datetime)