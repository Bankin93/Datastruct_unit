from datastruct.node import Node


class Queue:
    """Базовый класс очереди"""
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """добавления данных в очередь"""
        new_node = Node(data)
        if self.tail is not None:
            self.tail.next_node = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def dequeue(self):
        """Метод удаляет из очереди первый добавленный элемент,
        и возвращает данные удаленного экземпляра класса Node"""
        if self.head is None:
            return None
        value = self.head.data
        self.head = self.head.next_node
        return value
