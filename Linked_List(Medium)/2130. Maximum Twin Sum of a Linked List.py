"""
2130. Maximum Twin Sum of a Linked List

In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.
For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.
Given the head of a linked list with even length, return the maximum twin sum of the linked list.

Constraints:
1) The number of nodes in the list is an even integer in the range [2, 10^5]
2) 1 <= Node.val <= 10^5

Approach:  Reverse the linked list either first half or second half , then traverse both the linked lists i.e. one from head and one from the new reversed and find the maximum sum of their combined node's value and return it

"""

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        ans = 0
        while rev:
            ans = max(ans,rev.val+slow.val)
            slow = slow.next
            rev = rev.next
        return ans


# sample input

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

obj = Solution()
print(obj.pairSum(head))
