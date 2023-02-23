import unittest
from Datastruct.node import Node
from Datastruct.custom_queue import Queue


class TestQueue(unittest.TestCase):
    queue = Queue()
    queue.enqueue('data1')
    queue.enqueue('data2')
    queue.enqueue('data3')

    def test_enqueue(self):
        self.assertEqual(self.queue.head.data, 'data1')
        self.assertEqual(self.queue.head.next_node.data, 'data2')
        self.assertEqual(self.queue.tail.data, 'data3')
        self.assertEqual(self.queue.tail.next_node, None)
        with self.assertRaises(AttributeError):
            Node(self.queue.tail.next_node.data)
