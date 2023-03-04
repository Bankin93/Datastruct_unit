import unittest
from datastruct.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()

    def test_insert_beginning(self):
        self.ll.insert_beginning({'id': 1})
        self.assertEqual(self.ll.first_node.data, {'id': 1})
        self.assertEqual(self.ll.last_node.data, {'id': 1})

        self.ll.insert_beginning({'id': 0})
        self.assertEqual(self.ll.first_node.data, {'id': 0})
        self.assertEqual(self.ll.last_node.data, {'id': 1})

    def test_insert_at_end(self):
        self.ll.insert_at_end({'id': 2})
        self.assertEqual(self.ll.first_node.data, {'id': 2})
        self.assertEqual(self.ll.last_node.data, {'id': 2})

        self.ll.insert_at_end({'id': 3})
        self.assertEqual(self.ll.first_node.data, {'id': 2})
        self.assertEqual(self.ll.last_node.data, {'id': 3})

    def test_print_ll(self):
        self.assertEqual(self.ll.print_ll(), 'None')
        self.ll.insert_beginning({'id': 1})
        self.ll.insert_at_end({'id': 2})
        self.ll.insert_at_end({'id': 3})
        self.ll.insert_beginning({'id': 0})
        self.assertEqual(self.ll.print_ll(), "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")
