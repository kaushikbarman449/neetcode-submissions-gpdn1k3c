class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # using brute force
        n = len(matrix)
        resultMatrix = [[0]*n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                resultMatrix[j][n-1-i] = matrix[i][j]

        for i in range(n):
            for j in range(n):
                matrix[i][j] = resultMatrix[i][j]