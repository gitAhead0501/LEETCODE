"""
937. Reorder Data in Log Files
You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

There are two types of logs:

Letter-logs: All words (except the identifier) consist of lowercase English letters.
Digit-logs: All words (except the identifier) consist of digits.
Reorder these logs so that:

1) The letter-logs come before all digit-logs.
2) The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
3) The digit-logs maintain their relative ordering.
4) Return the final order of the logs.

Constraints:
A) 1 <= logs.length <= 100
B) 3 <= logs[i].length <= 100
C) All the tokens of logs[i] are separated by a single space.
D) logs[i] is guaranteed to have an identifier and at least one word after the identifier.

Approach: Maintain letters and digits array : sort letter by it identified i.e. [0] , then sort by its contents i.e. [1:]

"""

from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter,digit = [],[]
        for each in logs:
            if each.split()[1].isdigit():
                digit.append(each)
            else:
                letter.append(each)
        letter.sort(key = lambda x:x.split()[0])
        letter.sort(key = lambda x:x.split()[1:])
        return letter+digit