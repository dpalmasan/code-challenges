"""Test suite for two pointer problems."""
from code_challenges.linked_lists.linked_list import LinkedList
from code_challenges.linked_lists import two_pointers as tp


def test_remove_nth_node_two_pass_sample_cases():
    """Test sample cases."""
    ll = LinkedList([1, 2, 3, 4, 5])
    tp.remove_nth_from_end_two_pass(ll.head, 2)
    assert LinkedList.to_list(ll.head) == [1, 2, 3, 5]
    ll = LinkedList([1, 2])
    tp.remove_nth_from_end_two_pass(ll.head, 1)
    assert LinkedList.to_list(ll.head) == [1]


def test_remove_nth_node_sample_cases():
    """Test sample cases."""
    ll = LinkedList([1, 2, 3, 4, 5])
    tp.remove_nth_from_end(ll.head, 2)
    assert LinkedList.to_list(ll.head) == [1, 2, 3, 5]
    ll = LinkedList([1, 2])
    tp.remove_nth_from_end(ll.head, 1)
    assert LinkedList.to_list(ll.head) == [1]


def test_remove_nth_node_two_pass_corner_cases():
    """Test corner cases."""
    ll = LinkedList([1])
    head = tp.remove_nth_from_end_two_pass(ll.head, 1)
    assert LinkedList.to_list(head) == []
    head = None
    tp.remove_nth_from_end_two_pass(head, 1)
    assert LinkedList.to_list(head) == []


def test_remove_nth_node_corner_cases():
    """Test corner cases."""
    ll = LinkedList([1])
    head = tp.remove_nth_from_end(ll.head, 1)
    assert LinkedList.to_list(head) == []
    head = None
    tp.remove_nth_from_end(head, 1)
    assert LinkedList.to_list(head) == []
