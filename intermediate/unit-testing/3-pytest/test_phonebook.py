''' 
run pytest:
    '$ python3 -m pytest'
'''
import pytest

class PhoneBook:
    def __init__(self) -> None:
        self.numbers = {}

    def add(self, name, number):
        self.numbers[name] = number

    def lookup(self, name):
        return self.numbers[name]

    def names(self):
        return set(self.numbers.keys())

def test_lookup_by_name():
        phonebook = PhoneBook()
        phonebook.add("Bob", "123456")
        assert "123456" == phonebook.lookup("Bob")      # assert equal

def test_phonebook_contains_all_names():
    phonebook = PhoneBook()
    phonebook.add("Bob", "12345")
    assert "Bob" in phonebook.names()

def test_missing_name_raises_error():
    phonebook = PhoneBook()
    with pytest.raises(KeyError):
        phonebook.lookup("Bob")