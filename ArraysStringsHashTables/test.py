import unittest
from CheckArray import *


class TestArray(unittest.TestCase):
    def test_is_unique_hash(self):
        self.assertEqual(is_unique_brute("hola"), True)
        self.assertEqual(is_unique_brute("holaa"), False)
        self.assertEqual(is_unique_brute("aaaabbbbbbbbbbbccccccccccdddddddddd"), False)
        self.assertEqual(is_unique_brute("lorem"), True)
        self.assertEqual(is_unique_brute("AskgWevjforja"), False)

    def test_is_unique_brute(self):
        self.assertEqual(is_unique_brute("hola"), True)
        self.assertEqual(is_unique_brute("holaa"), False)
        self.assertEqual(is_unique_brute("aaaabbbbbbbbbbbccccccccccdddddddddd"), False)
        self.assertEqual(is_unique_brute("lorem"), True)
        self.assertEqual(is_unique_brute("AskgWevjforja"), False)


if __name__ == '__main__':
    unittest.main()
