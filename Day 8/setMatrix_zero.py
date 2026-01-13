# def markRows(arr,row,n):
#     for j in range(n):
#         if arr[row][j] != 0:
#             arr[row][j] = -1

# def markCols(arr,col,m):
#     for i in range(m):
#         if arr[i][col] != 0:
#             arr[i][col] = -1

# def setMatrix_zero(arr):
#     n = len(arr)
#     print(n)
#     m = len(arr[0])
#     print(m)
#     for i in range(n):
#         for j in range(m):
#             if arr[i][j] == 0:
#                 markRows(arr,i,m)
#                 markCols(arr,j,n)
#     for i in range(n):
#         for j in range(m):
#             if arr[i][j] == -1:
#                 arr[i][j] = 0
#     return arr

# def setMatrix_zero(arr):
#     n = len(arr)
#     m = len(arr[0])

#     row = [0]*n
#     col = [0]*m

#     for i in range(n):
#         for j in range(m):
#             if arr[i][j] == 0:
#                 row[i] = 1
#                 col[j] = 1

#     for i in range(n):
#         for j in range(m):
#             if row[i] or col[j] == 1:
#                 arr[i][j] = 0
    
#     return arr

def setMatrix_zero(arr):
    #row = arr[..][0]
    #col = arr[0][..]
    
    n = len(arr)
    m = len(arr[0])

    first_row_zero = False
    first_col_zero = False

    for j in range(m):
        if arr[0][j] == 0:
            first_col_zero = True
            break
    
    for i in range(n):
        if arr[i][0] == 0:
            first_row_zero = True
            break
    for i in range(1,n):
        for j in range(1,m):
            if arr[i][j] == 0:
                arr[i][0] = 0
                arr[0][j] = 0
    
    for i in range(1,n):
        for j in range(1,m):
            if arr[i][0] == 0 or arr[0][j] == 0:
                arr[i][j] = 0

    if first_row_zero:
        for i in range(n):
            arr[i][0] = 0
    
    if first_col_zero:
        for j in range(m):
            arr[0][j] = 0
    
    return arr



arr = [[0,1,2,0],
       [3,4,5,2],
       [1,3,1,5]]
print(setMatrix_zero(arr))