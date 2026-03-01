class TreeNode:
    def __init__(self,val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.val)

def sameBinaryTree(p,q):
    if not p and not q:
        return True
    
    if not p or not q or p.val != q.val:
        return False
    
    return (sameBinaryTree(p.left,q.left) and sameBinaryTree(p.right, q.right))

if __name__ == "__main__":
    A = TreeNode(1)
    B = TreeNode(2)
    C = TreeNode(3)

    D = TreeNode(1)
    E = TreeNode(2)
    F = TreeNode(3)

    A.left, A.right = B, C
    D.left, D.right = E, F

    print(sameBinaryTree(A,D))