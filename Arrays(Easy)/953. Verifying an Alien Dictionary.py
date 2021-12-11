"""
953. Verifying an Alien Dictionary

In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.


Constraints:
A) 1 <= words.length <= 100
B) 1 <= words[i].length <= 20
C) order.length == 26
D) All characters in words[i] and order are English lowercase letters.

Approach: For each word in words check lexo order of each character with next word i.e. compare i with i+1

"""


from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        h = {v:i for i,v in enumerate(order)}
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if j>=len(words[i+1]):
                    return False
                if words[i][j] != words[i+1][j]:
                    if h[words[i][j]] > h[words[i+1][j]]:
                        return False
                    break
        return True