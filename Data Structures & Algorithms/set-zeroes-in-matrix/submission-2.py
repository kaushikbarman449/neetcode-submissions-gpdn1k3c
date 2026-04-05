class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # SC: O(1) solution

        n = len(matrix) # no. of rows
        m = len(matrix[0]) # no. of cols

        row0 = False
        col0 = False

        for j in range(m):
            if matrix[0][j] == 0: # fixed row i.e first row moving across columns
                row0 = True
                break

        for i in range(n):
            if matrix[i][0] == 0: # fixed col i.e first col moving across rows
                col0 = True
                break

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if row0:
            for j in range(m):
                matrix[0][j] = 0
        
        if col0:
            for i in range(n):
                matrix[i][0] = 0


        