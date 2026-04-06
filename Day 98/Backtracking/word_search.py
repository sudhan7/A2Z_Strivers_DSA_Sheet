def word_search(board,word):
    row_len = len(board)
    col_len = len(board[0])

    def dfs(row,col,i):
        if i == len(word):
            return True
        
        if row < 0 or row >= row_len or col < 0 or col >= col_len:
            return False
        
        if board[row][col] != word[i]:
            return False
        
        visited = board[row][col]

        found = (dfs(row+1,col,i+1) or
                 dfs(row,col+1,i+1) or
                 dfs(row-1,col,i+1) or
                 dfs(row,col-1,i+1))
        
        board[row][col] = visited

        return found

    for r in range(row_len):
        for c in range(col_len):
            if dfs(r,c,0):
                return True
    
    return False

board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
word = "ABCCEDFSB"
print(word_search(board,word))