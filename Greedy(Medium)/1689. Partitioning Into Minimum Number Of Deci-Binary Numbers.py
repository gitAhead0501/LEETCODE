"""
1689. Partitioning Into Minimum Number Of Deci-Binary Numbers
A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros. For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.

Given a string n that represents a positive decimal integer, return the minimum number of positive deci-binary numbers needed so that they sum up to n.

Constraints:
A) 1 <= n.length <= 105
B) n consists of only digits.
C) n does not contain any leading zeros and represents a positive integer.

Approach: Steps needed is the maximum value in the string itself

"""


class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))