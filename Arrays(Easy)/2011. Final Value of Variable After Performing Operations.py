"""
2011. Final Value of Variable After Performing Operations
There is a programming language with only four operations and one variable X:

++X and X++ increments the value of the variable X by 1.
--X and X-- decrements the value of the variable X by 1.
Initially, the value of X is 0.

Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.

Constraints:
A) 1 <= operations.length <= 100
B) operations[i] will be either "++X", "X++", "--X", or "X--".


Approach: Simply follow the given question
"""


from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for each in operations:
            if each == "--X" or each == "X--":
                x = x - 1
            elif each == "++X" or each == "X++":
                x = x + 1
        return x