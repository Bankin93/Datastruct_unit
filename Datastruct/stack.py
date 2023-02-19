from Datastruct.node import Node


class Stack:
    """Базовый класс одноименной структуры данных"""
    def __init__(self):
        self.top = None

    def push(self, new_data):
        """Создание экземпляра Node, для связывания данных в стеке"""
        new_node = Node(new_data)
        new_node.next_node = self.top
        self.top = new_node

    def pop(self):
        """Метод удаляет из стека верхний элемент (последний добавленный)
         и возвращает данные удаленного экземпляра класса Node"""
        if self.top is None:
            return None
        value = self.top
        self.top = self.top.next_node
        return value.data
