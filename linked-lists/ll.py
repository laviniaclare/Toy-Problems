"""Contains linked list with all completed functions, used for easy testing"""

class Node(object):
    """Node in a linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    """Linked List using head and tail."""

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def is_empty(self):
        if not self.head and not self.tail:
            return True
        return False

    def add_node(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def print_nodes(self):
        cur = self.head
        while cur:
            print cur.data
            cur = cur.next

    def get_length(self):
        length = 0
        cur = self.head

        while cur:
            length += 1
            cur = cur.next

        return length

    def remove_odds(self):
        """takes in a linked list whose nodes contain integers and removes all nodes
        whose data is odd
        """
        cur = self.head

        while cur:
            if cur == self.head and cur.data % 2:
                self.head = cur.next
                cur = self.head
                if not cur:
                    self.tail = None
                continue

            if cur and cur.data % 2:
                prev.next = cur.next
                cur = cur.next
                if not cur:
                    self.tail = prev

            if cur and not cur.data % 2:
                prev = cur
                cur = cur.next
