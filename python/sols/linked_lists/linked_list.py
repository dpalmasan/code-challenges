"""Implement utilities for Linked Lists."""
from typing import List, Optional


class ListNode:
    """Simple node implementation for integer Linked List."""

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        """Constructor."""
        self.val = val
        self.next = next


class LinkedList:
    """Implement integer linked list."""

    def __init__(self, input: List[int]):
        """Constructor."""
        self._head = None
        self.sz = len(input)
        if input:
            self._head = ListNode(input[0])
            self.sz = 1
            pointer = self._head
            for el in input[1:]:
                pointer.next = ListNode(el)
                pointer = pointer.next

    @property
    def head(self):
        """Return head node."""
        return self._head

    @staticmethod
    def to_list(head: Optional[ListNode]) -> List[int]:
        """Given a head, converts it into a list."""
        output = []
        if head:
            pointer: Optional[ListNode] = head
            while pointer:
                output.append(pointer.val)
                pointer = pointer.next
        return output
