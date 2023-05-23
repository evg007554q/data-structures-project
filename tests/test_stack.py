"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest

from src import stack



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
        st.push('data1')
        st.push('data2')
        st.push('data3')
        self.assertEquals(st.top.data, 'data3')
        self.assertEquals(st.top.next_node.data, 'data2')
        self.assertEquals(st.top.next_node.next_node.data,  'data1')
        self.assertIsNone(st.top.next_node.next_node.next_node)

    def test_stack2(self):
        st = stack.Stack()
        st.push('data1')

        self.assertEquals(st.top.data, 'data1')
