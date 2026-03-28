def unique_paths(m,n):
    def recurse(row, col):
        if row == m-1 and col == n-1:
            return 1
        if row >= m or col >= n:
            return 0
        return recurse(row+1, col) + recurse(row , col+1)
    return recurse(0,0)

m = 3
n = 7
print(unique_paths(m,n))