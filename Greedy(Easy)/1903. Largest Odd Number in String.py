"""
1903. Largest Odd Number in String
You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.

A substring is a contiguous sequence of characters within a string.

Constraints:
A) 1 <= num.length <= 105
B) num only consists of digits and does not contain any leading zeros.

Approach: Find the rightmost odd digit and return upto that index
Methods: Search value in set {1,3,5,7,9} or int(value)%2 check for odd

"""

class Solution:
    def largestOddNumber(self, num: str) -> str:
        i = len(num)-1
        for x in num[::-1]:
            if int(x)%2:
                break
            i -= 1
        if i<0:
            return ""
        else:
            return num[:i+1]
        
        


class Solution:
    def largestOddNumber(self, num: str) -> str:     
        for i in range(len(num) - 1, -1, -1) :
            if num[i] in {'1','3','5','7','9'} :
                return num[:i+1]
        return ''