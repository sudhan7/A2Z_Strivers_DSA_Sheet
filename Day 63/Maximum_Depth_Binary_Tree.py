from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

def BFS(node):
    q = deque()
    q.append(node)

    while q :
        node = q.popleft()
        print(node)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)

def max_depth(root):
    if not root:
        return 0
    
    return 1 + max(max_depth(root.left),max_depth(root.right))


if __name__ == '__main__':
    A = TreeNode(1)
    B = TreeNode(2)
    C = TreeNode(3)
    D = TreeNode(4)
    

    A.left, A.right = B, C
    C.left = D

    print(max_depth(A))
    
    