"""
1389. Create Target Array in the Given Order
Given two arrays of integers nums and index. Your task is to create target array under the following rules:

Initially target array is empty.
From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
Repeat the previous step until there are no elements to read in nums and index.
Return the target array.

It is guaranteed that the insertion operations will be valid.

Constraints:
A) 1 <= nums.length, index.length <= 100
B) nums.length == index.length
C) 0 <= nums[i] <= 100
D) 0 <= index[i] <= i

Approach1: Brute Force : Use inBuilt function : insert (ACCEPTED)
Approach2: Hash Table : Store the order hash table and append reverse of values of hashtable , return stored array (NOT ACCEPTED : DOES NOT PASS EACH TEST CASE : BECOZ SOMETIMES THE VALUES STORED IN HASTBALE ARE NOT IN ORDER)
Approach3: Insert at the required position while shifting other items

"""

from typing import List

# 1) ACCEPTED : BRUTE
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for num, idx in zip(nums, index):
            target.insert(idx, num)
        return target


# 2) NOT ACCEPTED
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        h = {}
        for i in range(len(index)):
            if index[i] not in h:
                h[index[i]] = [nums[i]]
            else:
                h[index[i]].append(nums[i])
        print(h)
        res = []
        for each in h.values():
            res += each[::-1]
        return res


# 3) ACCEPTED : LOGICAL : 
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            if index[i]!=i:
                val = nums[i]
                j = i
                r = index[i]
                while j!=r:
                    nums[j] = nums[j-1]
                    j-=1
                nums[r] = val
        return nums