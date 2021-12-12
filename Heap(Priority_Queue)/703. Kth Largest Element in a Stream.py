"""
703. Kth Largest Element in a Stream

Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
 

Constraints:
A) 1 <= k <= 10^4
B) 0 <= nums.length <= 10^4
C) -10^4 <= nums[i] <= 10^4
D) -10^4 <= val <= 10^4
E) At most 10^4 calls will be made to add.
F) It is guaranteed that there will be at least k elements in the array when you search for the kth element.

Approach: Create heapq of array, heapify the array: pop from the heap till length equals k: heappush the new val and return the heap's last 0 index value

"""

import heapq
from typing import List
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap)>k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap)>self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)