class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        low, high = 0, (m * n) - 1

        while low <= high:
            mid = (low + high) // 2
            row = mid // n
            col = mid % n

            value = matrix[row][col]
            if value == target:
                return True
            elif value > target:
                high = mid - 1
            else:
                low = mid + 1

        return False 