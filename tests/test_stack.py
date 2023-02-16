import unittest

from Datastruct.node import Node

from Datastruct.stack import Stack


class TestStack(unittest.TestCase):
    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    stack.push('data3')

    def test_push(self):
        self.assertEqual(self.stack.top.data, 'data3')
        self.assertEqual(self.stack.top.next_node.data, 'data2')
        self.assertEqual(self.stack.top.next_node.next_node.data, 'data1')
        self.assertEqual(self.stack.top.next_node.next_node.next_node, None)
        with self.assertRaises(AttributeError):
            Node(self.stack.top.next_node.next_node.next_node.data)

