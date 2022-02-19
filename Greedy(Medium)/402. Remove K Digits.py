"""
402. Remove K Digits
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

Constraints:
A) 1 <= k <= num.length <= 105
B) num consists of only digits.
C) num does not have any leading zeros except for the zero itself.

Approach: Iterate over the num string store only non-zero values and run a while loop for popping values less than stack's top. If the string is monotonic, then k will not change inside the loop. Then the answer is obtained by removing the last k characters from the num string.

"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num:
            while stack and k and stack[-1]>n:
                stack.pop()
                k-=1
            if stack or n is not '0':
                stack.append(n)
        if k:
            stack = stack[:-k]
        return ''.join(stack) or '0'


" wrong solution/approach : not valid for all testcases"
# stack = []
        # i = 1
        # n = len(num)
        # while i<n and k:
        #     if num[i-1]<=num[i]:
        #         if num[i-1]:
        #             stack.append(num[i-1])
        #         k-=1
        #     i+=1
        # print(i,stack)
        # if not stack:
        #     return "0"
        # for k in range(i-1,n):
        #     stack.append(num[k])
        # ans = "".join(stack).lstrip('0')
        # if not ans:
        #     return  "0"
        # return ans
    
    # "10404050225366600200" 3
        
        # stack = [num[0]]
        # i=1
        # n = len(num)
        # while i<n and k:
        #     if stack[-1]<num[i]:
        #         k-=1
        #     elif stack[-1]>num[i]:
        #         stack.pop()
        #         stack.append(num[i])
        #         k-=1
        #     else:
        #         stack.append(num[i])
        #     i+=1
        # while k>0:
        #     if stack:
        #         stack.pop()
        #     k-=1
        # stack += num[i:]
        # ans = "".join(stack).lstrip('0')
        # if not ans:
        #     return '0'
        # return ans