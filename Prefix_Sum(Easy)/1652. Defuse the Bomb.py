"""
1652. Defuse the Bomb

You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.

To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.

If k > 0, replace the ith number with the sum of the next k numbers.
If k < 0, replace the ith number with the sum of the previous k numbers.
If k == 0, replace the ith number with 0.
As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!

Constraints:
A) n == code.length
B) 1 <= n <= 100
C) 1 <= code[i] <= 100
D) -(n - 1) <= k <= n - 1

Approach1: k numbers ahead for a circular array can be traversed by extending the array by itself : k numbers behind can be traversed first reversing the array then solving it for k>0 and then returning the reversed ans

"""

from itertools import accumulate
from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k<0: return self.decrypt(code[::-1],-k)[::-1]
        p = [*accumulate(code+code)]
        return [p[i+k]-p[i] for i in range(len(code))]