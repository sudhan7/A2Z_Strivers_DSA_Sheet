class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.val)

def ValidBST(root,left,right):
    if not root:
        return True
    if not (root.val < right and root.val > left):
        return False
    return(ValidBST(root.left,left,root.val) and ValidBST(root.right,root.val,right))

A = TreeNode(5)
B = TreeNode(8)
C = TreeNode(7)
D = TreeNode(8)
E = TreeNode(9)

A.left, A.right = B, C
C.left, C.right = D, E

print(ValidBST(A,float('-inf'),float('inf')))