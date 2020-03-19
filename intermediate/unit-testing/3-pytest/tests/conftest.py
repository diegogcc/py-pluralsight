''' Shared fixtures '''

import pytest

from phonebook.phonenumbers import PhoneBook

''' test fixtures 

    changing the 'return' statement for a 'yield' statement,
    we can simulate a tearDown after each test because we can put code AFTER the yield.

    OR

    we can add 'tmpdir' as a argument and pytest will supply it at runtime

    Note: see other fixtures like 'tmpdir' using:
        '$ pytest --fixtures'
'''
@pytest.fixture
def phonebook(tmpdir):
    ''' Provides an empty PhoneBook '''
    phonebook =  PhoneBook(tmpdir)
    return phonebook            # using tmpdir, we don't need the yield statement               
    # yield phonebook
    # phonebook.clear()           # clears the phonebook.txt file after yielding the instance
