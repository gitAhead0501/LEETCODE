"""
1720. Decode XORed Array
There is a hidden integer array arr that consists of n non-negative integers.

It was encoded into another integer array encoded of length n - 1, such that encoded[i] = arr[i] XOR arr[i + 1]. For example, if arr = [1,0,2,1], then encoded = [1,2,3].

You are given the encoded array. You are also given an integer first, that is the first element of arr, i.e. arr[0].

Return the original array arr. It can be proved that the answer exists and is unique.

Constraints:
A) 2 <= n <= 104
B) encoded.length == n - 1
C) 0 <= encoded[i] <= 10**5
D) 0 <= first <= 10**5

Approach1: Use associative property of XOR, if a xor b is c then a xor c is b : we store this b
Methods : 1) For loop and array to store : 2) Using inbuilt modules Itertools and accumulate and operator
Approach2: BIT Manipulation

"""


from typing import List
import itertools
import operator

# 1) For Loop
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        for i in range(len(encoded)):
            arr.append(arr[i]^encoded[i])
        return arr

# 1) Modules : ONE LINER
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        return list(itertools.accumulate(encoded, func=operator.xor, initial=first))