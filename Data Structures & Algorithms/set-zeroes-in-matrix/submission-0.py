class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Better than brute force solution: O(2 x n x m)
        n = len(matrix)
        m = len(matrix[0])

        rows = [False] * n
        cols = [False] * m

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if rows[i] or cols[j]:
                    matrix[i][j] = 0