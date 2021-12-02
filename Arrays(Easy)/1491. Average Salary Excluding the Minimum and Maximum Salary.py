"""
1491. Average Salary Excluding the Minimum and Maximum Salary

Given an array of unique integers salary where salary[i] is the salary of the employee i.

Return the average salary of employees excluding the minimum and maximum salary.

Constraints:
A) 3 <= salary.length <= 100
B) 10^3 <= salary[i] <= 10^6
C) salary[i] is unique.
D) Answers within 10^-5 of the actual value will be accepted as correct.

Approach: remove max and min value and return the avg of the array

"""

from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary.pop()
        salary.pop(0)
        return sum(salary)/len(salary)