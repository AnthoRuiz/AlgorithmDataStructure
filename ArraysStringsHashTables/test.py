import unittest
from CheckArray import *
from TwoSum import *
from GroupAnagrams import *
from SetMatrixZeroes import *
from ReverseArray import *
from Palindrome import *
from ReverseInteger import *
from Anagram import *


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

    def test_reverse_array(self):
        self.assertEqual(reverse(["h", "e", "l", "l", "o"]), (["o", "l", "l", "e", "h"]))
        self.assertEqual(reverse(["H", "a", "n", "n", "a", "h"]), (["h", "a", "n", "n", "a", "H"]))
        self.assertEqual(reverse(['a']), (['a']))
        self.assertEqual(reverse([]), ([]))

    def test_palindrome(self):
        self.assertEqual(is_palindrome('radar'), True)
        self.assertEqual(is_palindrome('aaaa'), True)
        self.assertEqual(is_palindrome('car'), False)

    def test_reverse_int(self):
        self.assertEqual(reverse_integer(859), 958)
        self.assertEqual(reverse_integer(1234), 4321)
        self.assertEqual(reverse_integer(8), 8)

    def test_anagram(self):
        self.assertEqual(is_anagram('anagram', 'nagaram'), True)
        self.assertEqual(is_anagram('rat', 'car'), False)
        self.assertEqual(is_anagram('', ' '), False)


if __name__ == '__main__':
    unittest.main()
