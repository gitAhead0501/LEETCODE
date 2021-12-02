"""
1700. Number of Students Unable to Eat Lunch

The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.

The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step:

If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
Otherwise, they will leave it and go to the queue's end.
This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the i​​​​​​th sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference of the j​​​​​​th student in the initial queue (j = 0 is the front of the queue). Return the number of students that are unable to eat.

Constraints:
A) 1 <= students.length, sandwiches.length <= 100
B) students.length == sandwiches.length
C) sandwiches[i] is 0 or 1.
D) students[i] is 0 or 1.

Approach : Its clear that when the student preference and sandwich's availability match we need to pop left from both and when they don't match then we only pop left from student and append it to student i.e. student at the beginning goes to the end of the queue

Methods : Either use of list of deque

"""


from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        i = 0
        while i != len(students):
            if students[0] == sandwiches[0]:
                i = 0
                students.pop(0)
                sandwiches.pop(0)
            else:
                i += 1
                students.append(students.pop(0))
        return len(students)