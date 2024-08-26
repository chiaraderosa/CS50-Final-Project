import pytest
from datetime import datetime
from project import calculate_days_until_birthday, is_valid_date, get_message_based_on_input

def test_calculate_days_until_birthday():
    assert calculate_days_until_birthday("01/09") == (datetime(datetime.now().year, 9, 1) - datetime.now()).days
    assert calculate_days_until_birthday("01/01") == (datetime(datetime.now().year + 1, 1, 1) - datetime.now()).days

def test_is_valid_date():
    assert is_valid_date("01/01") == True
    assert is_valid_date("31/12") == True
    assert is_valid_date("15/07") == True
    assert is_valid_date("00/01") == False
    assert is_valid_date("31/02") == False
    assert is_valid_date("15/13") == False
    assert is_valid_date("15/07/2024") == False  # Invalid format
    

def test_get_message_based_on_input():
    assert get_message_based_on_input("00/01") == "Please enter a valid date in the format DD/MM."