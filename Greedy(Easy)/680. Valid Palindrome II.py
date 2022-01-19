"""
680. Valid Palindrome II

Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Constraints:
A) 1 <= s.length <= 105
B) s consists of lowercase English letters.

Approach: Find the index where the string violates the palindrome condition, check in that substring if after deleting one character can the substring become palindrome or not.

"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        while i<len(s)//2 and s[i] == s[-i-1]:
            i+=1
        s = s[i:len(s)-i]
        return s[1:] == s[1:][::-1] or s[:-1] == s[:-1][::-1]