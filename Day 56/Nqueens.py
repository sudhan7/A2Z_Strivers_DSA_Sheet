def solve(col,board,n,leftrow,lowerDiagonal,upperDiagonal,ans):
    if col == n:
        ans.append(["".join(row) for row in board])
        return
    
    for row in range(n):
        if leftrow[row] == 0 and lowerDiagonal[row+col] == 0 and upperDiagonal[n-1+col-row] == 0:
            board[row][col] = "Q"
            leftrow[row] = lowerDiagonal[row+col] = upperDiagonal[n-1+col-row] = 1
            solve(col+1,board,n,leftrow,lowerDiagonal,upperDiagonal,ans)
            board[row][col] = "."
            leftrow[row] = lowerDiagonal[row+col] = upperDiagonal[n-1+col-row] = 0

def NQueens(n):
    ans = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    leftrow = [0] * n
    lowerDiagonal = [0] * (2*n-1)
    upperDiagonal = [0] * (2*n-1)
    solve(0,board,n,leftrow,lowerDiagonal,upperDiagonal,ans)
    return ans

n = 4
res = NQueens(n)
for board in res:
    for row in board:
        print(row)
    print()
