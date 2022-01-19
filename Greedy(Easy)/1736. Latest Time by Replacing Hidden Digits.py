"""
1736. Latest Time by Replacing Hidden Digits

You are given a string time in the form of hh:mm, where some of the digits in the string are hidden (represented by ?).

The valid times are those inclusively between 00:00 and 23:59.

Return the latest valid time you can get from time by replacing the hidden digits.

Constraints:
A) time is in the format hh:mm.
B) It is guaranteed that you can produce a valid time from the given string.

Approach: If in hr time both steps are not known then set it to '23':latest time else if 1step is missing add 1 if 2nd step is between 4and9 inclusive else 2 , similarly for min time

"""

class Solution:
    def maximumTime(self, time: str) -> str:
        hr,mn = time.split(':')
        hr = list(hr)
        mn = list(mn)
        if hr[0]=='?' and hr[1]!='?':
            if 4<= int(hr[1]) <=9:
                hr[0] = "1"
            else:
                hr[0] = "2"
        if hr[1]=='?' and hr[0]!='?':
            if hr[0] == "2":
                hr[1] = "3"
            else:
                hr[1] = "9"
                
        if hr[0]=='?' and hr[1]=='?':
            hr[0] = "2"
            hr[1] = "3"
        
        if mn[0] == '?' and mn[1]!='?':
            mn[0] = "5"
        if mn[1] == '?' and mn[0]!='?':
            mn[1] = "9"
        if mn[0] == '?' and mn[1]=='?':
            mn[0] = "5"
            mn[1] = "9"
        hr.append(':')
        return "".join(hr+mn)