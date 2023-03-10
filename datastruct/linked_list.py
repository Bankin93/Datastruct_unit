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

    def to_list(self):
        """возвращает список с данными, содержащимися
         в односвязном списке LinkedList"""
        ll_list = []
        node = self.first_node
        while node is not None:
            ll_list.append(node.data)
            node = node.next_node
        return ll_list

    def get_data_by_id(self, value: int):
        """возвращает первый найденный в LinkedList
        словарь с ключом id, значение которого
        равно переданному в метод значению"""
        node = self.first_node
        while node is not None:
            try:
                if node.data['id'] == value:
                    return node.data
                node = node.next_node
            except TypeError:
                print('Данные не являются словарем или в словаре нет id.')
                break
        return None

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

#if __name__ == '__main__':
    # ll = LinkedList()
    #
    # ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
    # ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
    # ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
    # ll.insert_beginning({'id': 0, 'username': 'serebro'})

    # метод to_list()
    # lst = ll.to_list()
    # for item in lst: print(item)
    # {'id': 0, 'username': 'serebro'}
    # {'id': 1, 'username': 'lazzy508509'}
    # {'id': 2, 'username': 'mik.roz'}
    # {'id': 3, 'username': 'mosh_s'}

    # get_data_by_id()
    # user_data = ll.get_data_by_id(3)
    # print(user_data)
    #{'id': 3, 'username': 'mosh_s'}

    # работа блока try/except
    # ll = LinkedList()
    # ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
    # ll.insert_at_end('idusername')
    # ll.insert_at_end([1, 2, 3])
    # ll.insert_at_end({'id': 2, 'username': 'mosh_s'})

    #user_data = ll.print_ll()
    #user_data = ll.get_data_by_id(2)
    # Данные не являются словарем или в словаре нет id.
    # Данные не являются словарем или в словаре нет id.
    #print(user_data)
    #{'id': 2, 'username': 'mosh_s'}
