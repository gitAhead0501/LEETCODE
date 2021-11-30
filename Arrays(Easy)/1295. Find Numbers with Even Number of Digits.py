"""
1295. Find Numbers with Even Number of Digits
Given an array nums of integers, return how many of them contain an even number of digits.

Constraints:
A) 1 <= nums.length <= 500
B) 1 <= nums[i] <= 10^5

Approach1: For each number in array check if the str data type of number's length is even or not [trick]
Approach2: Create a function for check if it contains even no of digits of not [logical approach]
Approach3: Only numbers between 10 and 99 or 1000 and 9999 or 100000 have even number of digits [trick]

"""

from typing import List

# 1) 
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                count += 1
        return count

# 2) 
class Solution:
    def hasEven(self,x:int) -> bool:
        r = True
        while x:
            r   = not r
            x //= 10
        return r
    def findNumbers(self, nums: List[int]) -> int:
        n = 0
        for x in nums:
            n += self.hasEven(x)
        return n


# 3)
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            if 10 <= i<=99 or 1000<= i<=9999 or i==100000:
                count += 1
        return count