"""
You are given a positive integer num consisting only of digits 6 and 9.
Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

Constraints:
A) 1 <= num <= 104
B) num consists of only 6 and 9 digits.

Approach1: Converting int to string and the replacing the first 6 with 9
Approach2: Replacing the first 6 with 9 but via mathematical approach

"""

# 1)
import math


class Solution:
    def maximum69Number (self, num: int) -> int:
        return int(str(num).replace('6','9',1))



# 2)
class Solution:
    def maximum69Number (self, num: int) -> int:
        digits = int(math.log(num,10))
        while digits>=0:
            v = num//(10**digits)%10
            if v==6:
                return num + 3*(10**digits)
            digits -= 1
        return num