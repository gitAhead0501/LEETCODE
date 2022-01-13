"""
1974. Minimum Time to Type Word Using Special Typewriter

There is a special typewriter with lowercase English letters 'a' to 'z' arranged in a circle with a pointer. A character can only be typed if the pointer is pointing to that character. The pointer is initially pointing to the character 'a'.

Each second, you may perform one of the following operations:

Move the pointer one character counterclockwise or clockwise.
Type the character the pointer is currently on.
Given a string word, return the minimum number of seconds to type out the characters in word.

Constraints:
A) 1 <= word.length <= 100
B) word consists of lowercase English letters.

Approach: For each character find the minimum value of its distance from prev character and its distance from the last character and return the minimum

"""

class Solution:
    def minTimeToType(self, word: str) -> int:
        count = 0
        ch = 'a'
        for char in word:
            x = abs(ord(char)-ord(ch))
            y = 26-abs(ord(char)-ord(ch))
            count += min(x,y)+1
            ch = char
        return count