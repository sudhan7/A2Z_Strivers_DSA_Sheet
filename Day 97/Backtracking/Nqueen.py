def issafe(row, col, board):
    n = len(board)
    
    # Check column above
    r = row
    while r >= 0:
        if board[r][col] == "Q":
            return False
        r -= 1
    
    # Check upper-left diagonal
    r, c = row , col 
    while r >= 0 and c >= 0:
        if board[r][c] == "Q":
            return False
        r -= 1
        c -= 1
    
    # Check upper-right diagonal
    r, c = row , col
    while r >= 0 and c < n:
        if board[r][c] == "Q":
            return False
        r -= 1
        c += 1
    
    return True

def solvequeen(n, board, row, results):
    if row == n:
        results.append(["".join(r) for r in board])  # store a snapshot
        return
    
    for col in range(n):
        if issafe(row, col, board):
            board[row][col] = "Q"
            solvequeen(n, board, row + 1, results)
            board[row][col] = "."  # backtrack

def nqueens(n):
    board = [["." ] * n for _ in range(n)]
    results = []
    solvequeen(n, board, 0, results)
    return results

n = 4
solutions = nqueens(n)
for s in solutions:
    for row in s:
        print(row)
    print()
