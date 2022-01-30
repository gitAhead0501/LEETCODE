"""
2144. Minimum Cost of Buying Candies With Discount

A shop is selling candies at a discount. For every two candies sold, the shop gives a third candy for free.

The customer can choose any candy to take away for free as long as the cost of the chosen candy is less than or equal to the minimum cost of the two candies bought.

For example, if there are 4 candies with costs 1, 2, 3, and 4, and the customer buys candies with costs 2 and 3, they can take the candy with cost 1 for free, but not the candy with cost 4.
Given a 0-indexed integer array cost, where cost[i] denotes the cost of the ith candy, return the minimum cost of buying all the candies.

Constraints:
A) 1 <= cost.length <= 100
B) 1 <= cost[i] <= 100

Approach: sort the array and count only the sum of first and second max value from the end of the sorted array.

"""

from typing import List


# Method1: 
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        return sum(cost) - sum(sorted(cost)[-3::-3])



# Method2:
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        if len(cost)<3:
            return sum(cost)
        cost.sort(reverse=True)
        ans = 0
        for i in range(0,len(cost)-1,3):
            ans += cost[i]+cost[i+1]
        if i!=len(cost)-1:
            i+=3
            ans += sum(cost[i:])
        return ans