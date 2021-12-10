"""
1961. Check If String Is a Prefix of Array
Given a string s and an array of strings words, determine whether s is a prefix string of words.

A string s is a prefix string of words if s can be made by concatenating the first k strings in words for some positive k no larger than words.length.

Return true if s is a prefix string of words, or false otherwise.

Constraints:
A) 1 <= words.length <= 100
B) 1 <= words[i].length <= 20
C) 1 <= s.length <= 1000
D)words[i] and s consist of only lowercase English letters.

Approach1: Iterate in words array and check if previous concatenated string value is in string s or not if not return False else check if it is present then if length of concat string and string s is same or not

Approach2: For each word in words, check if word is present in s or not by slice method

m = len(words)
n = len(s)
k = len(slice)
"""

from typing import List

# 1) TC: O(m*n)
class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        res = ""
        for i in range(len(words)):
            res += words[i]
            if res in s:
                if len(res) == len(s):
                    return True    
        return False


# 2) TC: O(m*(n+k))
class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        i = 0
        for word in words:
            if s[i:i+len(word)]!=word:
                return False
            i+=len(word)
            if i==len(s):
                return True
        return False