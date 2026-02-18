def Word_Search(board,word):
    row = len(board)
    col = len(board[0])

    def dfs(i,j,idx):
        if idx == len(word):
            return True
        
        if i<0 or j<0 or i>= row or j>= col or board[i][j] != word[idx]:
            return False
        temp = board[i][j]
        board[i][j] = "#"

        found = (dfs(i+1,j,idx+1) or
                 dfs(i-1,j,idx+1) or
                 dfs(i,j+1,idx+1) or
                 dfs(i,j-1,idx+1))
        
        board[i][j] = temp
        return found

    for i in range(row):
        for j in range(col):
            if dfs(i,j,0):
                return True
    return False

board = [["A", "B", "C", "E"], 
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]] 
word = "ABCCED"
print(Word_Search(board,word))
word = "SEE"
print(Word_Search(board,word))
word = "ABCB"
print(Word_Search(board,word))