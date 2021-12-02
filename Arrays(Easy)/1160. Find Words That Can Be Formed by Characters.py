"""
1160. Find Words That Can Be Formed by Characters
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

Constraints:
A) 1 <= words.length <= 1000
B) 1 <= words[i].length, chars.length <= 100
C) words[i] and chars consist of lowercase English letters.

Appraoch1: If each letter's frequency in a word is greater than it's frequency in chars string's counter than it is not a good string
Approach2: OR we can say if we subtract counters of each word from chars and if result is not None then it is also not a good string

"""

from collections import Counter
from typing import List

# 1)
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        sum, cnt = 0, Counter(chars)
        for word in words:
            word_c = Counter(word)
            for each in word_c:
                if word_c[each] > cnt[each]:
                    break
            else:
                sum += len(word)
        return sum



# 2)
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cnt = Counter(chars)
        return sum(len(word) for word in words if not Counter(word)-cnt)