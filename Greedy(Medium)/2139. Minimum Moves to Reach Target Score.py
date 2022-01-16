"""
2139. Minimum Moves to Reach Target Score

You are playing a game with integers. You start with the integer 1 and you want to reach the integer target.

In one move, you can either:

Increment the current integer by one (i.e., x = x + 1).
Double the current integer (i.e., x = 2 * x).
You can use the increment operation any number of times, however, you can only use the double operation at most maxDoubles times.

Given the two integers target and maxDoubles, return the minimum number of moves needed to reach target starting with 1.

Constraints:
A) 1 <= target <= 10^9
B) 0 <= maxDoubles <= 100

Approach: Iterate backwards from target to 1 , if target is even reduce it to half (if maxDoubles are available) if odd subtract 1 and make it even

"""

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        md = maxDoubles
        t = target
        count = 0
        while t>0 and md>0:
            if t%2:
                t -= 1
                count += 1
            else:
                t = t//2
                count += 1
                md -= 1
        if t == target:
            return target-1
        else:
            return count+t-1