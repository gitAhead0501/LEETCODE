"""
832. Flipping an Image
Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.

For example, flipping [1,1,0] horizontally results in [0,1,1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.

For example, inverting [0,1,1] results in [1,0,0].

Constraints:
A) n == image.length
B) n == image[i].length
C) 1 <= n <= 20
D) images[i][j] is either 0 or 1.

Approach:
First flip(reverse) each row in matrix
Then invert 0 and 1 in each row

"""

from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for each in image:
            each[:] = each[::-1]
            for i in range(len(each)):
                if each[i] == 0:
                    each[i] = 1
                else:
                    each[i] = 0
        return image