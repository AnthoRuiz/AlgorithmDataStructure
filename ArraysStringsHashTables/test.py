import unittest
from CheckArray import *
from TwoSum import *
from GroupAnagrams import *
from SetMatrixZeroes import *


class TestArray(unittest.TestCase):
    def test_is_unique_hash(self):
        self.assertEqual(is_unique_brute("abcd"), True)
        self.assertEqual(is_unique_brute("aAbBcCdDeE"), True)
        self.assertEqual(is_unique_brute("loremLOREM"), True)
        self.assertEqual(is_unique_brute("abcded"), False)

    def test_is_unique_brute(self):
        self.assertEqual(is_unique_set("abcd"), True)
        self.assertEqual(is_unique_set("aAbBcCdDeE"), True)
        self.assertEqual(is_unique_set("loremLOREM"), True)
        self.assertEqual(is_unique_set("abcded"), False)

    def test_two_sum_brute(self):
        self.assertEqual(two_sum_brute([9, 2, 5, 6], 7), [1, 2])
        self.assertEqual(two_sum_brute([1, 4, 10, -3], 14), [1, 2])
        self.assertEqual(two_sum_brute([9, 5, 1, 23], 10), [0, 2])
        self.assertEqual(two_sum_brute([9, 5, 1, 23], 100), [])
        self.assertEqual(two_sum_brute([], 100), [])
        self.assertEqual(two_sum_brute([9], 100), [])

    def test_two_sum_dict(self):
        self.assertEqual(two_sum_dict([9, 2, 5, 6], 7), [1, 2])
        self.assertEqual(two_sum_dict([1, 4, 10, -3], 14), [1, 2])
        self.assertEqual(two_sum_dict([9, 5, 1, 23], 10), [0, 2])
        self.assertEqual(two_sum_dict([9, 5, 1, 23], 100), [])
        self.assertEqual(two_sum_dict([], 100), [])
        self.assertEqual(two_sum_dict([9], 100), [])

    def test_group_anagrams(self):
        self.assertEqual(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]),
                         [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])

        self.assertEqual(group_anagrams(['saco', 'arresto', 'programa', 'rastreo', 'caso']),
                         [['saco', 'caso'], ['arresto', 'rastreo'], ['programa']])

    def test_set_matrix_zeroes(self):
        self.assertEqual(set_zeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]), [[1, 0, 1], [0, 0, 0], [1, 0, 1]])
        self.assertEqual(set_zeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]),
                         [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]])


if __name__ == '__main__':
    unittest.main()
