class Node:
    """Базовый класс узла"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node
