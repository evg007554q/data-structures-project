class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node
        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """

        if self.top:
            nn = Node(data,self.top)
        else:
            nn = Node(data,None)
        self.top = nn


    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        del_st = self.top.data
        self.top=self.top.next_node
        return del_st

    def __str__(self):
        """Магический метод для строкового представления объекта"""

        if self.top == None:
            return ""
        else:
            str_self = ""

            top = self.top

            while top != None:
                str_self += top.data

                top = top.next_node
                if top != None:
                    str_self += '\n'

            return str_self