"""
1672. Richest Customer Wealth
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

Constraints:
A) m == accounts.length
B) n == accounts[i].length
C) 1 <= m, n <= 50
D) 1 <= accounts[i][j] <= 100


Approach1: Naive approach, create a max_ and array to store the values and return the max value
Approach2: Efficient : return max without storing
"""

from typing import List

# 1)
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sum = 0
        a = []
        for i in range(len(accounts)):
            sum = 0
            for each in accounts[i]:
                sum += each
            a.append(sum)
        max = a[0]
        for j in range(len(a)):
            if a[j] >= max:
                max = a[j]
        return max
    # OR THE ABOVE IN ONE LINE : 
    # return  max([sum(accounts[i][:]) for i in range(len(accounts))])

# 2)
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        osum = 0
        for rows in accounts:
            sum = 0
            for j in range(len(rows)):
                sum += rows[j]
            if sum > osum:
                osum = sum
        return osum