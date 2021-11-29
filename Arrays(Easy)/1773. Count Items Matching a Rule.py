"""
1773. Count Items Matching a Rule
You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.

The ith item is said to match the rule if one of the following is true:

ruleKey == "type" and ruleValue == typei.
ruleKey == "color" and ruleValue == colori.
ruleKey == "name" and ruleValue == namei.
Return the number of items that match the given rule.

 

Constraints:
A) 1 <= items.length <= 104
B) 1 <= typei.length, colori.length, namei.length, ruleValue.length <= 10
C) ruleKey is equal to either "type", "color", or "name".
D) All strings consist only of lowercase letters.

Approach: Just follow problem statments

"""

from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        index = 0
        if ruleKey == "color": index = 1
        elif ruleKey == "name": index = 2
        
        count = 0
        for item in items:
            if item[index] == ruleValue: count += 1
        
        return count


# ANOTHER WAY OF WRITING THE ABOVE SOLUTION

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        for i in range(len(items)):
            if ruleKey == "type" and ruleValue == items[i][0]:
                count = count + 1
            elif ruleKey == "color" and ruleValue == items[i][1]:
                count = count + 1
            elif ruleKey == "name" and ruleValue == items[i][2]:
                count = count + 1
        return count