class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for c in range(1, rowIndex + 1):
            next_value = row[-1] * (rowIndex - c + 1) // c
            row.append(next_value)
        
        return row