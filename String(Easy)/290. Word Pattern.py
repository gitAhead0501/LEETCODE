"""
290. Word Pattern

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Constraints:
A) 1 <= pattern.length <= 300
B) pattern contains only lower-case English letters.
C) 1 <= s.length <= 3000
D) s contains only lowercase English letters and spaces ' '.
E) s does not contain any leading or trailing spaces.
F) All the words in s are separated by a single space.

Approach: Check if length of splitted string equals pattern's length or not, then check for every unique value is present in h and it's value equals to string's value or not, if not return False.
Also we need to check if there are any duplicates in h.values(), if there is then we need to return false.
Else True

"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        h = {}
        s = s.split()
        if len(s)!=len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in h:
                h[pattern[i]] = s[i]
            if pattern[i] in h and h[pattern[i]] != s[i]:
                return False
        arr = set()
        for x in h.values():
            if x in arr:
                return False
            else:
                arr.add(x)
        return True