# -*- coding:utf-8 -*-
import sys
sys.path.append('/home/dispensable/code/AlgorithmExercise/Python')
import unittest
from src.data_structure import check_parenthese_match, Node, LinkedList


class ParentheseTestCase(unittest.TestCase):
    """
    test for parenthese match
    """
    def test_is_parenthese_match(self):
        """
        is `((()())))` match to each other
        """
        self.assertFalse(check_parenthese_match('((()())))')[0])
        self.assertFalse(check_parenthese_match('))')[0])
        self.assertEqual(check_parenthese_match('(), (), ())'), (False, 10))
        self.assertEqual(check_parenthese_match('((())'), (False, 4))


class LinkedListTestCase(unittest.TestCase):
    def setUp(self):
        self.link_list = LinkedList(Node(1))

    def test_add_node(self):
        self.assertEqual(self.link_list.add_node(Node(2)).turn_to_list(), [1, 2])
        self.assertEqual(self.link_list.add_node(Node(2)).add_node(Node(4)).add_node(Node(5)).turn_to_list(), 
                        [1, 2, 2, 4, 5])

    def test_remove_node(self):
        self.link_list.add_node(Node(2)).add_node(Node(2)).add_node(Node(4)).add_node(Node(5))
        self.assertEqual(self.link_list.remove_node(Node(5)).turn_to_list(), [1, 2, 2, 4])
        self.assertEqual(self.link_list.remove_node(Node(1)).turn_to_list(), [2, 2, 4])
        self.assertEqual(self.link_list.remove_node(Node(2)).turn_to_list(), [2, 4])


if __name__ == "__main__":
    unittest.main()