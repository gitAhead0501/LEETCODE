"""
19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Constraints:
A) The number of nodes in the list is sz.
B) 1 <= sz <= 30
C) 0 <= Node.val <= 100
D) 1 <= n <= sz

Approach: Simply remove the link of the prev node of the target node and link to the next node of the target value if it exists else assign it as None.

"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None
        curr = head
        ln = 0
        while curr:
            ln += 1
            curr = curr.next
        if ln == n:
            head = head.next
            return head
        curr1 = head
        for i in range(ln-n-1):
            curr1 = curr1.next
        if curr1.next.next == None:
            curr1.next = None
            return head
        curr1.next = curr1.next.next
        return head