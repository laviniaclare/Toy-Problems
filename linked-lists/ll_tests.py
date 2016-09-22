import unittest
from ll import LinkedList, Node

class RemoveOddsTests(unittest.TestCase):
    
    def test_empty_list(self):
        empty_list = LinkedList()
        empty_list.remove_odds()
        self.assertEqual(empty_list.head, LinkedList().head)
        self.assertEqual(empty_list.tail, LinkedList().tail)

    def test_one_odd_node(self):
        pass

    def test_one_even_node(self):
        pass

    def test_tail_odd(self):
        pass

    def test_tail_even(self):
        pass

    def test_head_even(self):
        pass

    def test_head_odd(self):
        pass

    def test_all_even(self):
        pass

    def test_all_odd(self):
        pass



if __name__ == "__main__":
    unittest.main()