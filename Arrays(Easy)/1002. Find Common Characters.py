"""
1002. Find Common Characters

Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

Constraints:
A) 1 <= words.length <= 100
B) 1 <= words[i].length <= 100
C) words[i] consists of lowercase English letters.

Approach: For each letter in first word, count the frequencies of every letter in every word of array words , find min and if n>0 i.e. it is present in every word

"""

from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words)<2: return words
        arr = set(words[0])
        res = []
        for each in arr:
            n = min([word.count(each) for word in words])
            if n:
                res += [each]*n
        return res