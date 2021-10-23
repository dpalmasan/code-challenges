"""Implement solutions for two pointer problems."""
from typing import Optional
from code_challenges.linked_lists.linked_list import ListNode


def remove_nth_from_end_two_pass(
    head: Optional[ListNode], n: int
) -> Optional[ListNode]:
    """Remove the nth-node from the last given the head of a linked list.

    It does it traversing the list two times.

    :param head: First node of the linked list
    :type head: Optional[ListNode]
    :param n: Node to remove from the last
    :type n: int
    :return: Head of the modified list
    :rtype: Optional[ListNode]
    """
    if head is None:
        return None

    sz = 0
    pointer = head
    while pointer:
        sz += 1
        pointer = pointer.next

    if n == sz:
        head = head.next
        return head

    pos = 1
    pointer = head
    while sz - pos != n:
        pointer = pointer.next
        pos += 1

    pointer.next = pointer.next.next
    pointer = head
    return head


def remove_nth_from_end(
    head: Optional[ListNode], n: int
) -> Optional[ListNode]:
    """Remove the nth-node from the last given the head of a linked list.

    It does it traversing the list one time.

    :param head: First node of the linked list
    :type head: Optional[ListNode]
    :param n: Node to remove from the last
    :type n: int
    :return: Head of the modified list
    :rtype: Optional[ListNode]
    """
    if head is None:
        return None

    slow_pointer = None
    pointer = head
    idx = 1
    while pointer.next:
        pointer = pointer.next
        idx += 1
        if idx - 1 == n:
            slow_pointer = head
        if slow_pointer and pointer.next:
            slow_pointer = slow_pointer.next

    if slow_pointer is None:
        head = head.next
        return head
    slow_pointer.next = slow_pointer.next.next
    return head
