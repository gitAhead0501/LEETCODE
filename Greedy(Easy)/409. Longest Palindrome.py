"""
409. Longest Palindrome

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Constraints:
A) 1 <= s.length <= 2000
B) s consists of lowercase and/or uppercase English letters only.

Approach: Create a hashtable and check the frequency if it's odd add value-1 to the count and add 1 to the one variable and if it's even add value to the count and if the frequency is 1 , add 1 to the one variable: if 'one' is not 0: return count+one else: return count

"""

from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        count = 0
        one = 0
        for k,v in cnt.items():
            if v>1 and not v%2:
                count += v
            elif v>1 and v%2:
                count += v-1
                one += 1
            else:
                one += 1
        if one:
            return count+1
        else:
            return count