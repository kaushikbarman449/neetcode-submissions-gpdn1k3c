class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        columns = set()
        diagonals = set()       # r - c
        antiDiagonals = set()   # r + c

        board = [["."] * n for _ in range(n)]

        # actual backtracking steps
        def backtrack(row):
            if row == n:
                snapshot = ["".join(r) for r in board]
                ans.append(snapshot)
                return

            for column in range(n):
                if column in columns or (row - column) in diagonals or (row + column) in antiDiagonals:
                    continue

                columns.add(column)
                diagonals.add(row - column)
                antiDiagonals.add(row + column)
                board[row][column] = "Q"

                backtrack(row + 1)

                columns.remove(column)
                diagonals.remove(row - column)
                antiDiagonals.remove(row + column)
                board[row][column] = "."


        backtrack(0)
        return ans