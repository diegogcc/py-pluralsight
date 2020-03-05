import unittest
from phonebook import PhoneBook

class PhoneBookTest(unittest.TestCase):

    def setUp(self) -> None:
        self.phonebook = PhoneBook()
    
    def test_lookup_by_name(self):
        self.phonebook.add("Bob", "123456")
        number = self.phonebook.lookup("Bob")
        self.assertEqual("123456", number) 
    
    def test_missing_name(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")
    
    @unittest.skip("WIP")
    def test_skip(self):
        pass

    def test_emtpy_phonebook_consistency(self):
        self.assertTrue(self.phonebook.is_consistent())

    def test_is_consistent_different_entries(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Anna", "012345")
        self.assertTrue(self.phonebook.is_consistent())

    def test_is_consistent_duplicate_entries(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Anna", "12345")
        self.assertFalse(self.phonebook.is_consistent())

    def test_inconsistent_duplicate_prefix(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Anna", "123")
        self.assertFalse(self.phonebook.is_consistent())


if __name__ == "__main__":
    unittest.main()
