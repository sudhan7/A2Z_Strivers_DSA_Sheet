def issafe(row, col, board):

    r = row
    c = col

    while r >= 0:
        if board[r][c] == "Q":
            return False
        r-=1

    r = row
    while r >= 0 and c < len(board):
        if board[r][c] == "Q":
            return False
        r-=1
        c+=1
    
    r = row
    c = col

    while r >= 0 and c >= 0 :
        if board[r][c] == "Q":
            return False
        r-=1
        c-=1
    
    return True
    

def nqueens_2(n):
    board = [["."] * n for _ in range(n)]
    ans = [0]

    def solve(row):
        if row == n:
            ans[0] += 1
            return 
        
        for col in range(n):
            if issafe(row, col, board):
                board[row][col] = "Q"
                solve(row+1)
                board[row][col] = "."

    solve(0)
    return ans[0]

n = 4
print(nqueens_2(n))