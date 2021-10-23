"""Test Linked List utilities."""
from code_challenges.linked_lists.linked_list import LinkedList, ListNode


def test_linked_list():
    """Test LinkedList class."""
    head = ListNode(5, ListNode(8, ListNode(15)))

    # Basic cases
    assert LinkedList.to_list(head) == [5, 8, 15]
    assert LinkedList.to_list(None) == []

    # Test inverse function
    assert LinkedList.to_list(LinkedList([1, 4, 9, 10]).head) == [1, 4, 9, 10]
