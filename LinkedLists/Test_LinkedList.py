import unittest
from LinkedList import *


class TestLinkedList(unittest.TestCase):
    def test_linked_list_insert_first(self):
        linked_list = LinkedList()
        linked_list.insert_end(1)
        linked_list.insert_end(2)
        self.assertEqual(linked_list.size_of_list(), 2)


if __name__ == '__main__':
    unittest.main()
