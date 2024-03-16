def N_Queens(board, row, solution):
    n = len(board)
    if row == n:
        solution.extend(list(board))
        return True
    for col in range(n):
        if Place_check(board, row, col):
            board[row] = col
            if N_Queens(board, row + 1, solution):
                return True
            board[row] = -1
    return False

def Place_check(board, row, col):
    for r in range(row):
        c = board[r]
        if c == col or r - c == row - col or r + c == row + col:
            return False
    return True

n = int(input("Enter n: "))
board = [-1] * n
solution = []
N_Queens(board, 0, solution)
print(solution)