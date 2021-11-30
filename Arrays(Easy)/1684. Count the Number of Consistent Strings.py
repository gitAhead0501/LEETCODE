"""
1684. Count the Number of Consistent Strings

You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words. 

Constraints:
A) 1 <= words.length <= 104
B) 1 <= allowed.length <= 26
C) 1 <= words[i].length <= 10
D) The characters in allowed are distinct.
E) words[i] and allowed contain only lowercase English letters.

Approach1: Use hashtable to store 'allowed' string , and for each word in array check if each in word is present in hashtable : EFFICIENT (than searching a item in array)
Approach2: BRUTE FORCE : NESTED FOR LOOP : Searching in array
Approach3: We can remove words from the array which do not coordinate with the string 'allowed' and return the length of the array
Approach4: We can count the no. of words which do not coordinate with the string allowed and subtract it from the length of the original array

"""

import copy
from typing import List

# 1) EFFICIENT:
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        h = {x:i for i,x in enumerate(allowed)}
        for each in words:
            for w in each:
                if w not in h:
                    flag = 0
                    break
                else:
                    flag = 1
            if flag:
                count += 1
        return count


# 3) 
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        n = copy.copy(words)
        for i in range(len(words)):
            for j in range(len(words[i])):
                if words[i][j] in allowed:
                    continue
                else:
                    n.remove(words[i])
                    break
        return len(n)


# 4) 
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        for word in words:
            for alphabet in word:
                if alphabet not in allowed:
                    count+=1
                    break
        return len(words)-count
