class Solution:
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                current = board[row][col]

                if current == ".":
                    continue

                box = (row // 3) * 3 + (col // 3)

                if (current in rows[row] or
                    current in cols[col] or
                    current in boxes[box]):
                    return False

                rows[row].add(current)
                cols[col].add(current)
                boxes[box].add(current)

        return True