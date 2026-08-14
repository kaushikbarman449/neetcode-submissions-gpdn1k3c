class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        def helper(r, c, index):
            if index == len(word):
                return True
            if (r < 0
                or r >= ROWS
                or c < 0
                or c >= COLS
                or board[r][c] != word[index]
            ):
                return False

            # now the backtracking
            temp = board[r][c]
            board[r][c] = '#'
            
            found = (
                helper(r + 1, c, index + 1)
                or helper(r - 1, c, index + 1)
                or helper(r, c + 1, index + 1)
                or helper(r, c - 1, index + 1)
            )

            board[r][c] = temp
            return found

        for r in range(ROWS):
            for c in range(COLS):
                if helper(r, c, 0):
                    return True
        
        return False