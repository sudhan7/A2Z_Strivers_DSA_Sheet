class TreeNode:
    def __init__(self,val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.val)


def subtree(s,t):
    if not t: return True
    if not s: return False

    if isSameTree(s,t):
        return True
    
    return (subtree(s.left,t) or subtree(s.right,t))

def isSameTree(s,t):
    if not s and not t:
        return True
    
    if s and t and s.val == t.val:
        return (isSameTree(s.left,t.left) and isSameTree(s.right, t.right))
    
    return False

A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)

A.left,  A.right = B, C
B.left, B.right = D, E

F = TreeNode(2)
G = TreeNode(4)
H = TreeNode(5)

F.left, F.right = G, H

print(subtree(A,F))