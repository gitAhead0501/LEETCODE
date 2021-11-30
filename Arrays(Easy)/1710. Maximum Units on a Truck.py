"""
1710. Maximum Units on a Truck
You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

numberOfBoxesi is the number of boxes of type i.
numberOfUnitsPerBoxi is the number of units in each box of the type i.
You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.

Constraints:
A) 1 <= boxTypes.length <= 1000
B) 1 <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000
C) 1 <= truckSize <= 106

Approach: Reverse sort the boxTypes array w.r.t. no of units in each box i.e. wrt to index 1 and compute the ans

"""

from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # boxtypes = sorted(boxTypes, key = lambda x:x[1], reverse = True)
        #   OR the below one
        boxTypes.sort(key = lambda x:-x[1])
        res = 0
        for each in boxTypes:
            if each[0] < truckSize:
                truckSize -= each[0]
                res += each[0]*each[1]
            elif each[0] >= truckSize:
                res += truckSize*each[1]
                break
        return res