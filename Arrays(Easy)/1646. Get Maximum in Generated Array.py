"""
1646. Get Maximum in Generated Array

You are given an integer n. A 0-indexed integer array nums of length n + 1 is generated in the following way:
nums[0] = 0
nums[1] = 1
nums[2 * i] = nums[i] when 2 <= 2 * i <= n
nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n
Return the maximum integer in the array nums​​​.

Constraints:
A) 0 <= n <= 100

Approach: Generate the array using given info and return max from it

"""


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if not n: return 0
        nums = [0]*(n+1)
        nums[0], nums[1] = 0,1
        i = 1
        while (2 <= 2 * i <= n) and (2 <= 2 * i + 1 <= n):
            nums[2*i] = nums[i]
            nums[2*i+1] = nums[i] + nums[i+1]
            i+=1
        return max(nums)