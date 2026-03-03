class TreeNode:
    def __init__(self,val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.val)


def LCA(root,p,q):
    cur = root

    while cur:
        if p.val > cur.val and q.val > cur.val:
            cur = cur.right
        elif p.val < cur.val and q.val < cur.val:
            cur = cur.left
        else:
            return cur


A = TreeNode(5)
B = TreeNode(3)
C = TreeNode(8)
D = TreeNode(1)
E = TreeNode(4)
F = TreeNode(7)
G = TreeNode(9)
H = TreeNode(2)

A.left, A.right = B, C
B.left, B.right = D, E
C.left, C.right = F, G
D.left = H

print(LCA(A,B,E))