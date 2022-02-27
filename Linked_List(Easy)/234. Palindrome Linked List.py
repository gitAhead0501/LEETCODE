"""
234. Palindrome Linked List

Given the head of a singly linked list, return true if it is a palindrome.

Constraints:
1) The number of nodes in the list is in the range [1, 105].
2) 0 <= Node.val <= 9
 
Follow up: Could you do it in O(n) time and O(1) space?

Approach1: Additional space
Approach2: Constant space : Reverse the first half and compare with second half.

"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev,slow,fast = None,head,head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev