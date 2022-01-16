"""
2027. Minimum Moves to Convert String

You are given a string s consisting of n characters which are either 'X' or 'O'.

A move is defined as selecting three consecutive characters of s and converting them to 'O'. Note that if a move is applied to the character 'O', it will stay the same.

Return the minimum number of moves required so that all the characters of s are converted to 'O'.

Constraints:
A) 3 <= s.length <= 1000
B) s[i] is either 'X' or 'O'.

Approach: Check if character is X count++ and move three places ahead else move unit by unit

"""

class Solution:
    def minimumMoves(self, s: str) -> int:
        count,i = 0,0
        while i<len(s):
            if s[i]=='X':
                count+=1
                i+=3
            else:
                i+=1
        return count