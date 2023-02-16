from Datastruct.node import Node


class Stack:
    """Базовый класс одноименной структуры данных"""
    def __init__(self):
        self.top = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next_node = self.top
        self.top = new_node
