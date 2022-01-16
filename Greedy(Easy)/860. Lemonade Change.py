"""
860. Lemonade Change

At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Note that you do not have any change in hand at first.

Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.

Constraints:
A) 1 <= bills.length <= 105
B) bills[i] is either 5, 10, or 20.

Approach: Note down five and ten $ coins, if five becomes less than 0: return false

"""

from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five,ten = 0,0
        for x in bills:
            if x == 5:
                five+=1
            elif x == 10:
                ten+=1
                five-=1
            elif ten>0:
                five-=1
                ten-=1
            else:
                five-=3
            if five<0:
                return False
        return True