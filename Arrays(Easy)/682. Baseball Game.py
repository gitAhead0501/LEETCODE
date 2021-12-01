"""
682. Baseball Game
You are keeping score for a baseball game with strange rules. The game consists of several rounds, where the scores of past rounds may affect future rounds' scores.

At the beginning of the game, you start with an empty record. You are given a list of strings ops, where ops[i] is the ith operation you must apply to the record and is one of the following:

An integer x - Record a new score of x.
"+" - Record a new score that is the sum of the previous two scores. It is guaranteed there will always be two previous scores.
"D" - Record a new score that is double the previous score. It is guaranteed there will always be a previous score.
"C" - Invalidate the previous score, removing it from the record. It is guaranteed there will always be a previous score.
Return the sum of all the scores on the record.

Constraints:
A) 1 <= ops.length <= 1000
B) ops[i] is "C", "D", "+", or a string representing an integer in the range [-3 * 10^4, 3 * 10^4].
C) For operation "+", there will always be at least two previous scores on the record.
D) For operations "C" and "D", there will always be at least one previous score on the record.

Approach: Follow problem statement

"""

from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        record = []
        for each in ops:
            if each.lstrip('-').isdigit():
                record.append(int(each))
            elif each == 'C':
                record.pop()
            elif each == 'D':
                record.append(int(record[-1]*2))
            else:
                record.append(record[-1]+record[-2])
        return sum(record)
