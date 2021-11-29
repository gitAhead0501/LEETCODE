"""
1470. Shuffle the Array
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].

Constraints:
A) 1 <= n <= 500
B) nums.length == 2n
C) 1 <= nums[i] <= 10^3

Approach: Create an array and append it turn by turn the desired item

"""

from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr = []
        for i in range(n):
            arr.append(nums[i])
            arr.append(nums[i+n])
        return arr

'''
ONE LINERS : From Discussion Tab : 

    [nums[n*(i%2)+i//2] for i in range(2*n)]
	[j for i in range(n) for j in (nums[i], nums[i+n])]
	[x[i] for x in zip(nums[:n],nums[n:]) for i in [0,1]]
	[i for pair in zip(nums[:n],nums[n:]) for i in pair]
	[nums[int(i/2)] if i%2 == 0 else nums[int(i/2)+n] for i in range(2*n)]
	[nums[int(i/2)+n] if i%2 else nums[int(i/2)] for i in range(2*n)]
	sum(([nums[i], nums[i+n]] for i in range(n)), [])
	sum([list(x) for x in zip(nums[:n],nums[n:])],[])
	sum([nums[i::n] for i in range(n)],[])
	sum([[nums[i],nums[i+n]] for i in range(n)],[])
	[*functools.reduce(lambda y, x: y+x, zip(nums[:n], nums[n:]))]
	list(itertools.chain(*zip(nums[:n],nums[n:])))
	nums if [nums.insert((n - i), nums.pop()) for i in range(n)] != 0 else None
'''