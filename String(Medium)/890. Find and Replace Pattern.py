"""
890. Find and Replace Pattern

Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.

Constraints:
A) 1 <= pattern.length <= 20
B) 1 <= words.length <= 50
C) words[i].length == pattern.length
D) pattern and words[i] are lowercase English letters.

Approach: Create a function for creating map for each word in words array. If each char in word is not present in map set it's default value as the length of the mapping variable else it's value that is stored in the map. Now for each word match the mapping of word with mapping of pattern string.

"""

from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def f(w):
            h = {}
            return [h.setdefault(c,len(h)) for c in w]
        return [w for w in words if f(w)==f(pattern)]