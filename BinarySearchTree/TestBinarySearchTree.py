import unittest
from BinarySearchTree import *


class TestBinarySearchTree(unittest.TestCase):
    def test_bst_insert(self):
        bst_test = BinarySearchTree()
        bst_test.insert(10)
        bst_test.insert(5)
        bst_test.insert(8)
        bst_test.insert(12)
        bst_test.insert(-5)
        bst_test.insert(44)
        self.assertEqual(bst_test.in_order(bst_test.root), [-5, 5, 8, 10, 12, 44])

    def test_bst_get_max(self):
        bst_test = BinarySearchTree()
        bst_test.insert(10)
        bst_test.insert(5)
        bst_test.insert(8)
        self.assertEqual(bst_test.get_max(), 10)

    def test_bst_get_min(self):
        bst_test = BinarySearchTree()
        bst_test.insert(10)
        bst_test.insert(5)
        bst_test.insert(8)
        self.assertEqual(bst_test.get_min(), 5)

    def test_bst_remove(self):
        bst_test = BinarySearchTree()
        bst_test.insert(10)
        bst_test.insert(5)
        bst_test.insert(8)
        bst_test.insert(12)
        bst_test.insert(-5)
        bst_test.insert(44)

        bst_test.remove(8)
        bst_test.remove(10)
        bst_test.remove(12)

        self.assertEqual(bst_test.in_order(bst_test.root), [-5, 5, 44])


if __name__ == '__main__':
    unittest.main()
