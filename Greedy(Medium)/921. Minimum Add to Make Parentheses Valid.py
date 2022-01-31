"""
921. Minimum Add to Make Parentheses Valid

A parentheses string is valid if and only if:

It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.


Constraints:
A) 1 <= s.length <= 1000
B) s[i] is either '(' or ')'.


Approach1: for each char '(' count right opening and for each ')' count left opening if right>0 decrement right
Approach2: use stack

"""

# 1) O(n) : time and space both
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left,right = 0,0
        for p in s:
            if p == '(':
                right+=1
            elif right>0:
                right-=1
            else:
                left+=1
        return left+right



# 2) O(n) : time and O(1): space
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for p in s:
            if p == '(':
                stack.append(p)
            else:
                if not stack:
                    stack.append(p)
                elif stack[-1] != '(':
                    stack.append(p)
                else:
                    stack.pop()
        return len(stack)