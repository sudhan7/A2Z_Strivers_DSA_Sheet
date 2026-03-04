from collections import deque
class TreeNode:
    def __init__(self,val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.val)

def lever_order_traversal(root):
    q = deque()
    q.append(root)
    ans = []

    while q:
        temp = []
        qlen = len(q)

        for i in range(qlen):
            node = q.popleft()
            if node:
                temp.append(node.val)
                q.append(node.left)
                q.append(node.right)
        if temp:
            ans.append(temp)
        
    return ans

A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(6)
G = TreeNode(7)

A.left, A.right = B, C
B.left , B.right = D, E
C.left, C.right = F, G

print(lever_order_traversal(A))