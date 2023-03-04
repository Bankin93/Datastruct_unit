from datastruct.node import Node


class LinkedList:
    """Класс связанный список"""
    def __init__(self):
        self.first_node = None
        self.last_node = None

    def insert_beginning(self, data):
        """Метод принимает данные (словарь) и добавляет узел
        с этими данными в начало связанного списка"""
        new_node = Node(data)
        if self.first_node is None:
            self.first_node = new_node
            self.last_node = new_node
        else:
            new_node.next_node = self.first_node
            self.first_node = new_node

    def insert_at_end(self, data):
        """Метод принимает данные (словарь) и добавляет узел
        с этими данными в конец связанного списка"""
        new_node = Node(data)
        if self.last_node is None:
            self.first_node = new_node
            self.last_node = new_node
        else:
            self.last_node.next_node = new_node
            self.last_node = new_node

    def print_ll(self):
        """Метод для вывода в консоль данных из односвязанного списка"""
        ll_string = ''
        node = self.first_node
        if node is None:
            print(None)
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next_node

        ll_string += 'None'
        return ll_string
