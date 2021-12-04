"""
2073. Time Needed to Buy Tickets

There are n people in a line queuing to buy tickets, where the 0th person is at the front of the line and the (n - 1)th person is at the back of the line.

You are given a 0-indexed integer array tickets of length n where the number of tickets that the ith person would like to buy is tickets[i].

Each person takes exactly 1 second to buy a ticket. A person can only buy 1 ticket at a time and has to go back to the end of the line (which happens instantaneously) in order to buy more tickets. If a person does not have any tickets left to buy, the person will leave the line.

Return the time taken for the person at position k (0-indexed) to finish buying tickets.

Constraints:
A) n == tickets.length
B) 1 <= n <= 100
C) 1 <= tickets[i] <= 100
D) 0 <= k < n

Approach: Brute : Run loop until kth element is not zero, in each pass subtract -1 from every element : increment count 

"""

from typing import List

# 1)
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        i,count = 0,0
        while tickets[k]!=0:
            if tickets[i]!=0:
                tickets[i] -=1
                count += 1
            i = (i + 1) % len(tickets)
        return count


# 2)
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        return sum(min(tickets[k] - (i > k), num) for i, num in enumerate(tickets))