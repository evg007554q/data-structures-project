"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest

from src import stack

from src import queue
from src.queue import Queue


class Test_stack(unittest.TestCase):
    def test_Node(self):
        self.assertEquals( stack.Node(5, None).data  ,5)
        self.assertIsNone(stack.Node(5, None).next_node)
    def test_Node2(self):
        n1 = stack.Node(5, None)
        n2 = stack.Node('a', n1)
        self.assertEquals(n2.next_node , n1)
        self.assertEquals(n2.data, 'a')

    def test_stack(self):
        st = stack.Stack()
        self.assertEquals(st.top, None)
        st.push('data1')
        st.push('data2')
        self.assertEquals(st.top.next_node.next_node, None)
        st.push('data3')
        self.assertEquals(st.top.data, 'data3')
        self.assertEquals(st.top.next_node.data, 'data2')
        self.assertEquals(st.top.next_node.next_node.data,  'data1')
        self.assertEquals(st.top.next_node.next_node.data, 'data1')


    def test_stack2(self):
        st = stack.Stack()
        st.push('data1')

        self.assertEquals(st.top.data, 'data1')

    def test_pop(self):
        st = stack.Stack()
        st.push('data1')
        data1 = st.pop()

        # стэк стал пустой
        self.assertEquals(st.top, None)

        # pop() удаляет элемент и возвращает данные удаленного элемента

        self.assertEquals(data1, 'data1')

        st2 = stack.Stack()
        st2.push('data1')
        st2.push('data2')

        data2 = st2.pop()

        # теперь последний элемента содержит данные data1
        self.assertEquals(st2.top.data , 'data1')

        # данные удаленного элемента
        self.assertEquals(data2, 'data2')

    def test_HW3_stack(self):
        # HW3 test __str__
        st = stack.Stack()
        st.push('data1')
        st.push('data2')
        print(str(st))
        self.assertEquals(str(st), 'data2\ndata1')
    def test_HW3_Queue(self):
        # HW3 test Queue
        qu1 = Queue()

        self.assertEquals(str(qu1), '')
        qu1.enqueue('data1')
        qu1.enqueue('data2')
        qu1.enqueue('data3')
        self.assertEquals(qu1.head.data, 'data1')
        self.assertEquals(qu1.head.next_node.data, 'data2')
        self.assertEquals(qu1.tail.data, 'data3')
        self.assertIsNone(qu1.tail.next_node.data)

        # assert str(queue) == "data1\ndata2\ndata3"
        self.assertEquals(str(qu1), "data1\ndata2\ndata3")
