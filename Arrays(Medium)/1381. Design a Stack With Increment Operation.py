"""
1381. Design a Stack With Increment Operation

Design a stack which supports the following operations.

Implement the CustomStack class:

CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack or do nothing if the stack reached the maxSize.
void push(int x) Adds x to the top of the stack if the stack hasn't reached the maxSize.
int pop() Pops and returns the top of stack or -1 if the stack is empty.
void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements in the stack, just increment all the elements in the stack.

Constraints:
A) 1 <= maxSize <= 1000
B) 1 <= x <= 1000
C) 1 <= k <= 1000
D) 0 <= val <= 100
E) At most 1000 calls will be made to each method of increment, push and pop each separately.

Approach: Push(append till size is not maxSize) : Pop(till size is 0) : Increment(bottom k elements only)

"""

class CustomStack:

    def __init__(self, maxSize: int):
        self.st = []
        self.max = maxSize        

    def push(self, x: int) -> None:
        if len(self.st)!= self.max:
            self.st.append(x)

    def pop(self) -> int:
        if len(self.st) == 0:
            return -1
        else:
            return self.st.pop()

    def increment(self, k: int, val: int) -> None:
        if len(self.st) < k:
            for i in range(len(self.st)):
                self.st[i] += val
        else:
            for i in range(k):
                self.st[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)