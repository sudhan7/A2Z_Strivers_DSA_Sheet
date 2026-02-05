def celebrity(matrix):
    n = len(matrix)
    top = 0
    down = n - 1

    while top < down:
        if matrix[top][down] == 1:
            top+=1
        elif matrix[down][top] == 1:
            down-=1
        else:
            top+=1
            down-=1
        
        if top > down:
            return -1
        
    for i in range(n):
        if top == i:
            continue
        if matrix[top][i] == 1 or matrix[i][top] == 0:
            return -1
    return top
        

#matrix = [ [0, 1, 1, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 1, 1, 0] ]
matrix = [ [0, 1], [1, 0] ]
print(celebrity(matrix))