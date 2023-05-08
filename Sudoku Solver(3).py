
def sudoku(puzzle):
    answer = None

    def solve(board):
        find = find_empty(board)
        if not find:
            nonlocal answer
            answer = board
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if valid(board, i, (row, col)):
                board[row][col] = i

                if solve(board):
                    return True

                board[row][col] = 0

        return False

    def valid(board, num, pos):
        # Check row
        for i in range(len(board[0])):
            if board[pos[0]][i] == num and pos[1] != i:
                return False

        # Check column
        for i in range(len(board)):
            if board[i][pos[1]] == num and pos[0] != i:
                return False

        # Check box
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if board[i][j] == num and (i, j) != pos:
                    return False

        return True

    def find_empty(board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    return (i, j)

        return None

    solve(puzzle)
    return answer


puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]




def sudoku1(P):
    for row, col in [(r, c) for r in range(9) for c in range(9) if not P[r][c]]:

        rr, cc = (row // 3) * 3, (col // 3) * 3

        use = {1, 2, 3, 4, 5, 6, 7, 8, 9} - (
                    {P[row][c] for c in range(9)} | {P[r][col] for r in range(9)} | {P[rr + r][cc + c] for r in range(3)
                                                                                     for c in range(3)})

        if len(use) == 1:
            P[row][col] = use.pop()
            return sudoku(P)
    return P

print(puzzle)
print(sudoku1(puzzle))
