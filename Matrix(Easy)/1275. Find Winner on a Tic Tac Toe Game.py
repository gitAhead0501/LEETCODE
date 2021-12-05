"""
1275. Find Winner on a Tic Tac Toe Game
Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:

1. Players take turns placing characters into empty squares ' '.
2. The first player A always places 'X' characters, while the second player B always places 'O' characters.
3. 'X' and 'O' characters are always placed into empty squares, never on filled ones.
4. The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
5. The game also ends if all squares are non-empty.
6. No more moves can be played if the game is over.

Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw". If there are still movements to play return "Pending".

You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first.

Constraints:
A) 1 <= moves.length <= 9
B) moves[i].length == 2
C) 0 <= rowi, coli <= 2
D) There are no repeated elements on moves.
E) moves follow the rules of tic tac toe.

Approach: after filling the grid with moves : check if any row or column or diagonal contains same value 'x' or 'o' : return accordingly

"""

from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]

        def check(grid):
            if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != '.':
                if grid[0][0] == 'x':
                    return 'A'
                else:
                    return 'B'
            elif grid[0][0] == grid[0][1] == grid[0][2] and grid[0][0] != '.':
                if grid[0][0] == 'x':
                    return 'A'
                else:
                    return 'B'        
            elif grid[0][0] == grid[1][0] == grid[2][0] and grid[0][0] != '.':
                if grid[0][0] == 'x':
                    return 'A'
                else:
                    return 'B'        
            elif grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != '.':
                if grid[0][2] == 'x':
                    return 'A'
                else:
                    return 'B'
            elif grid[1][0] == grid[1][1] == grid[1][2] and grid[1][0] != '.':
                if grid[1][0] == 'x':
                    return 'A'
                else:
                    return 'B'        
            elif grid[2][0] == grid[2][1] == grid[2][2] and grid[2][0] != '.':
                if grid[2][0] == 'x':
                    return 'A'
                else:
                    return 'B'    
            elif grid[0][1] == grid[1][1] == grid[2][1] and grid[0][1] != '.':
                if grid[0][1] == 'x':
                    return 'A'
                else:
                    return 'B'        
            elif grid[0][2] == grid[1][2] == grid[2][2] and grid[0][2] != '.':
                if grid[0][2] == 'x':
                    return 'A'
                else:
                    return 'B'
            return 'D'

        j = 0
        for i in moves:
            x, y = i[0], i[1]
            if j % 2 == 0:
                grid[x][y] = 'x'
            else:
                grid[x][y] = 'o'
            j += 1

        if check(grid) == 'A':
            return 'A'
        elif check(grid) == 'B':
            return 'B'

        if check(grid) == 'D' and j <= 8:
            return 'Pending'
        else:
            return 'Draw'