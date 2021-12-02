"""
908. Smallest Range I

You are given an integer array nums and an integer k.

In one operation, you can choose any index i where 0 <= i < nums.length and change nums[i] to nums[i] + x where x is an integer from the range [-k, k]. You can apply this operation at most once for each index i.

The score of nums is the difference between the maximum and minimum elements in nums.

Return the minimum score of nums after applying the mentioned operation at most once for each index in it.

Constraints:
A) 1 <= nums.length <= 10^4
B) 0 <= nums[i] <= 10^4
C) 0 <= k <= 10^4

Approach:
1) Find max and min value in the array.
2) Add k to min and subtract k from max.
3) Now check if min is greater than max or not : If 'yes' that means that we can make two same values in array : and thus their ans will be 0 , as 4) it is the minimum 'Score'
5) If 'No' then difference of max and min will be the minimum 'Score' for the array

"""

from typing import List


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        if not k and len(nums)==1:
            return 0
        mi = min(nums)+k
        mx = max(nums)-k
        if mi>mx:
            return 0
        else:
            return mx-mi