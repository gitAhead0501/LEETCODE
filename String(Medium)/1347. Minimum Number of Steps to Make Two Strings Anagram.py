"""
1347. Minimum Number of Steps to Make Two Strings Anagram

You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

Constraints:
A) 1 <= s.length <= 5 * 104
B) s.length == t.length
C) s and t consist of lowercase English letters only.

Approach: Count the occurence of each character in both strings, subtract the similar character's value and return the sum of remaining occurences

"""

import collections


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ss,tt = map(collections.Counter, (s, t))
        return sum((ss-tt).values())