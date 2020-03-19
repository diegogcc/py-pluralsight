''' 
run pytest:
    '$ python3 -m pytest'

pytest fixtures :
    '$ pytest --fixtures'
'''
import pytest


def test_lookup_by_name(phonebook):
    phonebook.add("Bob", "123456")
    assert "123456" == phonebook.lookup("Bob")      # assert equal

def test_phonebook_contains_all_names(phonebook):
    phonebook.add("Bob", "12345") 
    assert "Bob" in phonebook.names()

def test_missing_name_raises_error(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup("Bob")