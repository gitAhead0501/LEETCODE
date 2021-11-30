"""
1475. Final Prices With a Special Discount in a Shop
Given the array prices where prices[i] is the price of the ith item in a shop.

There is a special discount for items in the shop, if you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i], otherwise, you will not receive any discount at all.

Return an array where the ith element is the final price you will pay for the ith item of the shop considering the special discount.

Constraints:
A) 1 <= prices.length <= 500
B) 1 <= prices[i] <= 10^3

Approach: Logical implementation of Stacks : Monotonic stack
We have to find the minimum value of discount in succeeding array
Store indices in stack and change the original array in place
"""

from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for i in range(len(prices)):
            while stack and (prices[stack[-1]] >= prices[i]):
                prices[stack.pop()] -= prices[i]
            stack.append(i)
        return prices