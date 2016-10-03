import unittest
from ll import LinkedList, Node

class RemoveOddsTests(unittest.TestCase):
    
    def test_empty_list(self):
        empty_list = LinkedList()
        empty_list.remove_odds()
        self.assertTrue(empty_list.is_empty())

    def test_one_odd_node(self):
        node = Node(3)
        one_odd_list = LinkedList()
        one_odd_list.add_node(node)
        one_odd_list.remove_odds()

        "it should produce and empty list has only one node, which is odd"
        self.assertTrue(one_odd_list.is_empty())

    def test_one_even_node(self):
        one_even_list = LinkedList()
        one_even_list.add_node(Node(2))
        one_even_list.remove_odds()
        "it should not change the list if the list has ony one node, which is even"
        self.assertEqual(one_even_list.get_length(), 1)

    def test_tail_odd(self):
        odd_tail = LinkedList()
        node_vals = [2, 3, 4, 5]
        for node_val in node_vals:
            odd_tail.add_node(Node(node_val))

        odd_tail.remove_odds()
        "it should remove the tail if the tail is odd and the head is even"
        self.assertEqual(odd_tail.tail.data, 4)
        self.assertEqual(odd_tail.get_length(), 2)

    def test_tail_even(self):
        even_tail = LinkedList()
        node_vals = [2, 3, 4, 10]
        for node_val in node_vals:
            even_tail.add_node(Node(node_val))

        even_tail.remove_odds()
        "it should remove odds if the tail is even and the head is even"
        self.assertEqual(even_tail.tail.data, 10)
        self.assertEqual(even_tail.get_length(), 3)
        

    def test_head_odd(self):
        odd_head = LinkedList()
        node_vals = [3, 4, 5, 6]
        for node_val in node_vals:
            odd_head.add_node(Node(node_val))

        odd_head.remove_odds()
        "it should remove odds when the head node is odd and the tail is even"
        self.assertEqual(odd_head.head.data, 4)
        self.assertEqual(odd_head.get_length(), 2)
        self.assertEqual(odd_head.tail.data, 6)

    def test_all_even(self):
        all_even = LinkedList()
        node_vals = [2, 4, 6]
        for node_val in node_vals:
            all_even.add_node(Node(node_val))

        all_even.remove_odds()
        "It should not remove any nodes if all nodes are even"
        self.assertEqual(all_even.get_length(), 3)

    def test_all_odd(self):
        pass



if __name__ == "__main__":
    unittest.main()