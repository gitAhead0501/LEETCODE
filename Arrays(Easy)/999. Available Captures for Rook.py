"""
999. Available Captures for Rook
On an 8 x 8 chessboard, there is exactly one white rook 'R' and some number of white bishops 'B', black pawns 'p', and empty squares '.'.

When the rook moves, it chooses one of four cardinal directions (north, east, south, or west), then moves in that direction until it chooses to stop, reaches the edge of the board, captures a black pawn, or is blocked by a white bishop. A rook is considered attacking a pawn if the rook can capture the pawn on the rook's turn. The number of available captures for the white rook is the number of pawns that the rook is attacking.

Return the number of available captures for the white rook.

Constraints:
A) board.length == 8
B) board[i].length == 8
C) board[i][j] is either 'R', '.', 'B', or 'p'
D) There is exactly one cell with board[i][j] == 'R'

Approach: First find the position of 'R' : move in each direction and search pawn in each direction and count until a Bishop arrives

GOOD QUESTION : DON'T KNOW Y IT'S GIVEN IN EASY CATEGORY

"""

from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # find the position of 'R'
        found = False
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    x0, y0 = i, j
                    found = True
                    break
            if found:
                break
        
        # move in each direction : i.e. NORTH SOUTH EAST WEST
        # search pawn in direction and count until a Bishop arrives
        res = 0
        for i,j in [[1,0],[-1,0],[0,-1],[0,1]]:
            x, y = x0+i, y0+j
            while 0<=x<8 and 0<=y<8:
                if board[x][y] == 'p': res+=1
                if board[x][y] != '.': break
                x+=i
                y+=j
        return res