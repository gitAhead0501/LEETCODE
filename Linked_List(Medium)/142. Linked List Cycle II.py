"""
142. Linked List Cycle II
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

 
Constraints:
A) The number of the nodes in the list is in the range [0, 10^4].
B) -10^5 <= Node.val <= 10^5
C) pos is -1 or a valid index in the linked-list.

Approach:  Take a slow pointer and a fast pointer. Traverse along the linked list while slow and fast pointer are valid or till slow and fast are equal. Again start with head and check at which node head is equal to the fast pointer. We do not modify the linked list

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        _slow = head
        _fast = head
        
        while _slow and _fast:
            _slow = _slow.next
            _fast = _fast.next.next if _fast.next else None
            print(_slow.val,_fast.val)
            if _slow == _fast:
                break
 
        if not _slow or not _fast or _slow != _fast:
            return None
        _slow = head
        while _slow != _fast:
            _slow = _slow.next
            _fast = _fast.next
        return _slow