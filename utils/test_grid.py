import unittest
from utils.grid import load_from_string

class TestGridFunctions(unittest.TestCase):
    def test_load_from_string(self):
        s = "abc"
        expected = [['a', 'b', 'c']]
        result = load_from_string(s)
        self.assertEqual(result, expected)

    def test_load_2d_array_from_string_multiple_lines(self):
        s = "abc\ndef\nghi"
        expected = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
        result = load_from_string(s)
        self.assertEqual(result, expected)

    def test_load_2d_array_from_string_empty_string(self):
        s = ""
        expected = [[]]
        result = load_from_string(s)
        self.assertEqual(result, expected)

    def test_load_2d_array_from_string_with_spaces(self):
        s = "a b c\n d e f \ng h i"
        expected = [['a', ' ', 'b', ' ', 'c'], [' ', 'd', ' ', 'e', ' ', 'f', ' '], ['g', ' ', 'h', ' ', 'i']]
        result = load_from_string(s)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()