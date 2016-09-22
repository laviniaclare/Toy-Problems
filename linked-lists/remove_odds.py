
"""Implement a linked list with a method "remove_odds" which removes all nodes containing odd
numbers from the list. Assume that all nodes contain integers as their data. The linked list
should have both a head and a tail"""

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

    def remove_odds(self):
        cur = self.head

        while cur:
            if cur == self.head and cur.data % 2:
                self.head = cur.next
                cur = self.head
                if not cur:
                    self.tail = None
                continue
            elif cur == self.head and not cur.data % 2:
                prev = cur
                cur = cur.next

            if cur and cur.data % 2:
                prev.next = cur.next
                cur = cur.next
                if not cur:
                    self.tail = prev

            if cur == self.tail:
                return
