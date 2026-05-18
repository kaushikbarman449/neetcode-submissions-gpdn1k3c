class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(numRows):
            row = [1]
            for c in range(1, i + 1):
                next_value = row[-1] * (i - c + 1) // c
                row.append(next_value)

            triangle.append(row)
        
        return triangle