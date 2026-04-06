class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # SC: O(1)
        n = len(matrix)
        # Step 1: Transpose
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Horizontal reverse the row elements
        for i in range(n):
            l, r = 0, n - 1
            while l < r:
                matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
                l += 1
                r -= 1
