from pytest import raises
from datetime import datetime
from .to_date import to_date

def test_it_returns_a_clone_of_the_given_date():
    date = datetime(2016, 1, 1)
    result = to_date(date)
    date = date.replace(year=2015)
    assert result == datetime(2016, 1, 1)

def test_it_creates_a_date_from_a_timestamp():
    timestamp = datetime(2016, 1, 1, 23, 30, 45, 123).timestamp()
    result = to_date(timestamp)
    assert result == datetime(2016, 1, 1, 23, 30, 45, 123)

def test_it_raises_valueerror_if_argument_is_nan():
    with raises(ValueError):
        to_date(float('nan'))

def test_it_returns_date_instance_if_argument_is_date_instance():
    date = datetime(2016, 1, 1)
    result = to_date(date)
    assert isinstance(result, datetime)