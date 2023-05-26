class Node:
    """Класс для узла очереди"""

    def __init__(self, data):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = Node


class Queue:
    """Класс для очереди"""

    def __init__(self, data=None):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None



    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        new_node = Node(data)
        # print(f'-- new_node.data {new_node.data} ')
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:

            self.tail.next_node = new_node
            self.tail = new_node
            self.tail.next_node.data = None

            self.next_node = new_node

            # print(f'-- new_node {new_node} ')
            # print(f'-- tail {self.tail} ')
            # print(f'-- tail next_node {self.tail.next_node} ')
            # print(f'-- next_node  {self.next_node} ')
            #

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        pass


    def __str__(self):
        """Магический метод для строкового представления объекта"""

        if self.head == None:
             return ""
        else:
            str_self = ""
            head = self.head
            while head.data != None:

                str_self+=head.data
                head = head.next_node
                if head.data != None:
                    str_self += '\n'

            return str_self


