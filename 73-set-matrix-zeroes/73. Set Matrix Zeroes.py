class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # go through the whole matrix and 
        # set the (i, 0) as indicating the 0 for horizontal
        # set the (0, j) as indicating the 0 for vertical
        # traverse the matrix again for putting the 0
        # time: O(2*M*N) space:O(1)
        oriTopLeftCorner = matrix[0][0]
        clearTopRight = matrix[0][0]
        clearTopDown = matrix[0][0]

        for i in range(1, len(matrix), 1):
            if matrix[i][0] == 0:
                clearTopRight = 0
                break
        for j in range(1, len(matrix[0]), 1):
            if matrix[0][j] == 0:
                clearTopDown = 0
                break
        for i in range(1, len(matrix), 1):
            for j in range(1, len(matrix[0]), 1):
                if matrix[i][j] == 0:
                    if i != 0:
                        matrix[0][j] = 0
                    if j!= 0:
                        matrix[i][0] = 0
        # print(matrix)
        # finishing building the 0 indicator
        # should not modify the first row and column
        for i in range(1, len(matrix), 1):
            for j in range(1, len(matrix[0]), 1):
                matrix[i][j] = 0 if (matrix[0][j]==0 or matrix[i][0]==0) else matrix[i][j]
        if clearTopRight == 0:
            for i in range(0, len(matrix), 1):
                matrix[i][0] = 0
        if clearTopDown == 0:
            for j in range(0, len(matrix[0]), 1):
                matrix[0][j] = 0
        return

        