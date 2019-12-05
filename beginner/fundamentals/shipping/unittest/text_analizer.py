import os
import unittest

def analize_text(filename):
    """Calculate the number of lines and characters in a file.
    
    Args:
        filename: The name of the file to analize
        
    Raises:
        IOError: If ''Filename'' does not exist or can't be read.
    
    Returns:
        A tuple where the first element is the number of lines in
        the file and the second element is the number of characters.
    """
    lines = 0
    chars = 0
    with open(filename, 'r') as f:
        for line in f:
            lines += 1
            chars += len(line)
    return (lines, chars)

class TextAnalisisTests(unittest.TestCase):
    """Tests for the ''analize_text()'' function"""

    def setUp(self):
        """Fixture that creates a file for the text methods to use."""
        self.filename = 'text_analisis_test_file.txt'
        with open(self.filename, 'w') as f:
            f.write('Now we are engaged in a great civil war. \n'
                    'testing wheter that nation,\n'
                    'or any nation so conceived and so dedicated,\n'
                    'can long endure.')
    
    def teatDown(self):
        """Fixture that deletes the files used by the test methods."""
        try:
            os.remove(self.filename)
        except:
            pass

    def test_function_runs(self):
        """Basic smoke test: does the function run"""
        analize_text(self.filename)

    def test_line_counts(self):
        """Check that the line count is correct."""
        self.assertEqual(analize_text(self.filename)[0], 4)

    def test_character_count(self):
        """Check that the character count is correct."""
        self.assertEqual(analize_text(self.filename)[1], 131)

    def test_no_such_file(self):
        """Check the proper exception is thrown for a missing file."""
        with self.assertRaises(IOError):
            analize_text('foobar')

    def test_no_deletion(self):
        """Check that the function doesnt delete the input file."""
        analize_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))

if __name__ == '__main__':
    unittest.main()