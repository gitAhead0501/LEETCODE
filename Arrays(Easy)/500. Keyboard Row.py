"""
500. Keyboard Row

Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:
1) the first row consists of the characters "qwertyuiop",
2) the second row consists of the characters "asdfghjkl", and
3) the third row consists of the characters "zxcvbnm".


Constraints:
A) 1 <= words.length <= 20
B) 1 <= words[i].length <= 100
C) words[i] consists of English letters (both lowercase and uppercase). 

Approach: compare the set differences of each word and each row1/2/3

"""

from typing import List
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        res = []
        for each in words:
            if set(each.lower())-row1==set():
                res.append(each)
            if set(each.lower())-row2==set():
                res.append(each)
            if set(each.lower())-row3==set():
                res.append(each)
        return res