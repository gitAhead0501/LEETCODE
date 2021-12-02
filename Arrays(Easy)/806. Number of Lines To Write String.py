"""
806. Number of Lines To Write String

You are given a string s of lowercase English letters and an array widths denoting how many pixels wide each lowercase English letter is. Specifically, widths[0] is the width of 'a', widths[1] is the width of 'b', and so on.

You are trying to write s across several lines, where each line is no longer than 100 pixels. Starting at the beginning of s, write as many letters on the first line such that the total width does not exceed 100 pixels. Then, from where you stopped in s, continue writing as many letters as you can on the second line. Continue this process until you have written all of s.

Return an array result of length 2 where:

result[0] is the total number of lines.
result[1] is the width of the last line in pixels.

Constraints:
A) widths.length == 26
B) 2 <= widths[i] <= 10
C) 1 <= s.length <= 1000
D) s contains only lowercase English letters.

Approach: Map every character to its width in widths array via ord relation : If width gets greater than 100 set wd to last added value and increment new line variable

"""
from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        i,j = 0,1
        wd = 0
        while i<len(s):
            w = widths[ord(s[i])-ord('a')]
            wd += w
            if wd>100:
                wd = w
                j+=1
            i+=1
        return [j,wd]