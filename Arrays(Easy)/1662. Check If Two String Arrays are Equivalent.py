"""
1662. Check If Two String Arrays are Equivalent
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

Constraints:
A) 1 <= word1.length, word2.length <= 103
B) 1 <= word1[i].length, word2[i].length <= 103
C) 1 <= sum(word1[i].length), sum(word2[i].length) <= 103
D) word1[i] and word2[i] consist of lowercase letters.

Approach: Just join the two array strings and compare : ONE LINER

"""

from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)