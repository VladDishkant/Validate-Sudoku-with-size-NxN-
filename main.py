# This program get input array size NxN and check valid this sudoku solution or no.
# Author: Vladyslav Dyshkant

import numpy as np
import math

# 1) check if we have N arrays for N elements -> and N > 0
# 2) check rows with 1..N numbers without repeats
# 3) check columns with 1..N numbers without repeats
# 4) check N arrays (N/sqrt(N))x(N/sqrt(N)) with 1..N numbers without repeats
# 4x4 if we devided 2 we have 4 parts 2x2
# 9x9 if we devided 3 we have 9 parts 3x3 -> NxN if we devided N/sqrt(N) we have N parts (N/sqrt(N))x(N/sqrt(N))

# Valid Sudoku
class Sudoku(object):
    def __init__(self, data):
        self.data = data
    def is_valid(self):
        N = len(self.data)
        numbers = list(range(1, N+1))

        if N > 0:
            if ".0" not in str(math.sqrt(N)):
                return False
            for i in range(N):
                if N != len(self.data[i]) or str(numbers) != str(sorted(self.data[i])):
                    return False

            rotateData = np.rot90(self.data)
            for i in range(N):
                if numbers != sorted(rotateData[i]):
                    return False

            littleSquares = int(N/math.sqrt(N))
            for x in range(littleSquares):
                for y in range(littleSquares):
                    temp = []
                    for i in range(littleSquares):
                        for j in range(littleSquares):
                            temp.append(self.data[i+littleSquares*x][j+littleSquares*x])
                    if numbers != sorted(temp):
                        return False
        else:
            return False
        return True

sudoku = Sudoku([
    [7, 8, 4, 1, 5, 9, 3, 2, 6],
    [5, 3, 9, 6, 7, 2, 8, 4, 1],
    [6, 1, 2, 4, 3, 8, 7, 5, 9],

    [9, 2, 8, 7, 1, 5, 4, 6, 3],
    [3, 5, 7, 8, 4, 6, 1, 9, 2],
    [4, 6, 1, 9, 2, 3, 5, 8, 7],

    [8, 7, 6, 3, 9, 4, 2, 1, 5],
    [2, 4, 3, 5, 6, 1, 9, 7, 8],
    [1, 9, 5, 2, 8, 7, 6, 3, 4]
])

print(Sudoku.is_valid(sudoku))