"""
1291. Sequential Digits
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits


Constraints:
A) 10 <= low <= high <= 10^9

Approach1: Store all the possible numbers in an array and use it for less than low and greater than high
Approach2: Store only 123456789 as string and use two for loops to check the numbers less than and greater than given values
Approach3: Use deque to popleft the items and append accordingly only the values btw low and high

"""


from collections import deque
from typing import List


# Approach1:
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        allnums = [12,23,34,45,56,67,78,89, 123,234,345,456,567,678,789, 1234,2345,3456,4567,5678,6789,12345,23456,34567,45678,56789, 123456,234567,345678,456789,1234567,2345678,3456789,12345678,23456789,123456789]
        res = []
        for x in allnums:
            if x < low:
                continue
            if x > high:
                break
            res.append(x)
        return res


# Approach2:
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = '123456789'
        n = len(s)
        res = []
        for i in range(n):
            for j in range(i+1,n):
                st = int(s[i:j+1])
                if st>=low and st<=high:
                    res.append(st)
        res.sort()
        return res



# Approach3:
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        out = []
        queue = deque(range(1,10))
        while queue:
            elem = queue.popleft()
            if low <= elem <= high:
                out.append(elem)
            last = elem % 10
            if last < 9:
                queue.append(elem*10 + last + 1)
        return out